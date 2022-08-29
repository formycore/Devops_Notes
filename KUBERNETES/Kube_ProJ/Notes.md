# install jenkins with ansible
sudo yum install java-1.8.0-openjdk-devel -y
** we get the java home path from the below command **
sudo /usr/sbin/alternatives --config java
            or
readlink -f /usr/bin/java | sed "s:/bin/java::"
sudo su -
vi ~/.bash_profile
JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.342.b07-1.el7_9.x86_64
export JAVA_HOME
PATH=$PATH:$HOME/bin:$JAVA_HOME


curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo

# install Maven
sudo yum install java-1.8.0-openjdk-devel -y
sudo wget https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz -P /opt
tar -xvf /opt/apache-maven-3.8.6-bin.tar.gz -C /opt
sudo ln -s /opt/apache-maven-3.8.6 /opt/maven
### under root
vi ~/.bash_profile
M2_HOME=/opt/apache-maven-3.8.6
M2=$M2_HOME/bin
export M2_HOME
export M2
PATH=$PATH:$HOME/bin:$JAVA_HOME:$M2_HOME:$M2

# Assign Shell to the Jenkins user
vi /etc/passwd
* search for the jenkins user and change the shell to /bin/bash *

# install Docker inside the Jenkins server
sudo yum install docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
chmod 777 /var/run/docker.sock

# Add jenkins user to into sudoers file
vi /etc/sudoers
jenkins ALL=(ALL) NOPASSWD: ALL

# install Maven integration and Docker pipeline plugins
 **Under jenkins plugin**
Manage Jenkins -> Manage Plugins -> Available -> search for maven integration and docker pipeline -> install without restart
