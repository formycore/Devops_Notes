- go to 
- https://v1-29.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
- https://v1-29.docs.kubernetes.io/docs/setup/production-environment/container-runtimes/

## install container runtime
- `sudo hostnamectl set-hostname master`
## 1_ Enabling IPV4 packet farwarding (Forwarding IPv4 and letting iptables see bridged traffic)
```
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```
### Verify IPv4 Packet Forwarding
```sysctl net.ipv4.ip_forward```

#### Verify that the br_netfilter, overlay modules are loaded by running the following commands:
```
lsmod | grep br_netfilter
lsmod | grep overlay
```
- verify that net.ipv4.ip_forward is set to 1 with 
```sysctl.net.ipv4.ip_forward```
## 2_ Turnoff swap off
```
sudo swapoff -a
- to check /etc/fstab 
- in aws by default there will be no swap
- 
```
## Install the container runtime
- https://v1-29.docs.kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd
``` getting started with containerd ```
- https://github.com/containerd/containerd/blob/main/docs/getting-started.md

- select option 2 ( select according to operating system)
- Set up Docker's apt repository.
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
- install the containerd packages
```sudo apt-get install containerd.io```
- Configure C - group
- to load the default container configuations 

**_Now we need to start with root_**

```containerd config default > /etc/containerd/config.toml```
- we have to enable systemdCgroup
```
vi /etc/containerd/config.toml
- search for the SystemdCgroup = false - change that to true
```
- restart the containerd
```
sudo systemctl restart containerd
sudo systemctl status containerd
sudo systemctl enable containerd
```
## Steps to check once again
- enabled ipv4 forwarding
- disabled swap
- installed containerd
- configured the container runtime

### Install the kubeadm, kubectl and kubelet
- select the operating system
- https://v1-29.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
# Only on Master
### Intialize the cluster in k8s control plane
- `https://v1-29.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/`
- `kubeadm init --apiserver-advertise-address <private-ip-master> --pod-network-cidr 10.244.0.0/16`
- `kubectl get pods -A`
- `kubectl apply -f https://reweave.azurewebsites.net/k8s/v1.29/net.yaml`
- if we face any issue in container creating
- delete the pod
- `kubectl delete pod <pod-name> -n kube-system`
- 
