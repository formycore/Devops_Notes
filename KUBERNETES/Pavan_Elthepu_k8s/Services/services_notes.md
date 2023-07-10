# SERVICES
```
- pods have ip address
- we cannot rely on ip address because it is dynamic
- we need a way to access the pods
- services are the way to access the pods
- svc have ip address and it is static
- users can access the svc ip address and svc will redirect the request to the pod
- svc is not on the node
- svc is on the master node
- kubectl api-resouces | grep svc
############################################
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  ports:
    - targetPort: 80 # specifies the port on container in the port 80, as we are using nginx on port # 80
      port: 80
      nodePort: 30008
  selector:
    app: nginx
############################################

- kubectl get svc
- kubectl describe svc <svcname>
- kubectl get svc -o yaml
- kubectl delete svc <svcname>
- kubectl apply -f <filename>
- kubectl get svc
- kubectl exec -it <podname> -- bash
- curl <svcname>:8082
- curl <private ip>:8082
- kubectl port-forward <podname> <port on local machine>:<port on pod>
- kubectl port-forward nginx 8083:8082
```
## Multiport container
```
############################################
apiVersion: v1
kind: Service
metadata:
  name: multi-port-container-service
spec:
  selector:
    app: nginx
  ports:
    - name: proxy
      port: 8082
      targetPort: 80
    - name: application
      port: 8083
      targetPort: 8083
############################################
- kubectl apply -f multi-port-container-service.yaml
- a pod has 2 containers 
- ports is an array
- for multiple service name is mandatory
- so now our service accepts two ports one is on 8082 and other is on 8083
- the container ports are running on 80 and 8083
- if we access service on 8082 it will redirect to 80


```

## Test
```
- testing for the nginx-service
- kubectl exec -it <podname> -- bash
i=1
while [ $i -le 10 ]; do
curl nginx-service:8082
i=$(( i+1 ))
done


-- on the other tab check the logs
- kubectl logs <podname>
- kubectl logs <podname> -f # for continous watching
## What pod associated with the service ?
  -- when a svc is created an endpoint is created with the same name of the svc


```

------------------------------------------------------------------------------------
## CLUSTER IP
```
- no outside access
- only inside the cluster
- database is the best example for this kind of service
############################################
apiVersion: v1
kind: Service
metadata:
  name: mysql-clusterip-service
spec:
    type: ClusterIP
    ports:
        - targetPort: 3306 
        port: 3306
    selector:
        app: mysql
############################################
```
## port forwarding
```
- kubectl port-forward <podname> <port on local machine>:<port on pod>
- kubectl port-forward nginx 8083:80
```

------------------------------------------------------------------------------------
## NodePort
```
- access from outside the cluster
- access using <nodeip>:<nodeport>
- nodeport range is 30000-32767
############################################
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport-service
spec:
  type: NodePort
  ports:
    - targetPort: 80
      port: 80
      nodePort: 30008
  selector:
    label:
      app: nginx
############################################

- kubectl apply -f nginx-service.yaml
- kubectl get svc
- ON MINIKUBE 
- TO ACCESS THE SERVICE WITH NODEPORT
- minikube ip -p <cluster-name>
- minikube ip -p ec2cluser(ec2cluster is any example for the cluster)
- minikube service nginx-service -p ec2cluster

```
------------------------------------------------------------------------------------
## LoadBalancer
```
- only works on cloud providers
- creates a load balancer on the cloud
- access using <loadbalancerip>:<port>
############################################
apiVersion: v1
kind: Service
metadata:
  name: nginx-loadbalancer-service
spec:
  type: LoadBalancer
  ports:
    - targetPort: 8082
      port: 80
      nodePort: 30008
  selector:
    label:
      app: nginx
############################################
- kubectl apply -f nginx-service.yaml
- kubectl get svc
```
------------------------------------------------------------------------------------
