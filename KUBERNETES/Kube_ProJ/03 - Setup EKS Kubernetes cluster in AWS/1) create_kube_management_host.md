# Kubernetes Management Host
* for this we need only t2.micro instance
* in the management host we need to install kubectl, awscli
Install and setup kubectl on Management host 
    a. Download kubectl version 1.19.6 
    b. Grant execution permissions to kubectl executable
    c. Move kubectl onto /usr/local/bin
    d. Test that your kubectl installation was successful
```
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl
chmod +x ./kubectl
mv ./kubectl /usr/local/bin 
kubectl version --short --client
```
2) Install and setup eksctl on Management Host
    a. Download and extract the latest release
    b. Move the extracted binary to /usr/local/bin
    c. Test that your eksclt installation was successful
```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```
3) Create an IAM Role and attache it to EC2 instance Management Host
    `Note: create IAM user with programmatic access if your bootstrap system is outside of AWS`
    IAM user should have access to
    * IAM full access
    * EC2 full access
    * VPC full access
    * CloudFormation full access
* attach the role to kubernetes managed hosts
