Setting up a Namespace
Check current config

kubectl config view
kubectl config get-contexts
You could also examine the current configs in file cat ~/.kube/config

Creating a namespace
Namespaces offers separation of resources running on the same physical infrastructure into virtual clusters. It is typically useful in mid to large scale environments with multiple projects, teams and need separate scopes. It could also be useful to map to your workflow stages e.g. dev, stage, prod.

Lets create a namespace called instavote

cd projects/instavote
cat instavote-ns.yaml
[output]

kind: Namespace
apiVersion: v1
metadata:
  name: instavote
Lets create a namespace

kubectl get ns
kubectl apply -f instavote-ns.yaml

kubectl get ns
And switch to it

kubectl config --help

kubectl config get-contexts

kubectl config current-context

kubectl config set-context --current --namespace=instavote

kubectl config view

kubectl config get-contexts

Exercise: Go back to the monitoring screen and observe what happens after switching the namespace.