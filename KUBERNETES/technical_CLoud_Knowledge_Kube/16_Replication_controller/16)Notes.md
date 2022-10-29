# 16 - Lab for the replication controller
* to check is there are any pods
    $ kubectl get pods
* to check is there are any replication controllers
    $ kubectl get replicationcontrollers
* to check is there are any services
    $ kubectl get services
* to check is there are any controller on the pod
    $ kubectl describe pod <pod_name>
    * we get the replication controller name
* to get the manifest file help
    $ kubectl explain rc
    $ kubectl explain rc --recursive | less
vi replication_controller.yaml
```
apiVersion: v1
kind: ReplicationController
metadata:
  name: samantharc # this is RC name
spec:
  replicas: 3 # here we are setting the number of replicas
  selector:
    team: dev # here we are taking the label to the pod
  template: # pod configuration
    metadata:
      name: samanthapod # this is pod name
        labels:
            team: dev # this is the label to the pod
    spec:
        containers: # here we are setting the container
        - name: samanthacontainer # this is the container name
          image: nginx
          ports: # here we are setting the port
            - containerPort: 80
            
```
* we can also see pod and rc
    $ kubectl get pods,rc
* now create the rc from the above file
    $ kubectl create -f replication_controller.yaml
* now we check the labels
    $ kubectl get pods,rc --show-labels
* use describe to get the rc details
    $ kubectl describe rc samantharc
* to remove the rc
    $ kubectl delete rc samantharc

* for example we created a pod
   $ kubectl run web --image=nginx
   $ kubectl get pods --show-labels
* remove the labels from the pod
    $ kubectl label pod <pod_name> <label>-
    $ kubectl label pod web run-
* set custom labels to the pod
    $ kubectl label pod <pod_name> <label>=<value>
    $ kubectl label pod web team=dev
* here one pod is created with the label team=dev
* now if we run the above replication_controller with replicas as 3 now we get only 2 pods as the first pod is running with the label team=dev
* if we want to troubleshoot any pod we remove the label team=dev and run the below command
    $ kubectl get pods <pod_name> <label>-
    $ kubectl get pods web team=dev-
* now the replication controller will create 1 more pod with the label team=dev as one of the pod is removed with the label
* now we troubleshoot the pod
    $ kubectl describe pod <pod_name>
    $ kubectl describe pod web team=dev
* after completion of the troubleshooting we can remove the label team=dev from the pod
    $ kubectl label pod <pod_name> <label>
    $ kubectl label pod web team=dev
* now the newly craeted pod deletes as the replicas are set to be only 3
** now we can also save the pods even after removing the replication controller **
    $ kubectl delete rc --cascade=false <rc_name>
    $ kubectl delete rc --cascade=false samantharc
