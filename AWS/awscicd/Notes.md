Tools used for awscicd 
```    - Auth
        - IAM
        - KMS
    - Artifact
        - Artifact
        - S3 
```

```    - CICD
        - CodeCommit - (just like github)
        - CodeBuild - (Continous Integration)
        - then it will go to Artifact or S3
        - with CodeDeploy we will deploy in aws instance or ecs
        - to use all these in pipeline then we go for CodePipeline
```
**1) CodeCommit**
2) Repository
   Repository name: awscicd
   Description: awscicd
   (Enable code guru review)(same as sonarqube)
3) Create repository
```

Under **IAM**
```1) Go to IAM
   2) Create user
    3) User name: awscicd
    4) Access type: Programmatic access
    5) Attach existing policies directly
    6) Select: awscodecommitpoweruser (later we will know why this is needed)
    7) Create
```
Under **IAM --> Users**
```1) Select awscicd
    2) Security credentials (https git credentials for aws code commit)
    3) here we get the user and password
    4) Download .csv file
    5) Copy Access key ID and Secret access key
```
-- Clone the repository
```1) Go to CodeCommit
    2) Select awscicd
    3) Clone URL
    4) Copy the URL
    5) Go to terminal
    6) git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/awscicd
    7) here we need to add the user and password which we got from the .csv file (here we need to assign the awscodecommitpoweruser policy)
    7) cd awscicd
    8) touch index.html (add the html code)
    9) git add .
    10) git commit -m "first commit"
    11) git push origin master
```
-- now checking with dev branch 
```1) git checkout -b dev
   2) edit the index file as some changes
   3) git add .
   4) git commit -m "second commit"
   5) git push origin dev
```
-- now merging 
-- go to the repo
```1) Go to CodeCommit
    2) Select awscicd
    3) Select Branches
    4) create pull request
    5) Source branch: dev
    6) Destination branch: master
    7) Create pull request
    8) Merge pull request
    9) Confirm merge (fast forward)

```
