<<<<<<< HEAD
Step 1: Install OpenJDK 8

Apache Maven requires Java 1.7 or greater. For this reason, you can install OpenJDK 8 as follows.

sudo yum install -y java-1.8.0-openjdk-devel

Step 2: Finally, setup the JAVA_HOME environment variable.

echo JAVA_HOME=$(readlink -f /usr/bin/java | sed s:bin/java::) | sudo tee -a /etc/profile
source /etc/profile

Step 3: Download and configure SonarQube

Download the SonarQube installer files archive.

wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-6.4.zip

You can always look for the link to the latest version of the application on the SonarQube download page.

Install unzip by running:

sudo yum -y install unzip

Unzip the archive using the following command.

sudo unzip sonarqube-6.4.zip -d /opt

Rename the directory:

sudo mv /opt/sonarqube-6.4 /opt/sonarqube

Step 4: Configure Systemd service

SonarQube can be started directly using the startup script provided in the installer package. As a matter of convenience, you should setup a Systemd unit file for SonarQube.

sudo nano /etc/systemd/system/sonar.service

Populate the file with:

[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking

ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop

User=root
Group=root
Restart=always

[Install]
WantedBy=multi-user.target

Start the application by running:

sudo systemctl start sonar

Enable the SonarQube service to automatically start at boot time.

sudo systemctl enable sonar

To check if the service is running, run:

sudo systemctl status sonar

====================================================================================
 Sonarqube script 
====================================================================================

# Step 1: Perform a system update #
sudo yum -y update

# Step 2: Install Java #
sudo yum install -y java-1.8.0-openjdk-devel

# Step 3: To Set JAVA_HOME / PATH for all user, You need to setup global config in /etc/profile OR /etc/bash.bashrc file for all users I am using /etc/profile here #

echo JAVA_HOME=$(readlink -f /usr/bin/java | sed s:bin/java::) | sudo tee -a /etc/profile
source /etc/profile

# Step 4 : To install wget #
sudo yum -y install wget

# Step 5 : Download and configure SonarQube #
wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-6.4.zip

# Step 6 : Install unzip by running #
sudo yum -y install unzip

# Step 7 : Unzip the archive using the following command #
sudo unzip sonarqube-6.4.zip -d /opt

# Step 8 : Rename the directory #
sudo mv /opt/sonarqube-6.4 /opt/sonarqube

# Step 9 : Configure Systemd service #
# SonarQube can be started directly using the startup script provided in the installer package. #
# As a matter of convenience, you should setup a Systemd unit file for SonarQube #
# Populate the file with sudo nano /etc/systemd/system/sonar.service #
# echoing the /etc/systemd/system/sonar.service #

echo [Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking

ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop

User=root
Group=root
Restart=always

[Install]
WantedBy=multi-user.target | sudo tee /etc/systemd/system/sonar.service

# Step 10 : Start the application by running #
sudo systemctl start sonar

#Step 11 : Enable the SonarQube service to automatically start at boot time #
sudo systemctl enable sonar

# Step 12 : To check if the service is running #
=======
Step 1: Install OpenJDK 8

Apache Maven requires Java 1.7 or greater. For this reason, you can install OpenJDK 8 as follows.

sudo yum install -y java-1.8.0-openjdk-devel

Step 2: Finally, setup the JAVA_HOME environment variable.

echo JAVA_HOME=$(readlink -f /usr/bin/java | sed s:bin/java::) | sudo tee -a /etc/profile
source /etc/profile

Step 3: Download and configure SonarQube

Download the SonarQube installer files archive.

wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-6.4.zip

You can always look for the link to the latest version of the application on the SonarQube download page.

Install unzip by running:

sudo yum -y install unzip

Unzip the archive using the following command.

sudo unzip sonarqube-6.4.zip -d /opt

Rename the directory:

sudo mv /opt/sonarqube-6.4 /opt/sonarqube

Step 4: Configure Systemd service

SonarQube can be started directly using the startup script provided in the installer package. As a matter of convenience, you should setup a Systemd unit file for SonarQube.

sudo nano /etc/systemd/system/sonar.service

Populate the file with:

[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking

ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop

User=root
Group=root
Restart=always

[Install]
WantedBy=multi-user.target

Start the application by running:

sudo systemctl start sonar

Enable the SonarQube service to automatically start at boot time.

sudo systemctl enable sonar

To check if the service is running, run:

sudo systemctl status sonar

====================================================================================
 Sonarqube script 
====================================================================================

# Step 1: Perform a system update #
sudo yum -y update

# Step 2: Install Java #
sudo yum install -y java-1.8.0-openjdk-devel

# Step 3: To Set JAVA_HOME / PATH for all user, You need to setup global config in /etc/profile OR /etc/bash.bashrc file for all users I am using /etc/profile here #

echo JAVA_HOME=$(readlink -f /usr/bin/java | sed s:bin/java::) | sudo tee -a /etc/profile
source /etc/profile

# Step 4 : To install wget #
sudo yum -y install wget

# Step 5 : Download and configure SonarQube #
wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-6.4.zip

# Step 6 : Install unzip by running #
sudo yum -y install unzip

# Step 7 : Unzip the archive using the following command #
sudo unzip sonarqube-6.4.zip -d /opt

# Step 8 : Rename the directory #
sudo mv /opt/sonarqube-6.4 /opt/sonarqube

# Step 9 : Configure Systemd service #
# SonarQube can be started directly using the startup script provided in the installer package. #
# As a matter of convenience, you should setup a Systemd unit file for SonarQube #
# Populate the file with sudo nano /etc/systemd/system/sonar.service #
# echoing the /etc/systemd/system/sonar.service #

echo [Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking

ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop

User=root
Group=root
Restart=always

[Install]
WantedBy=multi-user.target | sudo tee /etc/systemd/system/sonar.service

# Step 10 : Start the application by running #
sudo systemctl start sonar

#Step 11 : Enable the SonarQube service to automatically start at boot time #
sudo systemctl enable sonar

# Step 12 : To check if the service is running #
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
sudo systemctl status sonar