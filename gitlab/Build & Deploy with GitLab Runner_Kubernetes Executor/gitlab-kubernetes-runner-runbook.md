# GitLab CI/CD with One Kubernetes-Based Runner (Helm)

> **Purpose:** A self-contained runbook to rebuild, understand,
> troubleshoot, and continue this GitLab.com + local Kubernetes
> lab---even after a long break.
>
> **Last updated:** 5 November 2026\
> **GitLab URL:** `https://gitlab.com`\
> **Runner manager:** one replica\
> **Executor:** Kubernetes\
> **Helm release:** `gitlab-runner`\
> **Runner namespace:** `gitlab-runner`\
> **Job namespace:** `gitlab-ci-jobs`\
> **Observed chart version:** `0.94.2`\
> **Observed Runner version:** `19.5.2`

------------------------------------------------------------------------

## 1. Goal and expected architecture

The goal is to install **one GitLab Runner manager** in the local
Kubernetes cluster using Helm. The runner uses the Kubernetes executor.
For every GitLab CI job, it asks Kubernetes to create a temporary job
pod using the image declared in that job's `.gitlab-ci.yml`.

``` text
                         GitLab.com
                             |
                      Project pipeline
                       .gitlab-ci.yml
                             |
                             v
               GitLab Runner manager (one pod)
                  Namespace: gitlab-runner
                  ServiceAccount: gitlab-runner
                             |
                      Kubernetes API
                             |
                  Role / RoleBinding grants
                    access to job namespace
                             |
                             v
                  Namespace: gitlab-ci-jobs
                    /       |       \
                   v        v        v
               Alpine    Python    Terraform
               job pod   job pod    job pod
                    \       |       /
                     scripts execute
                             |
                     job pods cleaned up
```

### Key concept: one runner, many job images

Do **not** install one runner per language or tool.

The runner manager is the long-lived component. The Kubernetes executor
creates a separate temporary pod for each job, using that job's `image:`
value. For example:

-   `alpine:3.21`
-   `ubuntu:24.04`
-   `python:3.12-slim`
-   `node:22-alpine`
-   `hashicorp/terraform:1.9.8`

The job pods are separate from the runner manager pod.

------------------------------------------------------------------------

## 2. Important terminology

  -----------------------------------------------------------------------
  Term                                Meaning
  ----------------------------------- -----------------------------------
  GitLab Runner manager               Long-running pod that polls GitLab
                                      and coordinates jobs

  Runner authentication token         Secret credential beginning with
                                      `glrt-`; connects the runner to
                                      GitLab

  Registry credential                 Separate credential used to pull
                                      private container images

  Kubernetes executor                 Runner executor that creates job
                                      pods through the Kubernetes API

  Job image                           Container image specified by
                                      `image:` in a CI job

  Helper container                    Runner-provided container used for
                                      Git checkout, artifacts, and job
                                      support

  ServiceAccount                      Kubernetes identity used by the
                                      runner manager

  Role / RoleBinding                  Namespace-scoped permissions
                                      granted to that ServiceAccount

  Helm values file                    Configuration used to install or
                                      upgrade the runner chart
  -----------------------------------------------------------------------

**Never confuse the runner authentication token with a container
registry token.** They serve different purposes.

------------------------------------------------------------------------

## 3. Prerequisites and initial checks

Run these commands on the machine where `kubectl` and Helm are
configured:

``` bash
echo "===== KUBERNETES CONTEXT ====="
kubectl config current-context

echo "===== NODES ====="
kubectl get nodes -o wide

echo "===== KUBERNETES VERSION ====="
kubectl version

echo "===== HELM VERSION ====="
helm version

echo "===== NAMESPACES ====="
kubectl get namespaces

echo "===== NODE ARCHITECTURE ====="
kubectl get nodes \
  -o jsonpath='{range .items[*]}{.metadata.name}{" : "}{.status.nodeInfo.architecture}{"\n"}{end}'
```

