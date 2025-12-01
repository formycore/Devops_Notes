```
stages:
  - deploy
deploy:
  stage: deploy
  image: docker:24.0.5-cli
  variables:
    #DOCKER_HOST: unix:///var/run/docker.sock
    DOCKER_TLS_CERTDIR: ""
  tags:
    - devops
  script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login $CI_REGISTRY -u $CI_REGISTRY_USER --password-stdin
    - docker compose version
    - docker compose up 
    
```
- if we have a dockerfile in the repository, we can build the image using the following command
```
    - docker build -t $CI_REGISTRY_IMAGE:latest .
    - docker push $CI_REGISTRY_IMAGE:latest
```
