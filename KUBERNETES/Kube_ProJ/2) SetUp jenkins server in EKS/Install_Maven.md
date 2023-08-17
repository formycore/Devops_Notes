```
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
```
