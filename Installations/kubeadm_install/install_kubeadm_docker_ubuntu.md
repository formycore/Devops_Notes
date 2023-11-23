# change the hostname in aws
```
sudo hostnamectl set-hostname master
```
# Installation of kubeadm and docker on Ubuntu 22.04 along with docker
### On Master and Node
```
# 1. download the script
curl -fsSL https://get.docker.com -o install-docker.sh
# check the cri version support
# 2. Install make
sudo apt-get install make

```
### Install go
```
# RUN THIS AS ROOT
wget https://storage.googleapis.com/golang/getgo/installer_linux
chmod +x installer_linux
./installer_linux
source ~/.bash_profile

```

#### Install cri-dockerd from the mirantis github repo see the readme for more info
```
# RUN THIS AS ROOT
git clone https://github.com/Mirantis/cri-dockerd.git
cd cri-dockerd
mkdir bin
go build -o bin/cri-dockerd
mkdir -p /usr/local/bin
install -o root -g root -m 0755 bin/cri-dockerd /usr/local/bin/cri-dockerd
install packaging/systemd/* /etc/systemd/system
sed -i -e 's,/usr/bin/cri-dockerd,/usr/local/bin/cri-dockerd,' /etc/systemd/system/cri-docker.service
systemctl daemon-reload
systemctl enable cri-docker.service
systemctl enable --now cri-docker.socket
```
##### Intall kubeadm,kubelet,kubectl
```
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
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
```
