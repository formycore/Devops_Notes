# Multi-Node Kubernetes Cluster Setup Using Kubeadm
This readme provides step-by-step instructions for setting up a multi-node Kubernetes cluster using Kubeadm.

## Overview
This guide provides detailed instructions for setting up a multi-node Kubernetes cluster using Kubeadm. The guide includes instructions for installing and configuring containerd and Kubernetes, disabling swap, initializing the cluster, installing Flannel, and joining nodes to the cluster.

## Prerequisites
Before starting the installation process, ensure that the following prerequisites are met:

- You have at least two Ubuntu 18.04 or higher servers available for creating the cluster.
- Each server has at least 2GB of RAM and 2 CPU cores.
- The servers have network connectivity to each other.
- You have root access to each server.

## Installation Steps
The following are the step-by-step instructions for setting up a multi-node Kubernetes cluster using Kubeadm:

Update the system's package list and install necessary dependencies using the following commands:

```
sudo apt-get update
sudo apt install apt-transport-https curl -y
```

## Install containerd
To install Containerd, use the following commands:

```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install containerd.io -y
```

## Create containerd configuration
Next, create the containerd configuration file using the following commands:

```
sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml
```

## Edit /etc/containerd/config.toml
Edit the containerd configuration file to set SystemdCgroup to true. Use the following command to open the file:

```
sudo vim /etc/containerd/config.toml
```

Set SystemdCgroup to true:
```
SystemdCgroup = true
```

Restart containerd:
```
sudo systemctl restart containerd
```

## Install Kubernetes
To install Kubernetes, use the following commands:

- These instructions are for Kubernetes 1.27.

Update the apt package index and install packages needed to use the Kubernetes apt repository:

```
sudo apt-get update
# apt-transport-https may be a dummy package; if so, you can skip that package
sudo apt-get install -y apt-transport-https ca-certificates curl
```
- Download the public signing key for the Kubernetes package repositories. The same signing key is used for all repositories so you can disregard the version in the URL:
```
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.27/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```
- Add the appropriate Kubernetes apt repository. Please note that this repository have packages only for Kubernetes 1.27; for other Kubernetes minor versions, you need to change the Kubernetes minor version in the URL to match your desired minor version (you should also check that you are reading the documentation for the version of Kubernetes that you plan to install).
```
# This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.27/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```
## Disable swap
Disable swap using the following command:

```
sudo swapoff -a
```

Enable kernel modules
```
sudo modprobe br_netfilter
```

Add some settings to sysctl
```
sudo sysctl -w net.ipv4.ip_forward=1
```
## Initialize the Cluster (Run only on master)
Use the following command to initialize the cluster:
```
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

Create a .kube directory in your home directory:
```
mkdir -p $HOME/.kube
```

Copy the Kubernetes configuration file to your home directory:
```
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
```

Change ownership of the file:
```
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

## Install Flannel (Run only on master)
Use the following command to install Flannel:
```
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/v0.20.2/Documentation/kube-flannel.yml
```

## Verify Installation
Verify that all the pods are up and running:

```
kubectl get pods --all-namespaces
```

## Join Nodes
To add nodes to the cluster, run the kubeadm join command with the appropriate arguments on each node. The command will output a token that can be used to join the node to the cluster.

## Get the information about the nodes

```
kubectl get nodes
```

## Verify the above Kubernetes Cluster Setup by deploying nginx 
```
kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml

```

## Check the status of nginx pod

```
kubectl get pods -o wide
```
