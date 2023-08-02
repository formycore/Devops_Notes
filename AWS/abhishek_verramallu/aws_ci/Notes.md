```
- developer commits the code to aws codecommit then with aws codebuild it will build the code and store the artifacts in s3 or artifacts those might be in zip or war or any thing and then with aws code deploy it will deploy the code to the aws ec2 instance or ecs or lambda 

- to work with the same cicd use code pipeline

```



# Aws cicd
```
- aws codecommit - as git repo
- aws codebuild - for CI the artifacts are stored in s3 or artifacts
- aws code deploy 
- aws codepipeline

```
# KMS
```
- to store the secrets
- to encrypt the secrets
- to decrypt the secrets

```
# Storage
```
- artifacts
- s3

```
## aws codecommit
```
- within aws by aws to get CICD
- aws codecommit is a git repo
- aws codecommit does not work well with root account
- create a new user "codecommit"
-  in iam with aws codecommit poweruser
- login with aws codecommit user under us-east-1
- Create repository
- Name: codecommittest
- Description: codecommit test
- click on create
- click on clone url with https
- now we will get 403 error
    - go the user which is created for this purpose and click on security credentials
    - click on HTTPS Git credentials for AWS CodeCommit
    - click on generate credentials
    - copy the username and password
- now we can clone the repo
- paste the username and password from the https credentials
- cd codecommit
- copy the https://github.com/iam-veeramalla/aws-devops-zero-to-hero.git
- cd codecommit
- git clone https://github.com/iam-veeramalla/aws-devops-zero-to-hero.git
- cd aws-devops-zero-to-hero
- cd day-14
- cp -r . ~/awsdemo/aws_cicd/codecommit/
- cd ~/awsdemo/aws_cicd/codecommit/
- cd sample-python-app
- mv * ../
- rm -rf sample-python-app
- git add .
- git commit -m "initial commit"
- git push origin master
- now we can see the code in the codecommit

```
# aws code pipeline
```
- add codebuild for the user codecommit
- create a new codebuild project
- Create build project
- project name: sample-python-project
- description: sample-python-project
-Source
    - source provider: AWS CodeCommit
    - repository: codecommittest
    - branch: master
- Environment
    - Environment image: Managed image
    - Operating system: Ubuntu
    - Runtime: Standard
    - Image: aws/codebuild/standard:7.0 --- always use the latest
    - Environment type: Linux
- Service role:
    - create a new service role
    - Use cases for other AWS services:
        - AWS CodeBuild
    - role name: codebuild-role
    - click on create role
- what is service role ?
    -  with IAM we will create a iam-user or iam-roles and assign the permissions to the user or role
    - iam user  is login to the account 
    - awscodebuild is service
    - to perform actions on awscodebuild we need to create a role and assign the permissions to the role
    - it is a service that performs an action 
- create a new role
- this is role does not have any permissions
- to grant some permission to this role using aws system manager
- to awscodebuild permission we need to use aws system manager
- Buildspec
    - build specifications: Insert build commands
    - inside the buildspec file we will write the commands
    - start from phases
##############################################################
version: 0.2

env:
  parameter-store: # provide the docker build login in a secret location
     # key: "value"
     # key: "value"

phases:
  install:
    runtime-versions: # here the code is in python 
      python: 3.11
    # as there is no commands to run at the run time   
  pre_build: # install flask on the image
    commands:
      - pip install -r requirements.txt
  build:
    commands:
      - echo "Building the docker image"
      - docker build -t <> # here we user aws system manager
  post_build:
    commands:
      - echo "Build Successfull"
#####################################################################
- click on create build project




```