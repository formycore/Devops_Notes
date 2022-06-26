- just for testing purpose only
- testing env
- if any new feature from kubernetes,we can test it in the minikube
- how to configure minikube cluster setup
- we need to check whether the hardware supports virtualization supports or not 
- should be virtualization enabled
- it should have any one of the vm
- or with out vm also we can use minikube
- just with docker

## curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
## sudo install minikube-linux-amd64 /usr/local/bin/minikube


to start minikube with docker:
  - **minkube start** -- when with vm
  - **minikube start --driver=docker** - when with docker no vm
  - **minikube config set driver docker** as To make docker the default driver:
  - we can use linux and mac but not windows kernals without vm's

--
**install kubectl**

cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

## from the kubernetes site the repo_gpgcheck=1
## so we can skip the repo_gpgcheck=0
***sudo yum install -y kubectl***
-- minikube start --driver=docker
-- kubectl get cs
-- kubectl get nodes
-- kubectl get nodes -o wide
