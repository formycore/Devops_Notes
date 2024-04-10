# Container registry in GITLAB
```
- first create a project in gitlab
- in the setting we have access tokens
- select the scope as owner and select read and write registry
- copy the token and store it in a safe place
- in the gitlab project go to the CI/CD and create a new variable
- name the variable as token and paste the token in the value and as masked variable

       # in the setting we have an option for the access 
        # here we need to give the docker with owner role
        # add the USERNAME and DOCKER_TOKEN in the CI/CD variable
-------------------------------------------------------------------------------------------------
stages:
    - deploy_stage
deploy:
    stage: deploy_stage
    script:
        # in the setting we have an option for the access 
        # here we need to give the docker with owner role
        # add the USERNAME and DOCKER_TOKEN in the CI/CD variable
        - docker login -u $USERNAME -p $DOCKER_TOKEN registry.gitlab.com
        - docker build -t registry.gitlab.com/gcpchary31/container_registry/test:v4 .
        - docker push registry.gitlab.com/gcpchary31/container_registry/test:v4
        - docker stop app && docker rm app
        - docker run -d -p 5000:5000 --name app registry.gitlab.com/gcpchary31/container_registry/test:v4
    tags:
        - gcp  
-------------------------------------------------------------------------------------------------
