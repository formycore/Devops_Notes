# Without any volume
```
####################################
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
        - image: mongo
          name: mongo
          args: ["--dbpath", "/data/db"]
          env:
            - name: MONGO_INITDB_ROOT_USERNAME
              value: "admin"
            - name: MONGO_INITDB_ROOT_PASSWORD
              value: "password"
####################################

- kubectl apply -f mongo-deployment.yaml
- install mongodb compass
- connect to the mongodb
- https://www.mongodb.com/docs/compass/master/install/
- mongodb-compass
add data:
  -> Insert document
       {
        "title": "Refer Docker volumes"
       }
-> go inside container
-> check if data is added
-> kubectl exec -it <pod name> -- /bin/bash
- kubectl exec -it mongo-6966577c7c-2jq7k -- /bin/bash
- check the process of mongo
- ps -ef | grep mongo
- kill pid
- kubectl get pods
- if the restart count is 1 then it is restarted
- restarted the container not the pod
- the data is lost

```
# emptyDir

```
- to avoid this we use volumes
- storing the data in pod is best practice than storing in container
- attached emptyDir to the pod and mounted it to the container
- emptyDir is a volume type which is created when the pod is created and deleted when the pod is deleted

####################################
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
        - image: mongo
          name: mongo
          args: ["--dbpath", "/data/db"]
          env:
            - name: MONGO_INITDB_ROOT_USERNAME
              value: "admin"
            - name: MONGO_INITDB_ROOT_PASSWORD
              value: "password"
          volumeMounts:
            - mountPath: /data/db
              name: mongo-volume
      volumes:
        - name: mongo-volume
          emptyDir: {}
####################################
- kubectl apply -f mongo-deployment.yaml
- kubectl get pods -o wide check for the node name
- kubectl get pods -o yaml < to get the more info the pod >
- the location of the data is /var/lib/kubelet/pods/<pod_id>/volumes/kubernetes.io~empty-dir on the node it is running
- now delete the pod
- kubectl delete pod <pod_name>
- kubectl delete pod mongo-6966577c7c-2jq7k
- volume also deleted

```

# hostPath

```
####################################
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
        - name: mongo
          image: mongo
          args: ["--dbpath", "/data/db"]
          env:
            - name: MONGO_INITDB_ROOT_USERNAME
              value: "admin"
            - name: MONGO_INITDB_ROOT_PASSWORD
              value: "password"
          volumeMounts:
            - mountPath: /data/db
              name: mongo-volume
      volumes:
        - name: mongo-volume
          hostPath:
            path: /data
####################################
- kubectl apply -f mongo-deployment.yaml
- kubectl get pods -o wide
- kubectl delete pod <pod name>
- kubeclt delete pod
- data is not deleted

```
## Sharing data between containers
### what if the pods are running on different nodes and we want to share the data between them
### what if the node is delted and the data is lost
```
solution is persistent volume
1) persistent volume
2) persistent volume claim
3) storage class

1) persistent volume
- piece of storage in the cluster
- pv is kubernetes resource
- created with yaml

- it is a storage unit
- it is a cluster resource
- it is a volume that is created on the cluster
- it is not attached to any pod
- create a persistent volume

- accessModes are 
     - ReadWriteMany
     - ReadWriteOnce
     - ReadOnlyOnce
     - ReadOnlyMany
     - ReadWriteOncePod
- ReadWriteMany is used for sharing the data between the pods
- ReadWriteOnce is used for single node, if all the pods are running on the same node
- ReadOnlyOnce is used for single pod, we cannot write to it
- ReadOnlyMany is used for sharing the data between the pods, we cannot write to it
- ReadWriteOncePod is used for single pod
- in the persistent volume we can specified the storage size as 3GB
- we will have these pv storage sizes

```
## persistent volume
```
####################################
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mongo-pv
spec:
  capacity:
    storage: 3Gi
  accessModes:
    - ReadWriteMany
    # - ReadWriteOnce
    # - ReadOnlyOnce
    # - ReadOnlyMany
    # - ReadWriteOncePod
  local:
    path: /home/ubuntu/test
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - nodea # any node name
####################################
- kubectl apply -f mongo-pv.yaml
- kubectl get pv
- kubectl describe pv mongo-pv



```


## persistent volume claim
```
- how much storage we want to use for the pod
- when we specify access mode and persistance volume claim
- pvc looks for the pv with the same access mode and storage size
- for example if we specify 3GB storage size in pvc, it looks for the pv with 3GB storage size and also for the access mode specified in the pvc 
- now we specify the pvc in the pod we are running
- when we run the pod, and declare a volume in it with this pvc, the pod will look for the pvc and attaches to the pv that is bound to the pvc
- instead of using pv directly we use pvc 

####################################
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongo-pvc
spec: # specify the access modes and capacity
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 3Gi
  storageClassName: ""

####################################
- kubectl apply -f mongo-pvc.yaml
- kubectl get pvc
- check for the status and volume 
- bound means it is attached to the pv
- in the volume column we can see the pv name
- kubectl get pv
- status changes from available to bound
- now change the volumes section in the deployment file
####################################
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
        - name: mongo
          image: mongo
          args: ["--dbpath", "/data/db"]
          env:
            - name: MONGO_INITDB_ROOT_USERNAME
              value: "admin"
            - name: MONGO_INITDB_ROOT_PASSWORD
              value: "password"
          volumeMounts:
            - mountPath: /data/db
              name: mongo-volume
      volumes:
        - name: mongo-volume
          hostPath:
            path: /data
####################################
- kubectl apply -f mongo-deployment.yaml

```
## Deletion of pv and pvc
```
- to delete pv and pvc 
- first delete the pvc
- then pv
- if not the pv will be in terminating state
- kubectl delete pvc mongo-pvc
- kubectl delete pv mongo-pv
- kubectl get pv
- kubectl get pvc
- kubectl get pv -o wide
- kubectl get pvc -o wide

        OR
- first delete the pod
- kubectl delete mongo_deployment.yaml

- kubectl get pv
- if the status is released then we can delete the pv
- kubectl delete pv <pv name>
