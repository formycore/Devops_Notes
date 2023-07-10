```
- take an example of peaseeds (chikkudgaya)
- seeds inside the peaseeds are called containers
- peaseeds shell is called node
- A pod is group of one or more containers with shared n/w and storage resources
- to talk to kubernetes we need kubectl
- kubectl run <pod name> --image=<docker image name>
- kubectl run nginx --image=nginx
- kubectl get pods
- kubectl describe pod <pod name>
vi nginx-pod1.yaml
############################################
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod1
  labels:
    app: todo
    team: integration
    # These labels acts as indentifiers to the pod
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
############################################
- kubectl apply -f <filename>
- kubectl apply  -f nginx-pod1.yaml
- kubectl get pods
## Filter the pod with labels
- kubectl get pods --show-labels
- kubectl get pods -l app=todo
- kubectl get pods -l app=todo,team=integration
- kubectl get pod nginx-pod1 -o wide
- kubectl get pod nginx-pod1 -o yaml

```

## Port forwarding
```
- kubectl port-forward <pod name> <port to forward>:<port to forward to>
- kubectl port-forward nginx-pod1 8080:80
```
## LOGS
```
kubectl logs <pod name>
kubectl logs nginx-pod1
```
## Exec
```
kubectl exec -it <pod name> -- <command>
kubectl exec -it nginx-pod1 -- /bin/bash
```
## Delete pod
```
kubectl delete pod <pod name>
kubectl delete pod nginx-pod1
kubectl delete -f <pod yaml file>
kubectl delete -f pod-definition.yml
```

