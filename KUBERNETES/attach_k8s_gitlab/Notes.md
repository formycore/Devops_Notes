# Install gitlab on the K8s cluster

# create a a manifest file for deployment
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```
# Create a service for the deployment
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
  type: NodePort
```

# Attaching the k8s cluster to the gitlab
- Go to the gitlab project
- in k8s master 
- cat ~/.kube/config | base64 -w 0
- copy the output and paste it in the variable in the gitlab project
- Create a gitlab-ci.yml file in the root of the project
```
deploy:
  stage: deploy
  before_script:
  - echo $KUBECONFIG | base64 --decode > config.yaml
  - export KUBECONFIG=config.yaml
  script:
    - kubectl apply -f nginx-deployment.yaml
    - kubectl apply -f nginx-service.yaml
  tags:
    - kube

```
