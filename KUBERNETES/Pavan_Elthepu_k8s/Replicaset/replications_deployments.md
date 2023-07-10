# Replication and Deployment
## Replication
```
SELF HEALING
HIGH AVAILABILITY
ROLLOUTS AND ROLLBACKS
SCALING
--------------
# Replicaset
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicationset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      name: nginx-pod
      labels:
        team: integration
        app: nginx
    spec:
      containers:
      - name: nginx-container
        image: nginx
        ports:
        - containerPort: 80
```
--------------
```
replica : 3 
- if the pod is down it will create another pod
- if the pod is already there with this selector it will create only two instead of three
- kubectl get pods
   <name of the prefix of replicaset name>-<id of the pod>
- kubectl get pod <podname>  
- kubectl describe pod <podname>
- kubectl get pod <podname> -o yaml
- kubectl delete pod <podname>


