# Minimum requirements for minikube
# https://minikube.sigs.k8s.io/docs/start/
# Install kubectl on Linux
# https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
# Download the latest release with the command:
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
# Make the kubectl binary executable.
chmod +x ./kubectl
# Move the binary in to your PATH.
sudo mv ./kubectl /usr/local/bin/kubectl
# Test to ensure the version you installed is up-to-date:
kubectl version --client

# Install MiniKube on Linux
# https://kubernetes.io/docs/tasks/tools/install-minikube/
# Download the latest release with the command:
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
# Make the minikube binary executable.
chmod +x minikube
# Move the binary in to your PATH.
sudo mv minikube /usr/local/bin/
# Test to ensure the version you installed is up-to-date:
minikube version

# Install Docker on Linux
# https://docs.docker.com/engine/install/ubuntu/
# Uninstall old versions
sudo apt-get remove docker docker-engine docker.io containerd runc
# Update the apt package index and install packages to allow apt to use a repository over HTTPS:
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
# Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Use the following command to set up the stable repository.
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
# Verify that Docker Engine is installed correctly by running the hello-world image.
sudo docker run hello-world

