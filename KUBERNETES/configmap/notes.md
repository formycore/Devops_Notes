# Kubernetes ConfigMap Usage

## 1. Create the ConfigMap

You can create a ConfigMap using the following command:

```
kubectl create configmap test-cm --from-literal=db-port=3306 --dry-run=client -o yaml > demo-cm.yml
kubectl apply -f demo-cm.yml
kubectl get configmap
kubectl describe configmap test-cm
```

Example `demo-cm.yml`:
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: test-cm
data:
  db-port: "3306"
```

---

## 2. Create Deployment **without** Volume Mount

This method injects the ConfigMap value as an environment variable.

Example deployment YAML:
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
        env:
        - name: DB_PORT
          valueFrom:
            configMapKeyRef:
              name: test-cm
              key: db-port
```

Apply the deployment:
```
kubectl apply -f demo-deployment.yml
kubectl get pods
```

---

## 3. Create Deployment **with** Volume Mount

This method mounts the ConfigMap as a file inside the container.

Example deployment YAML:
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

Apply the deployment:
```
kubectl apply -f demo-deployment.yml
kubectl get pods
kubectl exec -it <pod-name> -- /bin/sh
cat /etc/config/db-port
```

To update the ConfigMap and see changes reflected in the pod (when using volume mount):

1. Edit `demo-cm.yml` and change the value:
    ```
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: test-cm
    data:
      db-port: "3307"
    ```
2. Apply the changes:
    ```
    kubectl apply -f demo-cm.yml
    ```
3. Check the updated value inside the pod:
    ```
    kubectl exec -it <pod-name> -- /bin/sh
    cat /etc/config/db-port
    ```

With volume mount, the value updates without needing to delete or recreate the pod.