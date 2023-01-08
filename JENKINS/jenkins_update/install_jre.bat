# Add user to Administrators group
net localgroup Administrators %username% /add
# verify the user is in Administrators group
net localgroup Administrators
# install oracle java 8 on windows
# 1. download java 8    
curl -o "C:\Program Files\Java\jdk-8u201-windows-x64.exe" https://download.oracle.com/otn/java/jdk/8u201-b09/1961070e4c9b4e26a04e7f5a083f551e/jdk-8u201-windows-x64.exe
# 2. install java 8 
"C:\Program Files\Java\jdk-8u201-windows-x64.exe" /s
# 3. set java 8 as default
setx /M JAVA_HOME "C:\Program Files\Java\jdk1.8.0_201"
# 4. set java 8 in path
setx /M PATH "%PATH%;C:\Program Files\Java\jdk1.8.0_201\bin"
# 5. verify java 8
java -version
# 6. install jenkins with windows batch
# 6.1. download jenkins.war
#https://get.jenkins.io/war-stable/2.277.3/jenkins.war
curl -o "C:\Program Files (x86)\Jenkins\jenkins.war" https://get.jenkins.io/war-stable/2.277.3/jenkins.war
# start jenkins with java8 jar
java -jar "C:\Program Files (x86)\Jenkins\jenkins.war" --httpPort=8080
# 6.2. start jenkins
net start jenkins
# 7. verify jenkins
curl http://localhost:8080
# 8. open jenkins in browser
start http://localhost:8080
