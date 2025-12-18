- kubectl kustomize -h 
- if we have 3 environments (dev, staging, prod) with different configurations, we can create a base kustomization.yaml file and then create overlays for each environment.
- overlays can be environment-specific directories that contain patches or additional resources specific patches
- we need this kind of directory structure:
  ```
  .
  ├── base
  │   ├── deployment.yaml
  │   ├── service.yaml
  │   └── kustomization.yaml
  └── overlays
      ├── dev
      │   ├── kustomization.yaml
      ├── staging
      │   ├── kustomization.yaml
      └── prod
          ├── kustomization.yaml
  ```
------------------------------
```
- under base/kustomization.yaml, we define the common resources:
  ```yaml
  apiVersion: kustomize.config.k8s.io/v1beta1
  kind: Kustomization
  resources:
    - deployment.yaml
    - service.yaml
  ```
- under base/deploy.yaml 
```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  strategy: {}
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
```
- under base/svc.yaml
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```
- under overlays/dev/kustomization.yaml, we can add environment-specific configurations:
  ```yaml
  apiVersion: kustomize.config.k8s.io/v1beta1
  kind: Kustomization

  resources:
    - ../../base

  # Options to add prefix/suffix to names
  namePrefix: dev-
  ```
- similarly, we can create overlays for staging and prod with their specific configurations.
-----------------------------------------------------------------------------------
**before applying kustomize, we can preview the final manifests using:**
```
kubectl kustomize base/deploy.yaml
```
- we can apply the kustomized manifests for a specific environment using:
```
kubectl apply -k overlays/dev
```
- with base and overlays we can see the differences in the name
```
kubectl kustomize base                                                                                                                                              ─╯
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  strategy: {}
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
```
```
kubectl kustomize base                                                                                                                                              ─╯
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  strategy: {}
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
```
