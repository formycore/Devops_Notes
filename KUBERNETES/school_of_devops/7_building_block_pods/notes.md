we can use create or apply
- apply do we create and update
- creating, updating , or making changes
```
kubectl apply --help
```
```
kubectl get pods --help
```
-------------------------------------
# Port forward
```
kubectl # just type it will show the list of commands
kubectl port-forward podname local:remote
```
# trouble shoot
```
kubectl edit pod podname
kubectl edit pod vote

- here change the image version to v50 under specs
- save and exit

- now check on the 
        - kubectl get pod podname -o yaml
        - here we get the message that is very helpful

```
# to check the status of the pod
```
kubectl get pods podname -o yaml
kubectl get pods vote -o yaml
kubectl get pods vote -o json

```
------------------------------------------------------------------------
# Volumes








------------------------------------------------------------------------
# multiple containers
```
apiVersion: v1
kind: Pod
metadata:
  name: web
  labels:
    tier: front
    app: nginx
    role: ui
spec:
  containers:
    - name: nginx
      image: nginx:stable-alpine
      ports:
        - containerPort: 80
          protocol: TCP
      volumeMounts:
        - name: data
          mountPath: /var/www/html-sample-app
    - name: sync
      image: schoolofdevops/sync:v2
      volumeMounts:
        - name: data
          mountPath: /var/www/app

  volumes:
    - name: data
      emptyDir: {} # it will empty only if the pod got delete not the container

```
------------------------------------------------------------------------
# connecting to the pods
```
here we have two containers
kubectl get pod
kubectl exec -it podname -- sh
kubectl exec -it web /sh
--- this will connect to the nginx container
--- if we want to another container
kubectl exec -it web sh -c sync
 
```