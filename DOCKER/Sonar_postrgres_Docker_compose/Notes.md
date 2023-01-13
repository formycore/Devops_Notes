# Install jenkins with docker compose
```
version: "3.3"
services:
  jenkins:
    image: jenkins/jenkins:lts
    privileged: true
    user: root
    ports:
      - 8080:8080
      - 50000:50000
    container_name: jenkins
    volumes:
      - /opt/jenkins_configuration:/var/jenkins_home
```
- Now run docker-compose up -d
- under the container <docker exec -it <container_id> /bin/bash>
- install maven and git
- for some maven builds are need some specific version
## Downloading the maven version
    - wget https://dlcdn.apache.org/maven/maven-3/3.8.7/binaries/apache-maven-3.8.7-bin.tar.gz
    - tar -xvf apache-maven-3.8.7-bin.tar.gz
    - mv apache-maven-3.8.7 /usr/local/maven
    - rm -rf apache-maven-3.8.7-bin.tar.gz
    - mv apache-maven-3.8.7 maven
## Configure Apache Maven Environment
    - cd /etc/profile.d/
    - vi maven.sh
    # Apache Maven Environment Variables
    # MAVEN_HOME for Maven 1 - M2_HOME for Maven 2
    export M2_HOME=/usr/local/maven
    export PATH=${M2_HOME}/bin:${PATH}
    - source maven.sh
    - mvn -version
# Now install sonarqube with docker compose
```
version: "3.3"
services:
  db:
    image: postgres:12-alpine
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=sonar
      - POSTGRES_DB=sonar
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - sonarqube-net
  sonarqube:
    image: sonarqube:community
    depends_on:
      - db
    environment:
      - sonar.jdbc.username=sonar
      - sonar.jdbc.password=sonar 
      - sonar.jdbc.url=jdbc:postgresql://db/sonar
    ports:
      - 9000:9000
    volumes:
      - sonar_conf:/opt/sonarqube/conf
      - sonar_data:/opt/sonarqube/data
      - sonar_extensions:/opt/sonarqube/extensions
      - sonar_plugins:/opt/sonarqube/lib/bundled-plugins
    networks:
      - sonarqube-net
networks:
  sonarqube-net:
volumes:
  sonar_conf:
  sonar_data:
  sonar_extensions:
  sonar_plugins:
  postgres_data:
```
# Now run docker-compose up -d
#####################################################################
# Now create jenkins slave 
- Now go to the jenkins container
    ```docker exec -it <container_id> /bin/bash ```
- Check the java version
    ```java -version```
- Now the host/agent server install the openjdk 11 on centos
    ```sudo yum -y install java-11-openjdk java-11-openjdk-devel```
- Now check the java version on the host/agent machine
    ```java -version```
- Now click on new node <manage jenkins -- manage nodes>
    - Give some name to the node
    - Permanent Agent
    - Description
    - Number of executors <A good value to start with would be the number of CPU cores on the machine>
    - Remote root directory <create a diretory on the agent server>
    - Labels <FROM THIS LABEL WE CALL THE JENKINS JOB>
    - Usage <use this node as much as possible/only build job with label defined in the job>
    - Launch method <Launch agent connecting to the control>
    - save
- Now go to the node,there we get the agent.jar 
- copy that agent.jar to host/agent server
- or else curl -sO http://xx.xx.xx.xx:8080/jnlpJars/agent.jar
- java -jar agent.jar -jnlpUrl http://xx.xx.xx.xx:8080/manage/computer/docker/jenkins-agent.jnlp -secret xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxcxx -workDir "/jenkins" &nohup
- Now the agen is connected
###################################################################################################
# Now create a job
```
// git 'https://github.com/ravdy/hello-world.git'
// if maven not found
// go to the maven server and check mvn -v, it will show the path of the maven installed,copy the path
// under the agent any 
// environment {
//     PATH = "${PATH}:/usr/local/maven/bin:$PATH"
//     PATH = "${PATH}:/usr/local/src/apache-maven/bin:$PATH"
//}
pipeline {
    agent {label 'docker'}
    environment {
        PATH = "${PATH}:/usr/local/maven/bin:$PATH"
    }
    stages {
        stage("git"){
            steps{
                git 'https://github.com/ravdy/hello-world.git'
            }
        }
        stage("Maven"){
            steps{
                sh 'mvn clean install'
            }
        }
        
    }
}
```
