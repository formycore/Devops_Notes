# pods
```
- pods can be scalable not the containers
- we can add the env variables,
      - can we add the new helper container to the pod
```
# Delployment
```
- here we give the template for the pods for adding the replicas
- scalable
- auto healing
- rolling updates
- rollback
```
# Services
```
- to give access the outside world
```
# Persistent Volume
```
- like volumes in docker
- when a persistent volume is created, it can claimed
```

# Autohealing
```
- kubectl get pods
NAME                                       READY   STATUS    RESTARTS   AGE
mypod                                      0/1     Unknown   0          17d
two-tier-app-deployment-6d57cb8df6-9k4jk   1/1     Running   0          5s
two-tier-app-deployment-6d57cb8df6-c2nnt   1/1     Running   0          5s
two-tier-app-deployment-6d57cb8df6-c6fl2   1/1     Running   0          64m
two-tier-app-deployment-6d57cb8df6-sjnvz   1/1     Running   0          64m
two-tier-app-pod                           1/1     Running   0          79m
maanya@master:~/shubham_2_tier_app$ kubectl delete pod two-tier-app-deployment-6d57cb8df6-9k4jk
pod "two-tier-app-deployment-6d57cb8df6-9k4jk" deleted
maanya@master:~/shubham_2_tier_app$ kubectl get pods
NAME                                       READY   STATUS    RESTARTS   AGE
mypod                                      0/1     Unknown   0          17d
two-tier-app-deployment-6d57cb8df6-7brmg   1/1     Running   0          3s
two-tier-app-deployment-6d57cb8df6-c2nnt   1/1     Running   0          60s
two-tier-app-deployment-6d57cb8df6-c6fl2   1/1     Running   0          65m
two-tier-app-deployment-6d57cb8df6-sjnvz   1/1     Running   0          65m
two-tier-app-pod                           1/1     Running   0          80m
```

# Scaling
```
- kubectl scale deployment name(in the metadata in the yml file) --replicas=<no of pods>
- kubectl scale deployment two-tier-app-deployment --replicas=4
```

# Services
```
- it will access to the outside world
- all the deployment have some label
- in the two-tier-app-deploy.yml file we have the label
- all the pods have the label will be grouped together and gives the ip address to it or pod is given to us
- these are three types of services
    - ClusterIP
    - NodePort
    - LoadBalancer
```
-------------------------------------------------------------------------------
- now we can access the app 
- kubectl get pods -o wide
- get the node ip and the port that mentioned in the service
- now create the mysql-deployment.yml file
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
  labels:
    app: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql-ctr
        image: mysql:latest
        env:
          - name: MYSQL_ROOT_PASSWORD
            value: "admin"
          - name: MYSQL_USER
            value: "root"
          - name: MYSQL_PASSWORD
            value: "admin"
          - name: MYSQL_DATABASE
            value: "mydb"
        ports:
          - containerPort: 3306
        imagePullPolicy: Always
```
- kubectl apply -f mysql-deployment.yml
- kubectl get pods
- we will get error becoz the volumes are missed here
- kubectl delete -f mysql-deployment.yml
- kubeclt get pods
- here we need the persistent volume
--------------------------------------------------
# Persistent Volume
```
- to store the database with the system storage
- this give some space from the host to this container/app
- in the pv file, in the host part make sure that the path is there
----------------------
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv
spec:
  capacity:
    storage: 256Mi
  volumeMode: Filesystem
  accessMode:
    -ReadWriteOnce
  persistentVolumeReclaimPolicy: Retian
  hostpath:
    path: /home/maanya/mysqldata
------------------
- now we need to claim this volume
-----------------------
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pvc
spec:
  accessMode:
    - ReadWriteOnce
  resources:
    requests:
      storage: 256Mi
-----------------------
- now we need to change the mysql-deployment.yml file
-----------------------
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
  labels:
    app: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql-ctr
        image: mysql:latest
        env:
          - name: MYSQL_ROOT_PASSWORD
            value: "admin"
          - name: MYSQL_USER
            value: "root"
          - name: MYSQL_PASSWORD
            value: "admin"
          - name: MYSQL_DATABASE
            value: "mydb"
        ports:
          - containerPort: 3306
        volumeMounts:
          - name: mysqldata
            mountPath: /var/lib/mysql
      volumes:
        - name: mysqldata
          PersistentVolumeClaim:
            claimName: mysql-pvc
-----------------------
- kubectl apply -f mysql-deployment.yml
- kubectl get pods
- now create the service for the mysql
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
    selector:
        app: mysql
    ports:
        - protocol: TCP
        port: 3306
        targetPort: 3306
--------------------------------
- kubectl apply -f mysql-service.yml
kubectl get svc
NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes         ClusterIP   10.96.0.1       <none>        443/TCP          19d
mysql              ClusterIP   10.101.15.155   <none>        3306/TCP         55s
sample-service     NodePort    10.104.82.135   <none>        5000:32421/TCP   19d
two-tier-app-svc   NodePort    10.105.154.1    <none>        80:31000/TCP     74m
---------------------
- now copy the clusterip of mysql service
- now go to the two-tier-app-deploy.yml file
- in the env part add the mysql service cluster ip
        env:
          - name: MYSQL_HOST
            value: "10.101.15.155"
          - name: MYSQL_USER
            value: "root"
          - name: MYSQL_PASSWORD
            value: "admin"
          - name: MYSQL_DB
            value: "mydb"

```
## Entering into the mysql pod
```
- kubectl exec -it mysql-7b4b8f7b5b-7brmg -- /bin/bash
- mysql -u root -p
- admin
- show databases;
- use mydb;
- show tables;
- select * from users;
```

