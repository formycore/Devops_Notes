# MASTER & NODES

1) sudo yum update -y
2) update the /etc/hosts file with the IP and hostname of the master and nodes
```
10.138.0.3 master
10.138.0.4 node
10.138.0.5 node1 
```
3) Check for the swap entry in /etc/fstab and comment it out
4) sudo swapoff -a
5) sudo yum install -y yum-utils device-mapper-persistent-data lvm2
6) sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
7) sudo yum install containerd.io -y
8) sudo systemctl start containerd
9) sudo systemctl enable containerd
10) install kubeadm kubelet kubectl
```
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF
```
## 11) Set SELinux in permissive mode (effectively disabling it)
```
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
```
12) sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
13) sudo systemctl enable --now kubelet
#### here we will get some errors for that we need to run this command first
Solution
```
sudo rm /etc/containerd/config.toml
sudo systemctl restart containerd
echo '1' > /proc/sys/net/ipv4/ip_forward
modprobe bridge
modprobe br_netfilter
```

# ONLY ON MASTER
1) kubeadm init
#### If you have lost the kubeadm join command with the token id then you can generate a new one using
kubeadm token create --print-join-command
#### if you are root user then execute this 
export KUBECONFIG=/etc/kubernetes/admin.conf
if as normal users then use the list of commands which are provided by the example
a) mkdir -p $HOME/.kube
b) sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
c) sudo chown $(id -u):$(id -g) $HOME/.kube/config

2) kubectl get nodes
3) kubectl get pods -n kube-system