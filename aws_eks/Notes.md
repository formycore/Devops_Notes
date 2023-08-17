## aws eks
```
eksctl create cluster \
--name sam-eks-test \
--region ap-south-1 \
--nodegroup-name my-nodes \
--node-type t3.small \
--managed --nodes 2 -- profile ps


```

# installation of eks and kubectl
```
------------------------------------------------------------
# Install eksctl
```curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version```
------------------------------------------------------------
# Install kubectl
```
sudo curl --silent --location -o /usr/local/bin/kubectl \
  https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/kubectl
sudo chmod +x /usr/local/bin/kubectl
```
------------------------------------------------------------
```

# Amazon EKS cluster IAM role

## Creating the Amazon EKS cluster role
```
AWS CLI to create the cluster role.
1) Copy the following contents to a file named cluster-trust-policy.json.
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

2) Create the role. You can replace eksClusterRole with any name that you choose.
aws iam create-role \
  --role-name eksClusterRole \
  --assume-role-policy-document file://"cluster-trust-policy.json"

3) Attach the required IAM policy to the role.
aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy \
  --role-name eksClusterRole
```





