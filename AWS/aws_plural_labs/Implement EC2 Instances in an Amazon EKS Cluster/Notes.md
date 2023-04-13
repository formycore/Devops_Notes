# Create an EKS Managed Node Group
In the first challenge, you created the Control Plane for your Kubernetes cluster. To create the Data Plane, you will need to add EC2 instances to the cluster. A Managed Node Group creates these instances and lets EKS manage the Data Plane for you.

Click the Compute tab.

Under Node groups click Add node group, then enter the following values:

`Name`: `Globomantics-Node-Group`

`Node IAM role` : **Eks-Ec2-Lab-EKS-Node-Role**

Click `Next`.

At the `configuration page`, click `Next`.

At the networking page, click the Subnets drop-down, and ensure only the three Private subnets are selected.

Click Next.

At the Review and create page, click Create.

EKS will begin creating the EC2 instances under this Node group. This will take approximately five to 15 minutes. The creation is successful when the Status changes from Creating to Active. Feel free to click the refresh button to see the updated status.
----------------------------------------------
Connect to Your EKS Cluster
In the top search box, type in and click on EC2.

Click Instances (running).

Select the instance named Eks-Ec2-Lab-BastionInstance.

Click the Connect.

Click the Session Manager tab, then click Connect.

Run the following commands to install the kubectl tool:

echo "[kubernetes]

name=Kubernetes

baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64

enabled=1

gpgcheck=0

repo_gpgcheck=0

gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg" | sudo tee /etc/yum.repos.d/kubernetes.repo

sudo yum install -y kubectl-1.23.6 

kubectl is the CLI tool to manage Kubernetes clusters. This will be your main point of entry to your cluster.

Verify that kubectl was installed correctly by running kubectl version.

Just ensure the output version matches; ignore any connection refused errors.

Run the following command to install eksctl:

curl --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | sudo tar xz -C /usr/local/bin/

eksctl is a CLI tool developed by AWS to perform common EKS tasks. You will use this in the next challenge to associate an IAM Role with a Kubernetes Service Account.

Run eksctl version to confirm that eksctl was installed correctly.

Enter cd to move to the home directory.

You will be creating a local file, and have access to do so in the home directory.

Run the following commands to install helm:

wget https://get.helm.sh/helm-v3.7.2-linux-amd64.tar.gz

tar -zxvf helm-v3.7.2-linux-amd64.tar.gz

sudo mv linux-amd64/helm /usr/local/bin/helm﻿

Run helm version to confirm that helm was installed correctly.

Helm is the package manager for Kubernetes. You will use this in the next challenge to install the AWS Load Balancer Controller package from an EKS repo to properly expose your services to the internet.

Run the following command to authenticate to AWS with your IAM user, using the Access Key ID and Secret Access Key values which are to the right of these instructions:

export AWS_ACCESS_KEY_ID=<Access Key ID>

export AWS_SECRET_ACCESS_KEY=<Secret Access Key>

Only the creator of the cluster can initially access it. This is why you need to configure these IAM credentials and why you can't use the IAM role attached to this instance.

Run aws eks --region us-west-2 update-kubeconfig --name Eks-Ec2-Lab-Cluster. This will update the configuration files to authenticate to the EKS cluster.

To confirm you have successfully connected to the cluster, run kubectl get nodes. 

You should see the domain names of the two instances in the Managed Node Group. Make sure you keep the terminal open for the next challenge.
------------------------------------
Configure the AWS Load Balancer Controller
From the Session Manager Terminal, complete the following steps:

Run eksctl utils associate-iam-oidc-provider --cluster=Eks-Ec2-Lab-Cluster --approve. This will allow pods in the EKS cluster to assume IAM Roles.

Run kubectl apply -f /kubernetes-manifests/kube-sa.yaml. This will create the necessary Service Account, Cluster Role, and Binding to use the AWS Load Balancer Controller.

Run eksctl create iamserviceaccount --cluster=Eks-Ec2-Lab-Cluster --name=aws-load-balancer-controller --namespace=kube-system --override-existing-serviceaccounts  --attach-policy-arn=arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):policy/Alb-Controller-Policy --approve. This will allow the Service Account used by the AWS Load Balancer Controller to create a Load Balancer for your Kubernetes services.

Run helm repo add eks https://aws.github.io/eks-charts. This will add the EKS repo to your list of Helm Repositories.

Run helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=Eks-Ec2-Lab-Cluster --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller to install the AWS Load Balancer Controller for your cluster.

Run kubectl get pods -n kube-system and confirm that you have aws-load-balancer-controller pods running.

Run kubectl apply -f /kubernetes-manifests/globomantics.yaml to deploy your Globomantics application.

Run kubectl get ingress ingress-globomantics -o wide to show your application's access point. The address should look similar to the following: k8s-default-ingressg-xxxxxxxx-xxxxxxxxx.us-west-2.elb.amazonaws.com. If the address is not yet available, re-run the command after a few minutes until you see the address.

You may have noticed that this address directs to an ELB. The AWS Load Balancer Controller automatically created this ELB and configured the ELB target groups to direct traffic to your Kubernetes Service. You can also find this ELB at the EC2 Console﻿. Feel free to explore the target groups created by the controller.

Enter the address from the last task into your browser.

You should see the following web page on your browser; it may take a few minutes to show up, so refresh periodically until it does: