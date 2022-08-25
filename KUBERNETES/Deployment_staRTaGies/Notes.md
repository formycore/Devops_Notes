* we have to two images 
    * ```gcr.io/google-samples/hello-app:1.0```
    * ```gcr.io/google-samples/hello-app:2.0```
* this will show appversion and the hostname of the pod

* we will change from 1.0 to 2.0 and see the changes

# Rolling Update
* this is for rolling update
* this is default one 
* with zero down time while changing the image or version
    * ```kubectl set image deployment rolling-update-deployment rollingupdate-image=gcr.io/google-samples/hello-app:2.0```
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rolling-update-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: rolling-update
  template:
    metadata:
      labels:
        app: rolling-update
    spec:
      containers:
      - name: rollingupdate-image
        image: gcr.io/google-samples/hello-app:1.0
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: rolling-update-service
spec:
  type: LoadBalancer
  selector:
    app: rolling-update
  ports:
  - port: 80
    targetPort: 8080
```

# Recreate
* this is for recreate update
* here we are mentioning the   
```
strategy:
    type: Recreate
```
* we get down time for sure while changing the image or version
* it will delete the old pod and create a new pod with down time
* ```kubectl set image deployment recreate-deployment recreate-image=gcr.io/google-samples/hello-app:2.0```
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: recreate-deployment
spec:
  replicas: 3
  strategy:
    type: Recreate  #here we need to mention the type
  selector:
    matchLabels:
      app: recreate
  template:
    metadata:
      labels:
        app: recreate
    spec:
      containers:
      - name: recreate-image
        image: gcr.io/google-samples/hello-app:1.0
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: recreate-service
spec:
  type: LoadBalancer
  selector:
    app: recreate
  ports:
  - port: 80
    targetPort: 8080
```


# Blue-Green

* this is for blue-green update
* we have two deployments with different labels
* and the service pointing to any one of the labels with the below command we can change the label 
pointing to the service
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: blue-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: blue
  template:
    metadata:
      labels:
        app: blue
    spec:
      containers:
      - name: blue-image
        image: gcr.io/google-samples/hello-app:1.0
        ports:
        - containerPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: green-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: green
  template:
    metadata:
      labels:
        app: green
    spec:
      containers:
      - name: green-image
        image: gcr.io/google-samples/hello-app:2.0
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: blue-green-service
spec:
  type: LoadBalancer
  selector:
    app: blue
  ports:
  - port: 80
    targetPort: 8080
```
* ```kubectl patch service blue-green-service -p '{"spec":{"selector":{"app":"green"}}}'```
* we can change the value of the selector to pointer with the above command
* we can select any one blue or green
* spec:selector:app:blue/green
* "spec":{"selector":{"app":"blue/green"}}


# Canary
* in canary 
* we have two deployment with same labels and the service pointing to the same labels
* here it will sent traffic to both the deployment one by one
* **if we use istio we can say 10% traffic to the new deployment and 90% to the old deployment**
* the percentage may vary
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: v1-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: canary
  template:
    metadata:
      labels:
        app: canary
    spec:
      containers:
      - name: canary-v1-image
        image: gcr.io/google-samples/hello-app:1.0
        ports:
        - containerPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: v2-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: canary
  template:
    metadata:
      labels:
        app: canary
    spec:
      containers:
      - name: canary-v2-image
        image: gcr.io/google-samples/hello-app:2.0
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: canary-service
spec:
  type: LoadBalancer
  selector:
    app: canary
  ports:
  - port: 80
    targetPort: 8080
```

