# Install gitlab runnner
# https://docs.gitlab.com/runner/install/
# https://docs.gitlab.com/runner/install/linux-manually.html
```
sudo yum update -y
sudo yum install git
sudo yum install docker.io -y
sudo usermod -aG docker $USER
groups ec2-user
sudo systemctl start docker
sudo systemctl enable docker
newgrp docker
docker run hello-world

curl -LJO "https://gitlab-runner-downloads.s3.amazonaws.com/latest/rpm/gitlab-runner_amd64.rpm"
sudo rpm -i gitlab-runner_amd64.rpm

sudo gitlab-runner register

copy the command from the gitlab server
next proceed with the questions

```