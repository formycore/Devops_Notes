#quotas
```
create a namespace kube-dev
create quota for 5 pods 
create quota for 5gb

- kubectl creaete ns kube-dev
- kubectl creaete quota pod-quota -n kube-dev --hard=pods=5 --dry-run=client -o yaml > podquota.yml
- kubectl create quota memory-quota -n kube-dev --hard=request.memory="5Gi",limits.memory="5Gi" --dry-run=client -o yaml > memquota.yml

-- create 5 pods with different metadata name and pod name with the below code 
for i in 4 5;
# for i in {1..5};
do
cat << EOF > pod-$i.yml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod$i
  namespace: kube-dev
spec:
  containers:
  - name: nginx-container
    image: nginx
    resources:
      requests:
        memory: "500Mi"
      limits:
       memory: "1Gi"
EOF
kubectl apply -f pod-$i.yml
done


controlplane $ cat del_pods.sh 
#!/bin/bash
del_pods=$(kubectl get pods -n kube-dev | awk 'NR > 1 {print $1}')
for i in $del_pods;
do
kubectl delete pods $i -n kube-dev
#echo $i
done
controlplane $ cat create_pods.sh 
#!/bin/bash
for i in {1..5};
do
kubectl run pod-$i --image=nginx -n kube-dev
#echo $i
done
controlplane $ cat loop_pods.sh 
#!/bin/bash
for i in 6;
do
cat << EOF > pod$i.yml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod$i
  namespace: kube-dev
spec:
  containers:
  - name: nginx-container
    image: nginx
    resources:
      requests:
        memory: "500Mi"
      limits:
       memory: "1Gi"
EOF
kubectl apply -f pod$i.yml
echo "--------------------------------------"
kubectl get quota -n kube-dev
done
controlplane $ 	 
```