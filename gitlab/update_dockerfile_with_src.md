# Gitlab cicd with the update the docker image with the change in the src code 
## taken this as the sample repo 
### [https://github.com/ravdy/hello-world](https://github.com/ravdy/hello-world)

```stages:
  - build
  - build-img

build_war:
  image: maven:3.8.7-eclipse-temurin-8-alpine
  stage: build
  script:
    - mvn clean install
  artifacts:
    paths:
      - webapp/target/*.war

build_img:
  image: docker:latest
  stage: build-img
  services:
    - docker:dind
  dependencies:
    - build_war # Fetch artifacts from the `build_war` job
  script:
    - cp webapp/target/*.war .
    - echo $CI_REGISTRY_PASSWORD | docker login $CI_REGISTRY -u $CI_REGISTRY_USER --password-stdin
    - docker build -t $CI_REGISTRY/hello-world:$CI_PIPELINE_ID .
    - docker push $CI_REGISTRY/hello-world:$CI_PIPELINE_ID
    - echo "hello"
```


# Dockerfile

```
# Use the official Tomcat base image
FROM tomcat:9.0-jdk8-openjdk



# Copy the WAR file from the build context to Tomcat's webapps directory
COPY *.war /usr/local/tomcat/webapps
```