Architecture reference:

-   `amd64` / `x86_64`: 64-bit Intel/AMD
-   `arm64` / `aarch64`: 64-bit ARM

Check that the cluster has enough CPU and memory for the runner and job
pods:

``` bash
kubectl describe nodes
kubectl top nodes
```

`kubectl top` requires Metrics Server to be installed and working.

------------------------------------------------------------------------

## 4. Create the GitLab project runner

In GitLab.com:

1.  Open the target project.
2.  Go to **Settings → CI/CD → Runners**.
3.  Select **Create project runner**.
4.  Set a description such as `k8s-helm-runner`.
5.  Add the tag `kube`.
6.  Enable **Run untagged jobs** if desired. Jobs in this runbook
    explicitly use the `kube` tag.
7.  For a lab, leave **Protected** disabled unless the target branch is
    protected and you specifically want a protected runner.
8.  Create the runner.
9.  Copy the generated **runner authentication token**.

The token normally begins with:

``` text
glrt-
```

### Important: legacy registration-token error

The following GitLab message was encountered:

``` text
Creating runners with runner registration tokens is disabled.
```

This means the legacy registration-token workflow is disabled. Do not
try to create a runner using the old registration token.

Use the new workflow: create a runner in the GitLab UI and use its
**runner authentication token** (`glrt-...`) with the Helm chart.

Do not put a real token in this Markdown file, a Git repository, a CI
log, or a screenshot. If a token is exposed, revoke/rotate it in GitLab.

------------------------------------------------------------------------

## 5. Create namespaces

This runbook uses separate namespaces for the runner manager and job
pods:

``` bash
kubectl create namespace gitlab-runner
kubectl create namespace gitlab-ci-jobs
```

If a namespace already exists, Kubernetes may report `AlreadyExists`;
that is not a problem.

Verify:

``` bash
kubectl get namespaces
```

------------------------------------------------------------------------

## 6. Create the runner authentication Secret

The Helm chart configuration in this lab expects a Secret named
`gitlab-runner-token`.

The Secret must contain the keys expected by the installed chart. In
this setup, use:

-   `runner-token`: the actual `glrt-...` runner authentication token
-   `runner-registration-token`: an empty compatibility value

### Recommended command (create or update)

This method is repeatable because it uses `apply`:

``` bash
read -s -p "Enter GitLab runner authentication token: " RUNNER_TOKEN
echo

kubectl create secret generic gitlab-runner-token \
  --namespace gitlab-runner \
  --from-literal=runner-token="$RUNNER_TOKEN" \
  --from-literal=runner-registration-token="" \
  --dry-run=client -o yaml | kubectl apply -f -

unset RUNNER_TOKEN
```

Alternative: if the shell variable has already been populated, the
following command is valid, but without `--dry-run ... | kubectl apply`,
it fails if the Secret already exists:

``` bash
kubectl create secret generic gitlab-runner-token \
  -n gitlab-runner \
  --from-literal=runner-token="$RUNNER_TOKEN" \
  --from-literal=runner-registration-token=""
```

### Verify key names without decoding the token

``` bash
kubectl get secret gitlab-runner-token \
  -n gitlab-runner \
  -o jsonpath='{.data}' 
echo
```

The output should include both key names:

``` text
runner-token
runner-registration-token
```

Do not use `kubectl get secret ... -o yaml` in a shared screenshot or
support message: Secret data is base64-encoded, not encrypted.

------------------------------------------------------------------------

## 7. Install the GitLab Runner Helm chart

Add and update the chart repository:

``` bash
helm repo add gitlab https://charts.gitlab.io
helm repo update
helm search repo gitlab/gitlab-runner
```

Create a working directory:

``` bash
mkdir -p ~/gitlab-k8s-runner
cd ~/gitlab-k8s-runner
```

Create `values.yaml`:

