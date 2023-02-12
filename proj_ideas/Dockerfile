FROM tomcat:8.0-alpine

LABEL maintainer=”deepak@softwareyoga.com”

ADD SampleWebApp.war /usr/local/tomcat/webapps/

EXPOSE 8080

CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]