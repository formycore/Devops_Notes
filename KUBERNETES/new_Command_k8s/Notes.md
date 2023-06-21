# To get all the version of the manifest we need this command 
kubectl api-resources 
kubectl api-resources | grep pod,svc,deployment,cluster....

# to view the commands example just type 
kubeadm

# to remove kubernetes securely
curl -sL https://git.io/scue-k8s-remove.sh | sh
run with root
# for versions in k8s
kubelet-1.24.0 kubeadm-1.24.0 kubectl-1.24.0 --disableexcludes=kubernetes


sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
sudo yum install -y kubelet-1.24.0 kubeadm-1.24.0 kubectl-1.24.0 --disableexcludes=kubernetes
sudo systemctl enable --now kubelet