``` yaml
gitlabUrl: https://gitlab.com

# The authentication token is supplied through the Kubernetes Secret.
runnerToken: ""

runners:
  secret: gitlab-runner-token
  tags: "kube"
  runUntagged: true
  locked: false

  config: |
    [[runners]]
      name = "k8s-helm-runner"
      executor = "kubernetes"

      [runners.kubernetes]
        namespace = "gitlab-ci-jobs"
        image = "alpine:3.21"

        privileged = false
        poll_timeout = 600

        # Explicit default policy avoids an empty pull policy.
        pull_policy = ["always"]

        # These are the policies jobs are allowed to request.
        allowed_pull_policies = ["always", "if-not-present"]

        # Lab setting: allow jobs to select different images.
        # Restrict this in production to trusted registries/images.
        allowed_images = ["*"]
        allowed_services = ["*"]

        cpu_request = "100m"
        cpu_limit = "1000m"
        memory_request = "128Mi"
        memory_limit = "1Gi"

        helper_cpu_request = "100m"
        helper_memory_request = "128Mi"

# The chart creates the runner manager ServiceAccount and its
# chart-managed permissions. The separate job-namespace Role and
# RoleBinding in section 8 grant the cross-namespace job permissions.
rbac:
  create: true
  clusterWideAccess: false

serviceAccount:
  create: true

replicas: 1
concurrent: 5
```

### Configuration notes

-   `replicas: 1`: one runner manager pod.
-   `concurrent: 5`: up to five jobs can be handled concurrently by this
    runner configuration. Actual parallelism is limited by cluster
    resources.
-   `namespace = "gitlab-ci-jobs"`: job pods are created in this
    namespace.
-   `privileged = false`: safer default; suitable for the image-testing
    examples below.
-   `pull_policy = ["always"]`: the default image pull policy used by
    jobs.
-   `allowed_pull_policies`: policies that jobs are permitted to use.
-   `allowed_images = ["*"]`: permits arbitrary job images for this
    learning lab. In a production environment, restrict this to trusted
    registries and approved image patterns.
-   `allowed_services = ["*"]`: permits arbitrary service images for
    this lab. Restrict it if services are not needed.

**Do not hardcode an architecture-specific helper image** unless you
have confirmed the cluster architecture and have a specific reason to
override the chart/runner default.

### Install

``` bash
helm install gitlab-runner \
  gitlab/gitlab-runner \
  --namespace gitlab-runner \
  --values values.yaml
```

If the release already exists, use `helm upgrade` instead of
`helm install`:

``` bash
helm upgrade gitlab-runner \
  gitlab/gitlab-runner \
  --namespace gitlab-runner \
  --values values.yaml
```

Check:

``` bash
helm list -n gitlab-runner
kubectl get pods -n gitlab-runner
kubectl get configmap -n gitlab-runner
```

------------------------------------------------------------------------

## 8. Grant the runner permissions in the job namespace

### Why this is necessary

The runner manager runs in namespace `gitlab-runner` with this
ServiceAccount:

``` text
system:serviceaccount:gitlab-runner:gitlab-runner
```

The Kubernetes executor creates job resources in the separate namespace
`gitlab-ci-jobs`.

The runner therefore needs permission in `gitlab-ci-jobs`. A Role in
`gitlab-runner` alone does not grant permissions in `gitlab-ci-jobs`.

Create `gitlab-runner-rbac.yaml`:

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: gitlab-runner-job-role
  namespace: gitlab-ci-jobs
