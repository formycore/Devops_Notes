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
