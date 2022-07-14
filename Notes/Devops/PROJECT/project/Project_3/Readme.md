<<<<<<< HEAD
# Simple devops project 3
1) code commit to git hub
2) build and test with jenkins
3) then deploy using docker
- we need 
- git 
- jenkins
- docker

echo "dockeradmin ALL=(ALL) NOPASSWD:ALL " >> /etc/sudoers

=======
# Simple devops project 3
1) code commit to git hub
2) build and test with jenkins
3) then deploy using docker
- we need 
- git 
- jenkins
- docker

echo "dockeradmin ALL=(ALL) NOPASSWD:ALL " >> /etc/sudoers

>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
sudo docker stop valaxy_demo;sudo docker rm -f valaxy_demo;sudo docker image rm -f valaxy_demo;sudo cd /opt/docker;sudo docker build -t valaxy_demo .