rules:
  # Create, inspect, watch, and delete CI job pods.
  - apiGroups: [""]
    resources:
      - pods
    verbs:
      - create
      - delete
      - get
      - list
      - watch

  # Attach to job containers and execute commands.
  - apiGroups: [""]
    resources:
      - pods/attach
      - pods/exec
    verbs:
      - create
      - delete
      - get
      - patch

  # Read job logs.
  - apiGroups: [""]
    resources:
      - pods/log
    verbs:
      - get

  # Manage job-specific credentials/secrets.
  - apiGroups: [""]
    resources:
      - secrets
    verbs:
      - create
      - delete
      - get
      - update

  # Create and remove job services when needed.
  - apiGroups: [""]
    resources:
      - services
    verbs:
      - create
      - delete
      - get

  # Read events for troubleshooting.
  - apiGroups: [""]
    resources:
      - events
    verbs:
      - get
      - list
      - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: gitlab-runner-job-rolebinding
  namespace: gitlab-ci-jobs
subjects:
  - kind: ServiceAccount
    name: gitlab-runner
    namespace: gitlab-runner
roleRef:
  kind: Role
  name: gitlab-runner-job-role
  apiGroup: rbac.authorization.k8s.io
```

Apply:

``` bash
kubectl apply -f gitlab-runner-rbac.yaml
```

### Verify permissions

``` bash
kubectl auth can-i create pods \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i create secrets \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i create services \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i list pods \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i create pods/attach \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner
```

Expected output for these checks:

``` text
yes
yes
yes
yes
yes
```

The user running `kubectl auth can-i --as=...` must themselves be
allowed to impersonate that ServiceAccount. If the command reports an
impersonation error, check your own Kubernetes permissions; that is
different from the runner's RoleBinding.

**Least-privilege note:** The Role above is the lab permission set used
during troubleshooting. Review it against the features enabled in your
Runner version and configuration. Do not replace it with `cluster-admin`
or wildcard permissions as a shortcut. Some optional Runner features or
newer versions may require additional narrowly scoped permissions.

------------------------------------------------------------------------

## 9. Verify runner registration and pod health

``` bash
kubectl get pods -n gitlab-runner -o wide

kubectl logs deployment/gitlab-runner \
  -n gitlab-runner
```

Follow logs:

``` bash
kubectl logs -f deployment/gitlab-runner \
  -n gitlab-runner
```

Check the GitLab project:

**Project → Settings → CI/CD → Runners**

The project runner should be online and should have the `kube` tag.

If the Deployment name differs, discover it:

``` bash
kubectl get deployments -n gitlab-runner
```

------------------------------------------------------------------------

## 10. Five individual pipeline examples

Create a GitLab project and add a `.gitlab-ci.yml` file in its root.
Each job uses the same runner tag: `kube`.

### Example 1: Alpine Linux

``` yaml
stages:
  - test

alpine-job:
  stage: test
  image: alpine:3.21
  tags:
    - kube
  script:
    - echo "Running inside Alpine Linux"
    - cat /etc/os-release
    - apk add --no-cache curl bash
    - curl --version
    - bash --version
    - echo "Alpine pipeline completed"
```

### Example 2: Ubuntu

``` yaml
stages:
  - test

ubuntu-job:
  stage: test
  image: ubuntu:24.04
  tags:
    - kube
  script:
    - echo "Running inside Ubuntu"
    - cat /etc/os-release
    - apt-get update
    - apt-get install -y curl wget git python3
    - curl --version
    - git --version
    - python3 --version
    - echo "Ubuntu pipeline completed"
```

### Example 3: Python

``` yaml
stages:
  - test

python-job:
  stage: test
  image: python:3.12-slim
  tags:
    - kube
  script:
    - echo "Running Python application"
    - python --version
    - pip --version
    - pip install requests
    - python -c "import requests; print(requests.__version__)"
    - python -c "print('Hello from Python Kubernetes Runner')"
```

### Example 4: Node.js

``` yaml
stages:
  - test

node-job:
  stage: test
  image: node:22-alpine
  tags:
    - kube
  script:
    - echo "Running Node.js application"
    - node --version
    - npm --version
    - mkdir node-project
    - cd node-project
    - npm init -y
    - echo "console.log('Hello from Node.js Kubernetes Runner')" > app.js
    - node app.js
    - echo "Node.js pipeline completed"
