```
kubectl scale --replicas=4 resource_name/resource_type
kubectl scale --replicas=4 deployment/nginx-deployment

```
## IT IS BETTER TO CHANGE IN THE MANIFEST FILE THE REPLICAS NUMBER


## Change the image
```
----------------------
apiVersion: apps/v1
kind: Deployment
metadata:
  - name: nginx-depl
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
    - name: nginx-pod
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx-containers
          image: nginx:1.21.3
          ports:
            - containerPort: 80
----------------------
- kubectl apply -f nginx-deployment.yaml
- kubectl get pods --show-labels
- if we change anything in the manifest file, a new rollout is created with new replicaset
- OLD REPLICATION DONT DELETES
- KUBERNETES STORES THE LAST 10 REPLICAS SETS AND CAN ROLLOUT TO ANY VERSION 
- in the yaml file 
- replicas: 3
  revisionHistoryLimits: 100
- kubectl set image resource_type/resource_name container_name=<new container image>
- kubectl set image deployment/nginx-deployment nginx-container=nginx:1.21.1
- now the image is updated
- kubectl rollout history <resource_type>/<resource_name>
- the out put will be like mostly empty with nothing in the change-cuase column
- kubectl rollout history deployments/nginx-deployment
- kubectl set image deployment/nginx-deployment nginx-container=nginx:1.21.1 --record
- kubectl rollout history deployments/nginx-deployment
- now we get the change-cause column with the image updated
- this will help in history 
- kubectl rollout history deployment/nginx-deployment 
###########################################
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
annotations:
    kubernetes.io/change-cause: "image updated to alpine"
    spec:
      replicas: 3
        selector:
          matchLabels:
            app: nginx
        template:
          metadata:
            name: nginx-pod
             labels:
               app: nginx
        spec:
          containers:
            - name: nginx-container
              image: nginx:alpine
              ports:
                - containerPort: 80
###########################################
- kubectl apply -f nginx-deployment.yaml


- kubectl rollout history deployment/nginx-deployment

- kubectl rollout undo deployment/nginx-deployment
     this will do the rollback to the previous version

- kubectl rollout undo deployment/nginx-deployment --to-revision=2
    this will do the rollback to the specific version


#################################################
```