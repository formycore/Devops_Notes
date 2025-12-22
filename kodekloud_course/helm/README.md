- helm install <app:version>
- helm upgrade <app> <app:version>
- helm rollback <app> <revision>
- helm uninstall <app>
- helm repo add <repo_name> <repo_url>
- helm repo update
- helm search repo <app>
- helm list

-------------------------
Installation Instructions
- helm installed on the local machine which is having access to the kubernetes cluster. with right login details.
setup kubeconfig file to work with the cluster.
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
1. Prerequisites (Validate First)

Before proceeding, ensure the following are available on your local machine:

Linux / macOS / Windows (WSL preferred for Windows)

Access credentials for the Kubernetes cluster

Cloud IAM user / service account OR

kubeconfig provided by cluster admin

Network access to the cluster API server (VPN, bastion, etc.)

Verify basic tools:

which kubectl
which helm


If missing, install them in the next steps.

2. Install kubectl
Linux (x86_64)
curl -LO https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

Verify
kubectl version --client

3. Install Helm (Client-Side Only)
Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

Verify
helm version


Expected output:

version.BuildInfo{Version:"v3.x.x", ...}


Note: Helm v3 does not require Tiller.

4. Create kubeconfig Directory (If Not Exists)
mkdir -p ~/.kube
chmod 700 ~/.kube

5. Set Up kubeconfig (Three Common Scenarios)
Scenario A: kubeconfig Provided by Admin

Copy the file to your system:

cp config ~/.kube/config


Secure permissions:

chmod 600 ~/.kube/config

Scenario B: Cloud-Managed Cluster (Example: AWS EKS)
aws eks update-kubeconfig \
  --region ap-south-1 \
  --name <cluster-name>


This automatically:

Fetches cluster endpoint & CA

Updates ~/.kube/config

Uses IAM authentication

Scenario C: Manual kubeconfig Creation

Use this when you have:

API server URL

CA certificate

Client certificate/key OR token

Example structure:

apiVersion: v1
kind: Config
clusters:
- name: my-cluster
  cluster:
    server: https://<API-SERVER>:6443
    certificate-authority-data: <BASE64_CA>

users:
- name: my-user
  user:
    token: <TOKEN>

contexts:
- name: my-context
  context:
    cluster: my-cluster
    user: my-user

current-context: my-context


Save as:

~/.kube/config

6. Export KUBECONFIG (If Using Custom Path)

If kubeconfig is not at the default location:

export KUBECONFIG=/path/to/config


Persist it:

echo 'export KUBECONFIG=/path/to/config' >> ~/.bashrc

7. Validate kubectl Access
Check context
kubectl config get-contexts
kubectl config current-context

Test cluster connectivity
kubectl get nodes


Expected:

NAME          STATUS   ROLES
worker-node   Ready    <none>


If this works, kubeconfig is correctlyCACCT setup correctly.

8. Validate RBAC Permissions (Important for Helm)

Helm requires permissions to create:

Secrets

ConfigMaps

Deployments

Services

Check access:

kubectl auth can-i create deployment
kubectl auth can-i create secret


If denied, request proper Role / ClusterRole binding.

9. Helm Uses kubeconfig Automatically

Helm does not need separate authentication.
It uses the same kubeconfig as kubectl.

Verify Helm can access cluster:

helm list -A


If successful:

No releases found

10. Test Helm End-to-End (Smoke Test)
Add a public repo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

Install a test chart
helm install nginx-test bitnami/nginx

Verify
kubectl get pods
helm status nginx-test

Cleanup
helm uninstall nginx-test
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
- how to do this refer https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/

