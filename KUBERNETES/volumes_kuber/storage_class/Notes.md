# Installing and Configuring AWS EBS CSI Driver for Kubernetes Cluster with Dynamic Provisioning of EBS Volumes

## Storage class for unmanaged kubernetes
```
if the kubernetes version is < 1.20 we can use provisioner as kubernetes.io/aws-ebs
if the kubernetes version is > 1.20 we need to install ebs csi driver 
we will install ebs csi driver with the helm chart 
if we use volumeBindingMode as immediate
     - as the pvc is created 
     - storageclass will provision the volume
     - storageclass has to create the pv
     - kuberneted pv & pvc will be bounded
    - here comes the issue
    - what if the pod for which this volume is created in not created
    - in that case storage is wasted
if we use volumeBindingMode is WaitForFirstConsumer
    - as along the pod is not created
    - storageclass will not provision the volume
    - if the pod is created, storage class will create the pv & storage
    - kubernetes will bind the pv & pvc
```

## To install EBS driver install with helm chart
### Installing Helm
- on the master node of kubernetes cluster
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

```
- Add the AWS EBS CSI Driver Helm chart repository:
```
helm repo add aws-ebs-csi-driver https://kubernetes-sigs.github.io/aws-ebs-csi-driver
helm repo update
```
- Deploy the AWS EBS CSI Driver using the following command:
```
helm upgrade --install aws-ebs-csi-driver \
    --namespace kube-system \
    aws-ebs-csi-driver/aws-ebs-csi-driver
```
- Verify that the driver has been deployed and the pods are running:
```kubectl get pods -n kube-system -l app.kubernetes.io/name=aws-ebs-csi-driver```


### Installing AWS EBS CSI Driver
- create a user in iam 
- attach the policy AmazonEC2FullAccess
- create user
- select the user 
- under security credentials tab
- create access key
- select command line (CLI)
- here we will get the access key id & secret access key
- on the master node of kubernetes cluster
- run the below command

- Create a secret to store your AWS access key and secret key using the following command:
```
kubectl create secret generic aws-secret \
    --namespace kube-system \
    --from-literal "key_id=${AWS_ACCESS_KEY_ID}" \
    --from-literal "access_key=${AWS_SECRET_ACCESS_KEY}"

```



# Creating Storage Class
```
storage class
#################################
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-sc
provisioner: ebs.csi.aws.com # if the kubernetes version is > 1.20 or above # here we need to ebs provisioner
paramaters:
  type: gp2
volumeBindingMode: WaitForFirstConsumer/Immediate
```
- Provisioning EBS Volumes
```kubectl apply -f storageclass.yaml```

- Create a pvc.yaml file and apply the pvc.yaml file using the following command:
```
#################
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ebs-claim
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 1Gi
#################
```
```kubectl apply -f pvc.yaml```
- Verify that the EBS volume has been provisioned and attached to the pod:
```kubectl get pvc
kubectl get pv
kubectl get pods
kubectl describe pod <pod-name>
kubectl exec -it <pod-name> -- /bin/bash
df -h
lsblk
exit
```