```

### Example 5: Terraform

``` yaml
stages:
  - validate

terraform-job:
  stage: validate
  image:
    name: hashicorp/terraform:1.9.8
    entrypoint: [""]
  tags:
    - kube
  script:
    - terraform version
    - mkdir terraform-project
    - cd terraform-project
    - |
      cat > main.tf <<'EOF'
      terraform {
        required_version = ">= 1.0"
      }

      resource "null_resource" "example" {}
      EOF
    - terraform fmt -check
    - terraform init -backend=false
    - terraform validate
    - echo "Terraform pipeline completed"
```

Note: This Terraform example validates a small local configuration. It
does not create cloud infrastructure.

------------------------------------------------------------------------

## 11. One pipeline to test all five images

Use this single `.gitlab-ci.yml` to test the five images. Since the jobs
are in the same stage, GitLab can schedule them concurrently, subject to
the runner's concurrency setting and cluster capacity.

``` yaml
stages:
  - test

alpine-test:
  stage: test
  image: alpine:3.21
  tags:
    - kube
  script:
    - echo "ALPINE JOB"
    - cat /etc/os-release
    - apk add --no-cache curl
    - curl --version

ubuntu-test:
  stage: test
  image: ubuntu:24.04
  tags:
    - kube
  script:
    - echo "UBUNTU JOB"
    - cat /etc/os-release
    - apt-get update
    - apt-get install -y curl
    - curl --version

python-test:
  stage: test
  image: python:3.12-slim
  tags:
    - kube
  script:
    - echo "PYTHON JOB"
    - python --version
    - pip --version
    - python -c "print('Python is working')"

node-test:
  stage: test
  image: node:22-alpine
  tags:
    - kube
  script:
    - echo "NODE JOB"
    - node --version
    - npm --version
    - node -e "console.log('Node is working')"

terraform-test:
  stage: test
  image:
    name: hashicorp/terraform:1.9.8
    entrypoint: [""]
  tags:
    - kube
  script:
    - echo "TERRAFORM JOB"
    - terraform version
```

Monitor the job namespace:

``` bash
kubectl get pods -n gitlab-ci-jobs -w
```

A job pod can have more than one container (for example, build and
helper containers). Pod names and container counts are generated by the
Runner and may vary.

------------------------------------------------------------------------

## 12. Private GitLab Container Registry images

Public images such as Alpine and Python normally do not need registry
credentials. Private images do.

For a private GitLab Container Registry image:

1.  Create a GitLab Deploy Token with `read_registry` permission (or use
    an appropriate supported registry credential).
2.  Create a Docker registry Secret in the namespace where the job pods
    run:

``` bash
kubectl create secret docker-registry gitlab-registry-secret \
  --namespace gitlab-ci-jobs \
  --docker-server=registry.gitlab.com \
  --docker-username='YOUR_DEPLOY_TOKEN_USERNAME' \
  --docker-password='YOUR_DEPLOY_TOKEN_VALUE'
```

3.  Add this under `[runners.kubernetes]` in the runner TOML
    configuration:

``` toml
image_pull_secrets = ["gitlab-registry-secret"]
```

4.  Upgrade the Helm release using the updated values file:

``` bash
helm upgrade gitlab-runner \
  gitlab/gitlab-runner \
  --namespace gitlab-runner \
  --values values.yaml
```

5.  Use the private image in `.gitlab-ci.yml`:

``` yaml
private-image-job:
  image: registry.gitlab.com/mygroup/myproject/custom-python:v1
  tags:
    - kube
  script:
    - python --version
