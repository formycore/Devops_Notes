# HANDS ON ISTIO/JAEGER/K8/EKS/KIALI
```
1) Create the AWS EC2 linux AMI instance
- Install kubectl [ We will be accessing the PODS and resources of k8]
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256) kubectl" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
- Install eksctl [ We will create the cluster ]
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/bin
eksctl version
```
# 2) Add IAM role to EC2 [ So that EC2 access the EKS ]
```
Go to IAM -> CLICK CREATE NEW IAM ROLE ->
SELECT EC2 -> CLICK ON ADMINISTRATOR ACCESS
-> CREATE ROLE

Go toEC2 instance you have created -> Click on
ACTIONS -> SECURITY -> MODIFY IAM ROLE ->
ATTACH YOUR NEW ROLE

```

# 3) Create Cluster
```eksctl create cluster --name=eksdemo1 --region=us-west-1 --zones=us-west-1b,us-west-1a --without-nodegroup```
# 4) Add OIDC
```eksctl utils associate-iam-oidc-provider --region us-west-1 --cluster eksdemo --approve```
# 5) Add nodes
```eksctl create nodegroup --cluster=eksdemo1 --region=us-west-1
--name=eksdemo-ng-public --node-type=t2.medium --nodes=2
--nodes-min=2 --nodes-max=4 --node-volume-size=10 --ssh-access
--ssh-public-key=key-test --managed --asg-access --external-dns-access
--full-ecr-access --appmesh-access --alb-ingress-access
6) INSTALL ISTIO
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.18.1
TARGET_ARCH=x86_64 sh -
7) Go into the directory
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli
cd istio-1.18.1
The installation directory contains:
● Sample applications in samples/
● The istioctl client binary in the bin/ directory.
8) SET THE PATH
export PATH=$PWD/bin:$PATH
9) INSTALL THE ISTIO WITH DEMO PROFILE
istioctl install --set profile=demo -y
10)
kubectl apply -f
https://raw.githubusercontent.com/istio/istio/release-1.18/samples/boo
kinfo/platform/kube/bookinfo.yaml
11) kubectl get services
12) kubectl get pods
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli
13) Hit the below command
kubectl exec "$(kubectl get pod -l app=ratings -o
jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS
productpage:9080/productpage | grep -o "<title>.*</title>"
14)TO INJECT ISTIO AS INIT CONTAINER [
NOW 2 PODS WILL RUN ]
- kubectl label namespace default istio-injection=enabled
- istioctl analyze
- Delete all pods
kubectl delete pod <pod_name>
[ NOTE - You will see two container per pod ]
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli
15) cd samples/bookinfo/networking/
kubectl apply -f bookinfo-gateway.yaml
16) kubectl get vs
kubectl get gateway
17)
kubectl get svc istio-ingressgateway -n istio-system
18) Set the ingress IP and ports:
export INGRESS_HOST=$(kubectl -n istio-system get service
istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service
istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service
istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
19) echo $SECURE_INGRESS_PORT
20)
export
INGRESS_HOST=a06f39bd75fac4a8491ee0db7ba09704-646636610.us
-west-1.elb.amazonaws.com
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
echo $GATEWAY_URL
21) HIT THE BELOW URL
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli
echo "http://$GATEWAY_URL/productpage"
http://a02c0d05e773744d289073f25ac63817-1278996514.us-west-1.elb.amazon
aws.com/productpage
22) KIALI DASHOBAORD [ ALL TOOLS INSTALLATION ]
cd istio-1.18.1/samples/addons
kubectl apply -f samples/addons
Or
Kubectl apply -f .
23) DO PORT FORWARD
OPEN THE SG TO ALL TRAFFIC
kubectl port-forward --address 0.0.0.0 svc/kiali 9008:20001 -n istio-system
http://54.67.18.57:9008/kiali/console/overview?duration=60&refresh=60000
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli
24) FOR JAEGER
kubectl port-forward --address 0.0.0.0 svc/tracing 8008:80 -n
istio-system
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli
Delete:
DELETE NODE
eksctl delete nodegroup --cluster=eksdemo
--region=us-west-1 --name=eksdemo-ng-public
DELETE CLUSTER
eksctl delete cluster --name=eksdemo --region=us-west-1
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli
Website - www.praveensingampalli.com
Youtube - https://www.youtube.com/praveensingampalli