# Kubernetes Quick Dive
## Architecture
Architecture diagram

- A Python webapp which lets you vote between two options
- A Redis queue which collects new votes
- A .NET worker which consumes votes and stores them in…
- A Postgres database backed by a Docker volume
- A Node.js webapp which shows the results of the voting in real time
    Note
- The voting application only accepts one vote per client. It does not register votes if a vote has already been submitted from a client.
# This is all done with using kubectl commands
## Deploying app with kubernetes
- Before launching the app, lets create a name space and switch to it
```kubectl get ns```
- Create a namespace
```kubectl create ns instavote
    kubectl get ns # to see the namespace
```
- to view the contexts
```kubectl config get-contexts```
- to switch to a context
```kubectl config set-context --current --namespace=instavote```
- Launch the app with newly created namespace
```kubectl create deployment vote --image=schoolofdevops/vote:v4```
# Scalability
- To scale the app
```kubectl scale deployment vote --replicas=4```
- To see the pods and deployment
```kubectl get pods,deployments```
- To see the logs
```kubectl logs -f <pod-name>```
- delete some pods and check the status
```kubectl delete pod <pod-name>```
- To see the status 
```kubectl rs,deployment,pods```
# Load Balancing with Services
- Publish the application (similar to using -P for port mapping)
# Roll Out a New Version
- To change the replicas
```kubeclt scale deployment vote --replicas=12```
- To update the image
```kubectl set image deployment vote vote=schoolofdevops/vote:v5```
- To view the rollout
```kubectl rollout status deployment vote```
