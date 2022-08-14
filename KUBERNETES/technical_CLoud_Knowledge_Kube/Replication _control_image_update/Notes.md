# Replication controller image update or rolling update
* previously we checked how to Replication Controller is done and it's management
* now we check how to rolling update is done
* why & how need to be done
    * in the previous rc we need to change the image of the container 
    * in the kubernetes version older than 1.14 rolling update is removed
***************************************************************************************************************
```
apiVersion: v1
kind: ReplicationController
metadata:
  name: devteamrc
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.1
        ports:
        - containerPort: 80
```
***************************************************************************************************************
* above the Replication Controller is done
* now we need to change the image of the container along with the names of the other specs also
* like in metadata name,selector name,template label name, image name that we need to change
* as these are already taken by the kubernetes
***************************************************************************************************************
```
apiVersion: v1
kind: ReplicationController
metadata:
  name: updatedevteamrc
spec:
  replicas: 3
  selector:
    app: nginxupdate
  template:
    metadata:
      labels:
        app: nginxupdate
    spec:
      containers:
      - name: nginx
        image: nginx:1.9.0
        ports:
        - containerPort: 80
```        
***************************************************************************************************************
* ```kubectl rolling-update <old rc name> --update-period=10s -f rc.yaml```
* ```kubectl rolling-update devteamrc --update-period=10s -f rc.yaml```
***************************************************************************************************************
* the process is like 
    * 1. we create a new rc with the new image
    * 2. the old pods will delete one by one while the new rc creates the new image pods with one by one
    * 3. the old pods will be deleted after the new pods are created
    * 4. Then both old and new RC will be deleted
    * 5. the new RC will be created with the new image
    * 6. During this time there is not new rc or old rc 
    * 7. here we get the downtime for the application
***************************************************************************************************************