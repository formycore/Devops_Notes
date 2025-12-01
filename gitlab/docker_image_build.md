- if installed gitlab runner with docker executor, we can use the following code to build docker images
- we need to change the values in config.toml 
```
concurrent = 1
check_interval = 0

[[runners]]
  name = "my-docker-runner"
  url = "https://gitlab.com/"
  token = "YOUR_TOKEN"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.cache]

  [runners.docker]
    tls_verify = false
    image = "docker:24.0.5-cli"
    privileged = true
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = [
      "/var/run/docker.sock:/var/run/docker.sock",
      "/cache"
    ]
    shm_size = 0


```
--------------------------------------------------------------
```
- sudo gitlab-runner verify
- sudo systemctl restart gitlab-runner
- sudo systemctl status gitlab-runner
--------------------------------------------------------------

```
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
--------------------------------------------------------------
# if we dont have any gitlab runner with docker executor, we can use the following code to build docker images
```
image: docker:latest
services:
  - docker:dind
variables:
  DOCKER_HOST: tcp://docker:2376
  DOCKER_TLS_CERTDIR: "/certs"
  DOCKER_DRIVER: overlay2
stages:
  - build
build_and_push:
  stage: build
  script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker build -t "$CI_REGISTRY_IMAGE:latest" .
    - docker push "$CI_REGISTRY_IMAGE:latest"

    # check inside the container registry
    (- docker build -t $CI_REGISTRY/kubernetes1472149/kubernetes-connect:v1 .
    - docker push $CI_REGISTRY/kubernetes1472149/kubernetes-connect:v1)

```
--------------------------------------------------------------