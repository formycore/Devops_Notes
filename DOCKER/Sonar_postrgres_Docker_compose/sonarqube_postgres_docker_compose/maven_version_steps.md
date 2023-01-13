# Install java 
sudo yum install java-11-openjdk-devel -y
sudo wget https://dlcdn.apache.org/maven/maven-3/3.8.7/binaries/apache-maven-3.8.7-bin.tar.gz
tar -xvzf apache-maven-3.8.7-bin.tar.gz -C /usr/local
cd /usr/local
sudo mv apache-maven-3.8.7/ maven
sudo tee -a /etc/profile.d/maven.sh <<EOF
# Apache Maven Environment Variables
# MAVEN_HOME for Maven 1 - M2_HOME for Maven 2
export M2_HOME=/usr/local/maven
export PATH=${M2_HOME}/bin:${PATH}
EOF

chmod +x maven.sh
source /etc/profile.d/maven.sh
mvn -version
