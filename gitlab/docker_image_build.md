```
stages:
  - build
build:
  image: docker:24.0.5-cli
  stage: build
  variables:
    #DOCKER_HOST: unix:///var/run/docker.sock
    DOCKER_TLS_CERTDIR: ""
  script:
    - echo $DOCKER_HOST
    - ls -la /var/run
    - docker version  
    - echo $CI_REGISTRY
    - echo "$CI_REGISTRY_PASSWORD" | docker login $CI_REGISTRY -u $CI_REGISTRY_USER --password-stdin
    - docker build -t $CI_REGISTRY/oluwaseun_alausa_course/two-tier-flask-app_1 .
    - docker push $CI_REGISTRY/oluwaseun_alausa_course/two-tier-flask-app_1
```
- when we have Dockerfile in the repository, GitLab CI/CD will use it to build the Docker image.