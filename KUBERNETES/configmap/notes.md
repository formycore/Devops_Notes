# config map
- if we want to change the values of the env values inside the container it is not possible
- so we use config map for first then we can use config with volume mount

## config map with env 
- kubectl create configmap <configmap-name> --from-literal=<key>=<value> --dry-run=client -o yaml > demo-cm.yml
- kubectl create configmap test-cm --from-literal=db-port=3306 --dry-run=client -o yaml > demo-cm.yml
- kubectl apply -f demo-cm.yml
- kubectl get configmap
- kubectl describe configmap <configmap-name>
---------------------
- now create a pod with config map
- kubectl create deployment myapp --image=abhishekf5/python-sample-app-demo:v1 --dry-run=client -o yaml > demo-deployment.yml
- kubectl apply -f demo-deployment.yml
- kubectl get pods
- if we change the value of config map we need to delete the pod and recreate it
- but if we go with volume mount then we can change the value of config map without deleting the pod
## config map with volume mount
- kubectl create configmap test-cm --from-literal=db-port=3306 --dry-run=client -o yaml > demo-cm.yml
- kubectl apply -f demo-cm.yml
- kubectl create deployment myapp --image=abhishekf5/python-sample-app-demo:v1 --port=3306 --dry-run=client -o yaml > demo-deployment.yml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
    replicas: 1
    selector:
        matchLabels:
        app: myapp
    template:
        metadata:
        labels:
            app: myapp
        spec:
        containers:
        - name: myapp
            image: abhishekf5/python-sample-app-demo:v1
            ports:
            - containerPort: 8000
            volumeMounts:
            - name: config-volume
            mountPath: /etc/config
        volumes:
        - name: config-volume
            configMap:
            name: test-cm
```     
- kubectl apply -f demo-deployment.yml
- kubectl get pods
- kubectl exec -it <pod-name> -- /bin/sh
- cat /etc/config/db-por
- now change the value of config map
- vim demo-cm.yml
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: test-cm
data:
  db-port: "3307"
``` 
- kubectl apply -f demo-cm.yml
- kubectl exec -it <pod-name> -- /bin/sh
- cat /etc/config/db-port
- now we can see the value is changed without deleting the pod
