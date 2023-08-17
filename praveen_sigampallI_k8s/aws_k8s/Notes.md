# K8 EKS SETUP ON AWS CLOUD
```Select EC2 LINUX 2 AMI and create T2.MEDIUM INSTANCE IN US-WEST-1```

# create a user in IAM
username : demouser
next
next
create user
select the user/security credentials/create access key/cli/next/done

create the password for the user
enable console access/enable/custom password/apply
copy the account id

login with iam user 

# Install all tools Prerequisites
```
yum install git -y
sudo yum install java-11-openjdk-devel -y

wget https://downloads.apache.org/maven/maven-3/3.8.8/binaries/apache-maven-3.8.8-bin.tar.gz
sudo tar xf apache-maven-3.8.8-bin.tar.gz -C /opt
cd /opt
sudo mv apache-maven-3.8.8/ apache-maven
sudo vi /etc/profile.d/maven.sh
# echo -e 'export M2_HOME=/opt/apache-maven'"\n"'export MAVEN_HOME=/opt/apache-maven' | sudo tee -a /etc/profile.d/maven.sh
    export M2_HOME=/opt/apache-maven

    export MAVEN_HOME=/opt/apache-maven

    export PATH=${M2_HOME}/bin:${PATH}
sudo chmod +x /etc/profile.d/maven.sh
source /etc/profile.d/maven.sh
mvn --version
# mvn --version -- check the path 
sudo ln -s /opt/apache-maven/bin/mvn mvn

# Install Docker
yum install docker -y
usermod -aG docker jenkins # [ Add jenkins user to dockergroup ]
systemctl start docker
systemctl enable docker

# - Install Python
yum install python3 -y

# Install Ansible
amazon-linux-extras install ansible2 -y
```
# ATTACH THE IAM ROLE and attach the role to the instance
```
Go to IAM -> CLICK CREATE NEW IAM ROLE ->
SELECT EC2 -> CLICK ON ADMINISTRATOR ACCESS
-> CREATE ROLE

Go toEC2 instance you have created -> Click on
ACTIONS -> SECURITY -> MODIFY IAM ROLE ->
ATTACH YOUR NEW ROLE
```
# – INSTALL SETUP FOR EKS
```
# Install kubectl
curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin
cp ./kubectl $HOME/bin/kubectl
export PATH=$HOME/bin:$PATH
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
source $HOME/.bashrc
kubectl version --short –client

# Install eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/bin
eksctl version


- MASTER Cluster creation [ Change the master cluster
name eksdemo as per your wish and select region as
us-west-1]

eksctl create cluster --name=eksdemo3 \
--region=us-west-1 \
--zones=us-west-1b,us-west-1a \
--without-nodegroup

- Add Iam-Oidc-Providers
eksctl utils associate-iam-oidc-provider \
--region us-west-1 \
--cluster eksdemo \
--approve


- WORKER NODE Create node-group [ Change the PEM key ssh-public-key to your key]

eksctl create nodegroup --cluster=eksdemo \
--region=us-west-1 \
--name=eksdemo-ng-public \
--node-type=t2.medium \
--nodes=2 \
--nodes-min=2 \
--nodes-max=4 \
--node-volume-size=10 \
--ssh-access \
--ssh-public-key=key-test \
--managed \
--asg-access \
--external-dns-access \
--full-ecr-access \
--appmesh-access \
--alb-ingress-access


```
# DELETE NODE AND THEN THE CLUSTER
```
DELETE NODE
eksctl delete nodegroup --cluster=eksdemo
--region=us-west-1 --name=eksdemo-ng-public
DELETE CLUSTER
eksctl delete cluster --name=eksdemo --region=us-west-1
```