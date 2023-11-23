# 2048 game deploy to kubernetes
```
sudo apt update -y
#sudo apt upgrade -y
wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | tee /etc/apt/keyrings/adoptium.asc
echo "deb [signed-by=/etc/apt/keyrings/adoptium.asc] https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | tee /etc/apt/sources.list.d/adoptium.list
sudo apt update -y
sudo apt install temurin-17-jdk -y
/usr/bin/java --version
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
                  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
                  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
                              /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update -y
sudo apt-get install jenkins -y
sudo systemctl start jenkins
sudo systemctl status jenkins

# install docker
sudo apt-get install docker.io -y
sudo systemctl start docker
sudo systemctl status docker
sudo systemtl enable docker
sudo usermod -aG docker jenkins
sudo usermod -aG docker ubuntu


# Install trivy
sudo apt-get install wget apt-transport-https gnupg lsb-release -y
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy -y

# Sonarqube
- try with sonarqube cloud
- login with github
- create project manually
- first create a organization
- then create a project
- give display name and project key
- public
- next
- previous version
- create project

# Install some plugins in jenkins
- Eclipse Temurin installer
- SonarQube Scanner
- NodeJS


# Manage Jenkins configure system
 - JDK installations
    - Add JDK
    - Name: jdk17
    - Install automatically
    - Install from adoptium
    - version: jdk-17.0.8.1+1
- NodeJS installations
    - Add NodeJS
    - Name: node16
    - Install automatically
    - Install from nodejs.org
    - version: 16.2.0

# on the sonarcloud
- go to project
- configure analysis
- configure manually
- Administration / Analysis MethodAnalyze a project with other CI
- copy the token

# jenkins
- create a credential with copied token
- Name: sonar-token

- configure sonarqube
    - SonarQube Scanner installations
    - Name: sonar-server
    - Install automatically
    - version : SonarQube Scanner 5.0.1.3006
    - save


```