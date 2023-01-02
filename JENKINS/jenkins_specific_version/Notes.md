https://directdevops.blog/2019/01/04/installing-specific-lts-version-of-jenkins-on-ubuntu/

# Installing Specific LTS Version of Jenkins on Ubuntu
```
sudo apt-get update 
sudo apt-cache search openjdk
sudo apt-get install openjdk-8-jdk
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt-get update
sudo apt-cache madison jenkins
sudo apt-get install jenkins=2.138.3 -y
```

[click here](https://directdevops.blog/2019/01/04/installing-specific-lts-version-of-jenkins-on-ubuntu/)
how to install specific version jenkis LTS