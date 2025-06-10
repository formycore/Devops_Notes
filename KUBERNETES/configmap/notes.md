# Kubernetes ConfigMap Usage

## 1. Create the ConfigMap

You can create a ConfigMap using the following commands:

```
# Generate a ConfigMap YAML from a literal key-value pair (db-port=3306)
kubectl create configmap test-cm --from-literal=db-port=3306 --dry-run=client -o yaml > demo-cm.yml

# Apply the generated YAML to create the ConfigMap in the cluster
kubectl apply -f demo-cm.yml

# List all ConfigMaps in the current namespace
kubectl get configmap

# Show detailed information about the created ConfigMap
kubectl describe configmap test-cm
```

Example `demo-cm.yml`:
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: test-cm
data:
  db-port: "3306"   # The key-value pair stored in the ConfigMap
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
  replicas: 1   # Number of pod replicas
  selector:
    matchLabels:
      app: myapp   # Selector to match pods with this label
  template:
    metadata:
      labels:
        app: myapp   # Pod label
    spec:
      containers:
      - name: myapp
        image: abhishekf5/python-sample-app-demo:v1   # Sample app image
        ports:
        - containerPort: 8000   # Expose port 8000 in the container
        env:
        - name: DB_PORT   # Set environment variable DB_PORT in the container
          valueFrom:
            configMapKeyRef:
              name: test-cm   # Reference the ConfigMap named 'test-cm'
              key: db-port    # Use the value of 'db-port' key from the ConfigMap
```

Apply the deployment:
```
# Create the deployment using the YAML file
kubectl apply -f demo-deployment.yml

# List all pods to verify deployment
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
  replicas: 1   # Number of pod replicas
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
        - name: config-volume   # Name of the volume to mount
          mountPath: /etc/config   # Mount the ConfigMap at this path inside the container
      volumes:
      - name: config-volume
        configMap:
          name: test-cm   # Reference the ConfigMap named 'test-cm'
```

Apply the deployment and verify:
```
# Create the deployment using the YAML file
kubectl apply -f demo-deployment.yml

# List all pods to verify deployment
kubectl get pods

# Open a shell inside the running pod (replace <pod-name> with actual pod name)
kubectl exec -it <pod-name> -- /bin/sh

# View the contents of the mounted ConfigMap file
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
      db-port: "3307"   # Change the value to 3307
    ```
2. Apply the changes:
    ```
    # Update the ConfigMap in the cluster
    kubectl apply -f demo-cm.yml
    ```
3. Check the updated value inside the pod:
    ```
    # Open a shell inside the pod again
    kubectl exec -it <pod-name> -- /bin/sh

    # Verify the updated value
    cat /etc/config/db-port
    ```

> **Note:**  
> With volume mount, the value updates automatically inside the pod without needing to delete or recreate the pod.