# Install docker and jenkins
sudo apt-get update
sudo apt-get install openjdk-11-jdk -y
java -version

curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins -y

sudo systemctl start jenkins.service
sudo systemctl enable jenkins.service
sudo systemctl status jenkins.service
cat /var/lib/jenkins/secrets/initialAdminPassword
------------------------------------------------------------
# Install docker
sudo apt-get update
sudo apt install docker.io -y
sudo usermod -aG docker jenkins
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl start jenkins
sudo systemctl enable jenkins
------------------------------------------------------------
# install aws cli
sudo apt-get update
sudo apt-get install awscli -y

aws configure   
------------------------------------------------------------
# Create IAM user with administrator access
## this is useful for eks 