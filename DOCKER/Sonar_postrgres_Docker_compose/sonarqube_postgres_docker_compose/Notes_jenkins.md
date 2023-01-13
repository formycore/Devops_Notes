# Now create jenkins compose file
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

# Now run the compose file
  - docker-compose up -d
  