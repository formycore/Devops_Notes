# Install the kubeadm in centos
-------------------------------------

# change the hostname in aws
```
sudo hostnamectl set-hostname master
```

# Installation of kubeadm on centos along with docker
### On Master and Node
```

sudo yum install wget git -y
# 1. download the script
curl -fsSL https://get.docker.com -o install-docker.sh
chmod +x install-docker.sh
./install-docker.sh
sudo usermod -aG docker $USER
sudo systemctl start docker
sudo systemctl enable --now docker

```

#### Install cri-dockerd from the mirantis github repo see the readme for more info
```
wget https://github.com/Mirantis/cri-dockerd/releases/download/v0.3.7/cri-dockerd-0.3.7.20231027185657.170103f2-0.el7.x86_64.rpm
yum install <.rpm_file>
systemctl start cri-docker
systemctl enable cri-docker

```

##### Intall kubeadm,kubelet,kubectl
```

# Set SELinux in permissive mode (effectively disabling it)
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
# This overwrites any existing configuration in /etc/yum.repos.d/kubernetes.repo
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.27/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.27/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF
sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
sudo systemctl enable --now kubelet
```

# On Master only
```

kubeadm init --help
check for the --pod-network-cidr and --cri-socket
kubeadm init --pod-network-cidr "10.244.0.0/16" --cri-socket "unix:///var/run/cri-dockerd.sock"

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config


kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml

```

# On Node only
```
After getting the join command from the master run the following command
kubeadm join xx.xx.xx.xx:6443 --token xxxxxxxxxxxxxxxx \
    --cri-socket "unix:///var/run/cri-dockerd.sock" \
    --discovery-token-ca-cert-hash sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