```

The registry Secret is separate from the runner authentication Secret.
The runner authentication token connects the runner to GitLab; the
registry credential allows Kubernetes to pull a private image.

------------------------------------------------------------------------

## 13. Troubleshooting log: errors encountered and fixes

This section records the actual errors encountered during the lab, their
causes, and the fixes applied or recommended.

### Error 1: GitLab says legacy runner registration tokens are disabled

**Error:**

``` text
Creating runners with runner registration tokens is disabled.
```

**Cause:**

The legacy runner registration-token workflow is disabled on GitLab.com.
The old registration-token process should not be used.

**Fix:**

1.  Open the GitLab project.
2.  Go to Settings → CI/CD → Runners.
3.  Select Create project runner.
4.  Configure the runner and create it.
5.  Copy the new runner authentication token, normally beginning with
    `glrt-`.
6.  Store it in the Kubernetes Secret as described in section 6.

**Lesson:** A runner authentication token (`glrt-...`) is not the same
as a legacy registration token or a registry token.

------------------------------------------------------------------------

### Error 2: Runner pod is Pending because a Secret key is missing

**Observed pod event:**

``` text
FailedMount:
MountVolume.SetUp failed for volume "projected-secrets":
references non-existent secret key: runner-registration-token
```

**Cause:**

The Secret named `gitlab-runner-token` existed, but it did not contain
the key `runner-registration-token` expected by the installed Helm
chart. The earlier Secret command had only created `runner-token`.

**Fix used:**

Re-create/update the Secret with both keys:

``` bash
read -s -p "Enter GitLab runner authentication token: " RUNNER_TOKEN
echo

kubectl create secret generic gitlab-runner-token \
  --namespace gitlab-runner \
  --from-literal=runner-token="$RUNNER_TOKEN" \
  --from-literal=runner-registration-token="" \
  --dry-run=client -o yaml | kubectl apply -f -

unset RUNNER_TOKEN
```

Then restart the runner Deployment:

``` bash
kubectl rollout restart deployment/gitlab-runner \
  -n gitlab-runner

kubectl rollout status deployment/gitlab-runner \
  -n gitlab-runner
```

**Lesson:** Secret names and Secret key names must match what the chart
expects. Check the installed chart's documentation and rendered
resources when upgrading chart versions.

------------------------------------------------------------------------

### Error 3: Invalid pull policy

**Job log:**

``` text
Preparing the "kubernetes" executor
Using Kubernetes namespace: gitlab-ci-jobs
Using Kubernetes executor with image alpine:3.21 ...

ERROR: Job failed:
invalid pull policy for container "build",
pull_policy ([]) defined in Runner config (default)
is not one of the allowed_pull_policies ([Always IfNotPresent])
```

**Cause:**

The runner had an empty default pull policy (`[]`), while its allowed
pull policies were `Always` and `IfNotPresent`.

**Fix:**

Under `[runners.kubernetes]` in the TOML configuration, explicitly set:

``` toml
pull_policy = ["always"]
allowed_pull_policies = ["always", "if-not-present"]
```

Then upgrade the Helm release:

``` bash
helm upgrade gitlab-runner \
  gitlab/gitlab-runner \
  --namespace gitlab-runner \
  --values values.yaml
```

Restart if needed and verify the configuration:

``` bash
kubectl get configmap gitlab-runner \
  -n gitlab-runner -o yaml
```

**Lesson:**

-   `pull_policy` is the default policy.
-   `allowed_pull_policies` is the list of policies permitted for jobs.

------------------------------------------------------------------------

### Error 4: Runner cannot create Secrets in the job namespace

**Job log:**

``` text
WARNING: won't use informers:
"not allowed: list on pods"

ERROR: Error cleaning up secrets:
resource name may not be empty

