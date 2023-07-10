# minikube start
minikube start
# Start the minikube with two cluster nodes
minikube start --nodes 2 -p ec2cluster --driver=docker
# Check the status of the cluster
minikube status -p ec2cluster
# Check the status of the cluster
kubectl get nodes -o wide

# Kubectl syntax
```
kubectl [command] [TYPE] [NAME] [flags]
kubectl is the cli
command is the action to perform on the resource (create, get, describe, delete)
TYPE is the resource type (node, pod, deployment)
flags are optional parameters to the command -f file name, -o output format, -n namespace
```

# Kubectl commands
```
kubectl get nodes -o wide
- here each node is a container
- List down all the cluster
    kubectl config get-contexts
- Switch to a cluster
    kubectl config set-context <cluster-name>
- Add the worker node
    minikube node add --<worker/node> -p <cluster-name>
    minikube node add --worker -p ec2cluster
- Delete the worker node
    minikube node delete <node-name> -p <cluster name>
    minikube node delete ec2cluster-m03 -p ec2cluster
- Access the dashboard of the minikube
    minikube dashboard ---url -p <cluster-name>
    minikube dashboard --url -p ec2cluster
    On minikube remote server, ran these:
        minikube dashboard
        kubectl proxy
    On local machine, ran this:
        ssh -i ~/.ssh/id_rsa -L 12345:localhost:8001 ubuntu@<minikube-remote-server-ip>
        http://localhost:12345/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/
