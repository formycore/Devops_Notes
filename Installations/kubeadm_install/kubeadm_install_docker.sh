#!/bin/bash
# Install docker
curl -fsSL https://get.docker.com -o install-docker.sh
sh install-docker.sh
sudo usermod -aG docker $USER
newgrp docker
sudo su -
wget https://storage.googleapis.com/golang/getgo/installer_linux
chmod +x installer_linux
./installer_linux
source ~/.bash_profile
exit