ERROR: Job failed (system failure):
prepare environment: setting up credentials:
secrets is forbidden:
User "system:serviceaccount:gitlab-runner:gitlab-runner"
cannot create resource "secrets" in API group ""
in the namespace "gitlab-ci-jobs".
```

**Cause:**

The runner manager used this ServiceAccount:

``` text
system:serviceaccount:gitlab-runner:gitlab-runner
```

But job resources were created in another namespace:

``` text
gitlab-ci-jobs
```

The ServiceAccount did not have the necessary permissions in the job
namespace. The informer warning also indicated it could not list pods.

**Fix:**

Create a Role and RoleBinding in `gitlab-ci-jobs`, binding the
`gitlab-runner` ServiceAccount from `gitlab-runner`. Use the complete
YAML in section 8.

Apply:

``` bash
kubectl apply -f gitlab-runner-rbac.yaml
```

Verify:

``` bash
kubectl auth can-i create pods \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i create secrets \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i list pods \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i create services \
  -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner
```

Expected result: `yes` for each check, assuming the caller is allowed to
impersonate that ServiceAccount.

**Lesson:** When the runner manager and job pods are in different
namespaces, the runner needs appropriate permissions in the job
namespace. A RoleBinding in one namespace does not grant permissions in
another namespace.

The `resource name may not be empty` message appeared during cleanup
after credential setup failed. Treat it as a secondary symptom until the
RBAC issue is fixed; investigate separately if it remains after the job
can create its Secret successfully.

------------------------------------------------------------------------

## 14. Useful operational commands

  ------------------------------------------------------------------------------------------------------------------
  Task                                Command
  ----------------------------------- ------------------------------------------------------------------------------
  List runner pods                    `kubectl get pods -n gitlab-runner -o wide`

  List job pods                       `kubectl get pods -n gitlab-ci-jobs -o wide`

  Watch job pods                      `kubectl get pods -n gitlab-ci-jobs -w`

  Runner logs                         `kubectl logs deployment/gitlab-runner -n gitlab-runner`

  Follow runner logs                  `kubectl logs -f deployment/gitlab-runner -n gitlab-runner`

  Describe a runner pod               `kubectl describe pod POD_NAME -n gitlab-runner`

  Describe a job pod                  `kubectl describe pod POD_NAME -n gitlab-ci-jobs`

  Job namespace events                `kubectl get events -n gitlab-ci-jobs --sort-by=.metadata.creationTimestamp`

  Helm release                        `helm status gitlab-runner -n gitlab-runner`

  Helm values                         `helm get values gitlab-runner -n gitlab-runner`

  Rendered Helm manifest              `helm get manifest gitlab-runner -n gitlab-runner`

  Check Role and binding              `kubectl get role,rolebinding -n gitlab-ci-jobs`

  Check runner ServiceAccount         `kubectl get serviceaccount gitlab-runner -n gitlab-runner`

  Check node resources                `kubectl describe nodes`
  ------------------------------------------------------------------------------------------------------------------

### When a job pod is stuck

``` bash
kubectl get pods -n gitlab-ci-jobs -o wide

kubectl describe pod POD_NAME -n gitlab-ci-jobs

kubectl get events -n gitlab-ci-jobs \
  --sort-by=.metadata.creationTimestamp
