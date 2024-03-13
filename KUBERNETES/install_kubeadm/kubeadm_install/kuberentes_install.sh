#!/bin/bash
# First turn off swap
sudo swapoff -a
# Install docker/containerd
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install containerd.io -y
sudo systemctl start containerd
sudo systemctl enable containerd
# Install kubeadm kubelet kubectl
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF
# Set SELinux in permissive mode (effectively disabling it)
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
# Installing kubelet, kubeadm, and kubectl
sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
sudo systemctl enable --now kubelet
# we will get some errors for that we need to run this command first
# run these commands as root

sudo rm /etc/containerd/config.toml
sudo systemctl restart containerd
echo '1' > /proc/sys/net/ipv4/ip_forward
modprobe bridge
modprobe br_netfilter

