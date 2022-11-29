# Followed https://docs.google.com/document/d/1_SlIpFvrLbHFe2XL6-OEFDKbbp2p0nFKW1hFSDHOFDw/edit
# YouTube Link https://www.youtube.com/watch?v=nbp9zxkmi74&t=2261s

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
sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
sudo systemctl enable --now kubelet
```
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
```kubeadm init```

        here we get the join command for the nodes
        copy that to the nodes 
#### If you have lost the kubeadm join command with the token id then you can generate a new one using
```kubeadm token create --print-join-command```
#### if you are root user then execute this 
   export KUBECONFIG=/etc/kubernetes/admin.conf
#### if you are normal user then execute this
```
             1a) mkdir -p $HOME/.kube 

             1b) sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

             1c) sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
```kubectl get nodes
kubectl get pods -n kube-system
```
4) we can see that the pods are in pending state because we have not installed the network plugin yet

# install calico CNI
```
curl https://docs.projectcalico.org/manifests/calico.yaml -O

kubectl apply -f calico.yaml

kubectl get pods -n kube-system
```