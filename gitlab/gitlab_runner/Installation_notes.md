# Install gitlab runnner
# https://docs.gitlab.com/runner/install/
# https://docs.gitlab.com/runner/install/linux-manually.html

## Other way to register the runner
```
- Goto the gitlab server
- settings -> CI/CD -> Runners
- at the new runner there will be three dots click on it
- select the runner installation and registration instructions
- after following those instructions we might get an error

ERROR: Job failed: prepare environment: exit status 1. Check https://docs.gitlab.com/runner/shells/index.html#shell-profile-loading for more information

- sudo rm /home/gitlab-runner/.bash_logout
- sudo gitlab-runner register

```


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
