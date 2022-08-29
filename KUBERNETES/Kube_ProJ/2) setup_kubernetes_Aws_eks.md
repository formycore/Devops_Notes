# (4) Create EKS cluster and nodes from EC2 Management Host
## install aws-cli
python3 -m pip install aws-cli
* aws configure

## Installing aws-iam-authenticator
```
curl -o aws-iam-authenticator https://s3.us-west-2.amazonaws.com/amazon-eks/1.21.2/2021-07-05/bin/linux/amd64/aws-iam-authenticator
chmod +x ./aws-iam-authenticator
mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator && export PATH=$PATH:$HOME/bin
echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
aws-iam-authenticator help
```


```
eksctl create cluster --name cluster-name  \
--region region-name \
--node-type instance-type \
--nodes-min 2 \
--nodes-max 2 \ 
--zones <AZ-1>,<AZ-2>

example:
eksctl create cluster --name samantha-cluster \
   --region ap-south-1 \
--node-type t2.medium \
```
* for our app we need min 2 cpu's so choose t2.medium
* we can also delete the cluster 
```
eksctl delete cluster --name samantha-cluster --region ap-south-1
```
**now create a new cluster with different name and with zones**
* eksctl create cluster \
--name deepika-cluster \
--region ap-south-1 \
--node-type t2.medium \
--zones ap-south-1a,ap-south-1b

