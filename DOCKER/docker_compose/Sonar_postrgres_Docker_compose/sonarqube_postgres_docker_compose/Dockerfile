# Base image
FROM jenkins/jenkins:lts
# Build the container
USER root
# Install wget
RUN apt-get update \
    && apt-get install -y wget git
# Get maven 3.8.7
RUN wget -O /tmp/apache-maven-3.8.7 https://downloads.apache.org/maven/maven-3/3.8.7/binaries/apache-maven-3.8.7-bin.tar.gz
# Install Maven
RUN tar -zxvf /tmp/apache-maven-3.8.7 -C /opt/ \
    && ln -s /opt/apache-maven-3.8.7 /opt/maven \
    && ln -s /opt/maven/bin/mvn /usr/local/bin \
    && rm -rf /tmp/apache-maven-3.8.7
ENV MAVEN_HOME /opt/maven
RUN chown -R jenkins:jenkins /opt/maven
# Remove caches
RUN apt-get clean

USER jenkins
