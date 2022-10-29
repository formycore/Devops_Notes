# INSTALL JENKINS
## Step 1: Install OpenJDK 8 package
* sudo yum install java-1.8.0-openjdk-devel -y
**we get the java home path from the below command**
* sudo /usr/sbin/alternatives --config java
            or
* readlink -f /usr/bin/java | sed "s:/bin/java::"
* sudo su -
---------------------------------------------------------------------------------------------------------
```
vi ~/.bash_profile
JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.342.b07-1.el7_9.x86_64
export JAVA_HOME
PATH=$PATH:$HOME/bin:$JAVA_HOME
```
---------------------------------------------------------------------------------------------------------
* echo $JAVA_HOME
## Step 2: Install Jenkins repository
```
curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
```
## Step 3: Install Jenkins
```sudo yum install jenkins -y```
## Step 4: Start Jenkins service
```
sudo systemctl start jenkins
sudo systemctl status jenkins
sudo systemctl status jenkins
```



