```
for this project we need a user, with root it can be dangerous

Installations


- new user
- awscli
- kubectl
- eksctl
- jenkins
- docker
- docker-compose



IAM
Users
Add user
user name: shack
check for : Provide user access to the AWS Management Console - optional
check for : I want to create an IAM user
Attach policies directly
    AmazonEC2FullAccess
    AmazonEKS_CNI_Policy
    AmazonEKSClusterPolicy
    AmazonEKSWorkerNodePolicy
    AWSCloudFormationFullAccess
    IAMFullAccess

create user
-----------------------------
- go to user list
- click on shack
- click on security credentials
- under permissions 
- click on inline policies

    - click on create policy
    - select the visual editor
    - service: EKS
    - actions: All actions
    - resources: All resources
    - create policy
    - name: eksfullaccess
- it will added to the user
-----------------------------------------
- create a ec2 instance
- ubuntu
- t2.xlarge
- 30GB
-------------
sudo apt get update

# install awscli
sudo apt install awscli


# Install kubectl
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.18.8/2020-09-18/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
kubectl version --short --client

# Install eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version

# Create EKS cluster

eksctl create cluster --name=my-eksa \
                      --region=us-east-1 \
                      --zones=us-east-1a,us-east-1b \
                      --without-nodegroup

# Install jenkins

# Install docker

# Install SonarQube
docker run -d -p 9000:9000 -v /path/to/your/host/directory:/opt/sonarqube/data sonarqube:lts-community

# OIDC provider

eksctl utils associate-iam-oidc-provider \
    --region us-east-1 \
    --cluster my-eksa \
    --approve

eksctl create nodegroup --cluster-my-eksa \
                        --region-us-east-1 \
                        --name=node2 \
                        --node-type=t3.medium \
                        --nodes=3\
                        --nodes-min=2 \
                        --nodes-max=3 \
                        --node-volume-size=20 \
                        --ssh-access \
                        --ssh-public-key=Key \
                        --managed \
                        --asg-access \
                        --external-dns-access \
                        --full-ecr-access \
                        --appmesh-access \
                        --alb-ingress-access


```




```