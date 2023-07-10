FROM tomcat:8-jre11
# Remove all the contents inside the below dir
RUN rm -rf /usr/local/tomcat/webapps/*
COPY target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD [ "catalina.sh", "run" ]
WORKDIR /usr/local/tomcat/
VOLUME //usr/local/tomcat/webapps