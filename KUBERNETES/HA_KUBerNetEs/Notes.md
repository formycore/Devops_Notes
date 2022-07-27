# haproxy for kubernetes
3 machines master
2 nodes
1 load balancer
---------------
load balancer
	- sudo - su
	- sudo yum update
	- yum install haproxy -y
    - **sudo semanage port -a -t http_cache_port_t 6443 -p tcp** # 6443 is the default haproxy port
    - without the above semanage command, the port will not be available for use
    - sudo systemctl enable haproxy.service
	- vi /etc/haproxy/haproxy.cfg #vi /etc/haproxy/haproxy.cfg from the site
********************************************************************************
frontend fe-apiserver
   bind 0.0.0.0:6443
   mode tcp
   option tcplog
   default_backend be-apiserver

backend be-apiserver
    mode tcp
    option tcplog
    option tcp-check
    balance roundrobin
    default-server inter 10s downinter 5s rise 2 fall 2 slowstart 60s maxconn 250 maxqueue 256 weight 100
        server master1 <master_kube_private_ip>:6443 check
        server master2 <master_kube_private_ip>:6443 check
        server master3 <master_kube_private_ip>:6443 check
********************************************************************************
systemctl restart haproxy
systemctl enable haproxy
systemctl status haproxy

* to check whether the load balancer is working or not
  - nc -v localhost 6443
********************************************************************************
# on BOTH the Master & Nodes
- Install kubeadm,kubelet,docker
    - Install docker
        - sudo yum install -y yum-utils
        - sudo yum-config-manager \
           --add-repo \
           https://download.docker.com/linux/centos/docker-ce.repo
        - sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    $ docker without sudo
        sudo groupadd docker
        sudo usermod -aG docker $USER
        sudo systemctl start docker
        sudo systemctl enable docker
        newgrp docker
- Disable swap
    - sudo swapoff -a
    - sudo sed -i 's/^\(.*swap.*\)$/#\1/' /etc/fstab
- Disable SElinux
    - sudo sed -i 's/^\(.*SELINUX.*\)$/#\1/' /etc/sysconfig/selinux
    - sudo setenforce 0
- Install kubeadm,kubelet
********************************************************************************
# setting up kubernetes
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=0
# if we keep this as zero it will install fastly and avoid some errors
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF

sudo yum install -y kubelet-1.23.6 kubeadm-1.23.6 kubectl-1.23.6 --disableexcludes=kubernetes
sudo systemctl enable --now kubelet
********************************************************************************
									ON MASTER


# Intialization 

sudo su -

cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system

sed -ie "s/cgroupDriver: systemd/cgroupDriver: cgroupfs/g" /var/lib/kubelet/config.yaml

vi /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}

sudo systemctl daemon-reload
sudo systemctl restart docker

- kubeadm init --control-plane-endpoint <load_balancer_private_ip:6443> --upload-certs
==================================================================
								ON NODE

sudo su -
vi /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}

sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl restart kubelet
systemctl enable kubelet.service
kubeadm join <here>
check for the kubectl get nodes on the master


        


