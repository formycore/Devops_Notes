# Connecting a Kubernetes cluster with GitLab
##### get the code from https://github.com/formycore/gitlab-kube-inte-sample-repo
## 1)  Install An Agent In Your Cluster
```
- as per the document we need to have any cloud Kubernetes clusters
- we can continue with the self hosted clusters also
- install the agent first
```
### 2) Install the agent manually
```
- Create an agent configuration file
- create a new file in the repository
- .gitlab/agents/<agent-name>/config.yaml
- create a empty file with above name
- You can leave the file blank for now, and configure it later
- we fill this file later with 
	- which grp
	- which username
	- which repository

```
### 3) Register the agent with GitLab
```
- we need to install the agent before registering to the cluster
- under gitlab project 
	- operate
	- Kubernetes cluster
	- we can see the see the agent name ( .gitlab/agents/<agent-name>/config.yaml see above )
	- click on Register
	- we get set helm commands (helm needs to be installed on the master node)
	- copy the generated code and paste it in the master node 
	- in the gitlab page refresh it 
	- connection state is active (green)
	- Connecting b/w gitlab repo and Kubernetes cluster is up 
	
```
### 4) Authorize the agent to access your projects

```
- under the config file (.gitlab/agents/<agent-name>/config.yaml) 
- ci_access:
  projects:
    - id: path/to/project
- ci_access:
  projects:
    - id: awssandeepchary1/gitlab-kube-inte-sample-repo
- we are given the access to the agent to this repo 


```
### CICD
```
- google search for the gitlab container Register CICD
- we get the sample code 
- edit the code 
- we need to provide the values for these in the gitlab --> setting --> CICD --> variables
- CI_REGISTRY:
- CI_REGISTRY_PASSWORD
- CI_REGISTRY_USER
```
```

stages:
  - build
  - build-img
mvn_build:
    image: maven:3.9.9-eclipse-temurin-23-alpine
    stage: build
    script:
        - mvn clean install -Dmaven.test.skip=true
    artifacts:
      paths:
        - "target/*.jar"
build-push-img:
    image: docker:stable
    stage: build-img
    needs:
      - mvn_build
    services:
      - name: docker:dind
    script:
        #- docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
        - echo $CI_REGISTRY_PASSWORD | docker login $CI_REGISTRY -u $CI_REGISTRY_USER --password-stdin
        - docker build -t $CI_REGISTRY/pet-clinic:$CI_PIPELINE_ID .
        - docker push $CI_REGISTRY/pet-clinic:$CI_PIPELINE_ID

```

### On The Master Node
```
- create a pod with the above image 
- $kubectl run login-app --image=registry.gitlab.com/awssandeepchary1/gitlab-kube-inte-sample-repo/demo:v1 --dry-run=client -o yaml >> login-app.yml


```
## Now the full cicd gitlab file
```
variables:
  KUBE_CONTEXT: awssandeepchary1/k8s-connect:kuber-connect
stages:
  - build
  - deploy
build_image:
  stage: build
  image: docker:stable
  services:
    - name: docker:dind
  script:
    - docker login -u $CI_REGISTRY_USER  -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY/demo:v1 .
    - docker push $CI_REGISTRY/demo:v1
deploy_project:
  stage: deploy
  image: 
    name: bitnami/kubectl:latest
    entrypoint: ['']
  script:
    # - kubectl config use-context path/to/agent/project:agent-name
	# path we were given the empty file for (<agent-name>/config.yaml)
	# given under variables KUBE_CONTEXT: awssandeepchary1/k8s-connect:<agent-name>(kuber-connection)
    - kubectl config use-context $KUBE_CONTEXT
	- kubectl apply -f <secret> <deploy> <svc>  
    - kubectl get pods
    - kubectl get nodes -o wide


```
