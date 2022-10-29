Master and nodes
- **sudo yum update -y**
- # install the docker
    - **curl -fsSL https://get.docker.com/ | sh**
    - **sudo usermod -aG docker $(whoami)**
    - **sudo systemctl start docker**
    - **sudo systemctl enable docker**
    - **sudo systemctl status docker**
# installing the kubernetes

cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF

# actually the repo_gpgcheck is 1 there are some errors in the repo, so we need to set it to 0 repo_gpgcheck=0

# Set SELinux in permissive mode (effectively disabling it)
**sudo setenforce 0**
**sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config**

**sudo yum install -y kubelet-1.23.6 kubeadm-1.23.6 kubectl-1.23.6 --disableexcludes=kubernetes**

**sudo systemctl enable --now kubelet**
-------------------------------------------
Master only
- sudo su -
- kubeadm init --apiserver-advertise-address=<private-ip> --pod-network-cidr=<cidr>



# letting ip tables to see bridged traffic
cat << EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat << EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sudo sysctl --system

sed -i "s/cgroupDriver: systemd/cgroupDriver: cgroupfs/g" /var/lib/kubelet/config.yaml
systemctl deamon reload
systemctl restart kubelet

vi /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}

sudo systemctl daemon-reload
sudo systemctl restart docker


kubeadm init

kubeadm reset

kubeadm init --apiserver-advertise-address=10.182.0.3 --pod-network-cidr=10.0.0.0/16


 mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:



------------------
- kubectl get nodes (it will be in the notready status)
- kubectl get pods --all-namespaces
- kube-systems coredns will be in the pending status
# ----------------
we need calico to install on Master
- curl https://docs.projectcalico.org/manifests/calico.yaml -O
- kubectl apply -f calico.yaml

-------------------------------------------------
ON WORKER NODE
-vi /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}

sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl restart kubelet
systemctl enable kubelet.service

