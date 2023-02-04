# pull the jenkins latest image
FROM jenkins/jenkins:lts
# Build the container
USER root
# install update and wget
RUN apt-get update && \
    apt-get install -y wget && \
    wget -O /tmp/apache-maven-3.6.3.tar.gz https://downloads.apache.org/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz && \
   tar xzf /tmp/apache-maven-3.6.3.tar.gz -C /opt/ && \
   ln -s /opt/apache-maven-3.6.3 /opt/maven && \
   ln -s /opt/maven/bin/mvn /usr/local/bin && \
   rm -f /tmp/apache/maven-3.6.3.tar.gz
ENV MAVEN_HOME /opt/maven
RUN chown -R jenkins:jenkins /opt/maven && \
     apt-get clean
USER jenkins