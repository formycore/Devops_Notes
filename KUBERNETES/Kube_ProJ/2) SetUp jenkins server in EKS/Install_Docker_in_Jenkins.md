## INSTALL DOCKER INSIDE THE JENKINS SERVER
sudo yum install docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
chmod 777 /var/run/docker.sock

# ADD JENKINS USER TO INTO SUDOERS FILE
vi /etc/sudoers
jenkins ALL=(ALL) NOPASSWD: ALL

## ASSIGN SHELL TO THE JENKINS USER
vi /etc/passwd
* search for the jenkins user and change the shell to /bin/bash *

### INSTALL MAVEN INTEGRATION AND DOCKER PIPELINE PLUGINS
 **Under jenkins plugin**
Manage Jenkins -> Manage Plugins -> Available -> search for maven integration and docker pipeline -> install without restart
