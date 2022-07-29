    *for example
        * kubectl run nginx-pod --image=nginx --port=80
        * here run = kind of object <here it is pod>
            * if it is deployment we use deployment or deploy
        * nginx-pod is name of pod <object name>
        * then what are the components to require a pod
            * we need a container to create a pod
            * to create a container we use --image
        * --image=nginx is the image to use to create the container
        * --port=80 is the port to expose the container

    *  here we used 
        * object type <here it is pod>
        * object name <here it is nginx-pod>
        * object components <here it is container>
        * version using to create an object <here it is v1>

here 
* object type ---------------------- kind:pod
* object name ---------------------- metadata
* object components ------------------- spec
* version --------------------------- apiVersion:v1
---------------------------------------------------------------------------------------
**services**

    * the pod we created is running with in the node
    * to see the pod we use $ kubectl get pods
    * to see the pod we use $ kubectl get pods -o wide
    * to access this pod we need a service manifest file 
    * **cluster-ip** : Choosing this service only reachable within the cluster
    * **node-port** : Choosing this service outside the cluster by requesting <NodeIp>:<NodePort>
    * **load-balancer** : the service used for load balancing
    * **external-ip** : Maps the service to contents of the (foo.example.com) 
* if we create a new services
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  ports:
  - port: 8080
    targetPort: 80
  type: NodePort
```
    * $ kubectl apply -f nginx-service.yaml
    * $ kubectl get services
    * $ kubectl get all
    * even though we created nginx-service.yaml we can see that it is not running yet
    * EndPoint none so we cannot access it
    * we have created the service but we have not telling to which pod this traffic should go
    * label to the pod 
    ```
    Labels:
        app: demo-nginx
    ```
    * selector to the service
    ```
    Selector:
        app: demo-nginx
    ```
*************************************************************
```
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: demo-nginx
spec:
  containers:
  - image: nginx
    name: nginx-demo
    ports:
    - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  ports:
  - port: 8080
    targetPort: 80
  selector:
    app: demo-nginx
  type: NodePort
```
 * from the above we are saying that accessing the application on NodePort 
 * it will fwd to 8080
 * then it will send it to the port no 80
 * based on the selector (label)
 * this selector (label) is applied to the nginx-pod
 * this is how both pod and service will communicate

    

