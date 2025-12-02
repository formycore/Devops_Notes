# GitLab Kubernetes Agent Setup Guide

## Table of Contents
1. [Initial Setup](#initial-setup)
2. [Agent Installation & Registration](#agent-installation--registration)
3. [Deployment Configuration](#deployment-configuration)
4. [Authorization](#authorization)

---

## Initial Setup

### Step 1: Agent Infrastructure
- Create Repository A on GitLab (connection repo)
- Create an agent on GitLab
- Install GitLab agent on your Kubernetes cluster
- Register the connection between K8s and GitLab

### Step 2: Project Deployment
- Create Repository B on GitLab (data/project repo)
- Create Kubernetes manifest files for your project
- Push project data to Repository B
- Build container image and push to GitLab Container Registry

### CI/CD Pipeline Overview
1. Build container image with source code
2. Push image to container registry
3. Pull image from registry to Kubernetes nodes
4. Deploy application to cluster

> **Note:** We create two repositories:
> - `k8s-connection`: Empty project for agent configuration (firewall rules)
> - `kubernetes-data`: Project data and Kubernetes manifests

**Reference:** [GitLab Kubernetes Agent Documentation](https://docs.gitlab.com/user/clusters/agent/)

---

## Agent Installation & Registration

### Creating Agent Configuration File

1. **Navigate to the `k8s-connection` repository**
2. **Create configuration file path:** `.gitlab/agents/k8s-connection/config.yaml`

The configuration file acts as a firewall where you define:
- Which groups can access the cluster
- Which usernames are authorized
- Which repositories have access
- General cluster access policies

> **Reference:** [Agent Configuration File Setup](https://docs.gitlab.com/user/clusters/agent/install/#create-an-agent-configuration-file)

### Registering the Agent with GitLab

**Option 1: GitLab UI Registration** (Recommended)

1. In GitLab, navigate to your project (should be `k8s-connection`)
2. Go to **Operate** → **Kubernetes clusters**
3. Click **Connect a cluster (agent)**
4. Enter a unique name for your agent: `k8s-connection`
5. Click **Register agent**
6. Copy all Helm commands provided

### Installing Agent on Kubernetes Cluster

**Using Helm Installation Process:**

1. Copy the Helm commands from GitLab UI
2. Paste and execute them in your Kubernetes cluster terminal:
   ```bash
   # The commands will look similar to:
   helm repo add gitlab https://charts.gitlab.io
   helm repo update
   helm install gitlab-agent gitlab/gitlab-agent \
     --namespace gitlab-agent-system --create-namespace \
     --set gitlabUrl=https://gitlab.com \
     --set agentToken=<YOUR_AGENT_TOKEN>
   ```

### Verifying Agent Connection

After installation, verify the connection is established:

1. Go to your `k8s-connection` repository in GitLab
2. Navigate to **Operate** → **Kubernetes clusters**
3. Confirm the connection status shows as "connected"

> **✓ Connection established successfully!**

---

## Deployment Configuration

### Test in the kubernetes cluster

#### Step 1: Create GitLab Registry Secret

**Generate secret for private registry access:**

```bash
kubectl create secret docker-registry gitlab-registry-secret \
  --docker-server=registry.gitlab.com \
  --docker-username=<your-gitlab-username> \
  --docker-password=<your-gitlab-personal-access-token> \
  --dry-run=client -o yaml > gitlab-registry-secret.yaml
```

Then apply the secret:
```bash
kubectl apply -f gitlab-registry-secret.yaml
```

#### Step 2: Create Pod Manifest

**Generate pod deployment file:**

```bash
kubectl run php-image \
  --image=registry.gitlab.com/<your-gitlab-username>/<your-repo-name>:<tag> \
  --port=80 \
  --dry-run=client -o yaml > pod.yaml
```

**Edit `pod.yaml` to include the image pull secret:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: php-image
  name: php-image
spec:
  containers:
  - image: registry.gitlab.com/kubernetes1472149/kubernetes-connect/php:v6
    name: php-image
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
  # This secret allows pulling from private registry
  imagePullSecrets:
    - name: gitlab-registry-secret
status: {}
```

#### Step 3: Create Service Manifest

**Generate service file:**

```bash
kubectl create service nodeport phpservice \
  --tcp=80:80 \
  --dry-run=client -o yaml > service.yaml
```

**Edit `service.yaml` - Update selector to match pod label:**

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: phpservice
  name: phpservice
spec:
  ports:
  - name: phpports
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    # ⚠️ IMPORTANT: This must match the pod label defined above
    run: php-image
  type: NodePort
status:
  loadBalancer: {}
```

#### Step 4: Apply All Manifests

```bash
kubectl apply -f gitlab-registry-secret.yaml
kubectl apply -f pod.yaml
kubectl apply -f service.yaml
```

---

## CI/CD Workflow

### Update `.gitlab-ci.yml` for kubectl Commands

**Reference:** [GitLab CI/CD Workflow Documentation](https://docs.gitlab.com/user/clusters/agent/ci_cd_workflow/)

**Example deployment job:**

```yaml
variables:
  KUBE_CONTEXT: kubernetes1472149/k8s_connect:k8s-agent

stages:
  - build
  - deploy
build_image:
  image: docker
  stage: build
  services:
    - docker:dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY/kubernetes1472149/kubernetes-connect/php:v6 .
    - docker push $CI_REGISTRY/kubernetes1472149/kubernetes-connect/php:v6
deploy:
  stage: deploy
  image:
    name: bitnami/kubectl:latest
    entrypoint: ['']
  script:
    - kubectl config use-context $KUBE_CONTEXT
    - kubectl get pods
    - kubectl get nodes -o wide
    - kubectl apply -f secret.yaml
    - kubectl apply -f pod.yaml
    - kubectl apply -f service.yaml


```

**Context format explanation:**
- `kubernetes1472149/k8s_connect` = `<group_name>/<repo_name>`
- `k8s-connection` = agent name (from registration)

---

## Authorization

### Authorize Project Repository to Access Agent

**Reference:** [GitLab Agent Authorization](https://docs.gitlab.com/user/clusters/agent/ci_cd_workflow/#authorize-your-projects-to-access-the-agent)

1. **Update agent configuration file**
   - Location: `.gitlab/agents/k8s-connection/config.yaml` (in `k8s-connection` repo)
   
2. **Add CI/CD access rules:**

```yaml
# .gitlab/agents/k8s-connection/config.yaml
ci_access:
  projects:
    # Authorize the k8s-data repository to deploy via CI/CD
    - id: kubernetes1472149/k8s_data
```

> **Format:** `id: <group-path>/<project-path>`

This configuration allows the `k8s-data` repository's CI/CD pipeline to authenticate with the agent and deploy to your Kubernetes cluster.

---

## Quick Reference

### Useful kubectl Commands

```bash
# View configured contexts
kubectl config get-contexts

# Switch to agent context
kubectl config use-context <context-name>

# Verify connectivity
kubectl get pods
kubectl get nodes -o wide
kubectl get services
```

### Key File Locations

| File | Location | Purpose |
|------|----------|---------|
| Agent Config | `.gitlab/agents/k8s-connection/config.yaml` | Access control & firewall rules |
| Secret | `gitlab-registry-secret.yaml` | Registry authentication |
| Pod | `pod.yaml` | Application deployment |
| Service | `service.yaml` | Network exposure |
| CI/CD | `.gitlab-ci.yml` | Pipeline configuration |

---

## Troubleshooting

- **Connection not established?** Verify Helm installation completed successfully
- **Image pull errors?** Ensure secret is created and referenced in pod spec
- **Authorization denied?** Check CI access rules in agent config file
- **Kubectl context not found?** Re-run Helm setup commands and verify context name


- 