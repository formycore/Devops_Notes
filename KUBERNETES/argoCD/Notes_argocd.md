argocd monitor apps deployed on the cluster
we need to feed the argocd server with the cluster config
argocd concept is similar to git with push and pull architecture
to deploy app to cluster

with argocd we must maintain two repos
1) app repo (we maintain dockerfiles)
2) manifest files repo (we maintain k8s manifest files)
3) connect these two repos with argocd server