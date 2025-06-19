# install the gitlab runner
sudo curl -L --output /usr/local/bin/gitlab-runner "https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/latest/binaries/gitlab-runner-linux-amd64"
sudo chmod +x /usr/local/bin/gitlab-runner
# install the gitlab runner service
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
# start the gitlab runner service
sudo gitlab-runner start
# register the gitlab runner
- we get this from the gitlab instance
- gitlab-runner register
# we need to provide the following information
- gitlab instance url
- gitlab token
- gitlab runner description
- gitlab runner tags freecodecamp
- gitlab runner executor (docker, shell, etc.)docker
- then it will ask for the docker image to use, we can use the default one or specify a custom one docker:27.1.2 (as per 19 June 2025)
# we can check the status of the gitlab runner
gitlab-runner status
--------------------------------------------------
# example gitlab code 
# https://gitlab.com/gitlab-course-public/freecodecamp-gitlab-ci
- fork this repository
- it wont have .gitlab-ci.yml file, so we need to create one
- we can use the following code in the .gitlab-ci.yml file
```yaml
stages:
    - build
    - test
build website:
    image: node:16-alpine
    stage: build
    tags:
        - freecodecamp
    script:
        - yarn install
        - yarn build
    artifacts:
        paths:
            - build
test website:
    image: alpine
    stage: test
    tags:
        - freecodecamp    
    script:
        - test -f build/index.html
unit tests:
    stage: test
    tags:
        - freecodecamp    
    image: node:16-alpine
    script:
        - yarn install
        - yarn test
```