```

Look for:

-   `ImagePullBackOff`: image name, registry access, or credentials
    issue.
-   `ErrImagePull`: image pull failed; inspect pod events for the exact
    reason.
-   `Pending`: insufficient CPU/memory, node selector, taint, or
    scheduling issue.
-   `CreateContainerConfigError`: missing Secret/configuration or
    invalid container configuration.
-   `Forbidden`: Kubernetes RBAC permission issue.
-   `FailedMount`: missing Secret, ConfigMap, key, or volume
    configuration.

------------------------------------------------------------------------

## 15. Important security and production notes

This is a learning lab. Before using the same configuration for
production:

1.  Replace `allowed_images = ["*"]` with trusted image patterns or
    registries.
2.  Replace `allowed_services = ["*"]` with only the services required.
3.  Keep `privileged = false` unless a reviewed build requirement needs
    privileged containers.
4.  Do not grant `cluster-admin` to the runner.
5.  Review the Role permissions against the exact Runner version and
    features in use.
6.  Store runner and registry credentials in Kubernetes Secrets; do not
    commit them.
7.  Use a dedicated project/group runner and protect sensitive
    production workloads.
8.  Set resource requests and limits appropriate to the actual cluster.
9.  Consider image digest pinning for reproducible builds.
10. Review cleanup, retention, and namespace isolation before running
    untrusted pipeline code.

**Important:** Allowing arbitrary images and arbitrary CI scripts is
appropriate only for a controlled lab. A user able to modify a pipeline
may execute arbitrary code inside the permissions and network boundaries
available to that job.

------------------------------------------------------------------------

## 16. Next learning milestones

After the five-image pipeline works, continue in this order:

-   [ ] Confirm the runner is online in GitLab.
-   [ ] Run the Alpine job successfully.
-   [ ] Run Ubuntu, Python, Node.js, and Terraform jobs.
-   [ ] Run all five jobs in one pipeline and observe parallel
    scheduling.
-   [ ] Test a private GitLab Container Registry image.
-   [ ] Add an Ansible image and run a playbook syntax check.
-   [ ] Build and push a container image using a suitable builder (for
    example, BuildKit).
-   [ ] Deploy an application to Kubernetes from a pipeline using a
    restricted deployment identity.
-   [ ] Add caching and artifacts.
-   [ ] Add protected environments and deployment approvals.
-   [ ] Review resource limits and runner/job namespace security.

------------------------------------------------------------------------

## 17. Official documentation

Use official documentation to confirm settings when upgrading GitLab
Runner or the Helm chart:

-   GitLab Runner Helm chart:
    https://docs.gitlab.com/runner/install/kubernetes/
-   Kubernetes executor:
    https://docs.gitlab.com/runner/executors/kubernetes/
-   Runner authentication tokens:
    https://docs.gitlab.com/ci/runners/new_creation_workflow/
-   GitLab CI `image` keyword: https://docs.gitlab.com/ci/yaml/#image
-   GitLab Container Registry:
    https://docs.gitlab.com/user/packages/container_registry/
-   Kubernetes RBAC:
    https://kubernetes.io/docs/reference/access-authn-authz/rbac/

------------------------------------------------------------------------

## 18. Quick restart checklist for returning to this lab

If returning after months or a year, start here:

``` bash
# 1. Confirm the cluster and context
kubectl config current-context
kubectl get nodes -o wide

# 2. Check namespaces
kubectl get namespaces

# 3. Check Helm release
helm list -n gitlab-runner
helm status gitlab-runner -n gitlab-runner

# 4. Check runner manager
kubectl get pods -n gitlab-runner
kubectl logs deployment/gitlab-runner -n gitlab-runner

# 5. Check job namespace and RBAC
kubectl get pods -n gitlab-ci-jobs
kubectl get role,rolebinding -n gitlab-ci-jobs

# 6. Check runner permissions
kubectl auth can-i create pods -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

kubectl auth can-i create secrets -n gitlab-ci-jobs \
  --as=system:serviceaccount:gitlab-runner:gitlab-runner

# 7. Check the GitLab project
# Project → Settings → CI/CD → Runners
```

Then run the simple Alpine pipeline from section 10.

### Current progress recorded

The following issues have been observed and addressed in the
troubleshooting process:

-   [x] Legacy registration-token workflow rejected by GitLab.com; use a
    runner authentication token.
-   [x] Runner Secret missing the `runner-registration-token` key;
    update the Secret with both expected keys.
-   [x] Empty default Kubernetes pull policy; configure
    `pull_policy = ["always"]`.
-   [x] Runner ServiceAccount lacked permissions in the separate job
    namespace; add a namespace-scoped Role and RoleBinding.

**Do not assume the entire lab is complete just because the runner
manager pod is Running.** The final success condition is a GitLab
pipeline job completing successfully inside a dynamically created
Kubernetes job pod.
