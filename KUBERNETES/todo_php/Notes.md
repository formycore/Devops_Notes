# 🚀 Kubernetes PHP Todo App Setup (MySQL + phpMyAdmin)

This guide sets up a complete PHP Todo application with MySQL and phpMyAdmin in Kubernetes.

---

# 📌 Architecture

```
PHP App  → mysql-svc → MySQL Pod
phpMyAdmin → mysql-svc → MySQL Pod
```

👉 Always use **service name (`mysql-svc`)**, never IP.

---

# ✅ Step 1: ConfigMap & Secret (MySQL)
## Create Namespace

```bash
kubectl create namespace todo
```

## Create ConfigMap


```bash
kubectl create configmap db-cm \
  --from-literal=MYSQL_DATABASE=todo \
  -n todo
```

## Create Secret

```bash
kubectl create secret generic db-secret \
  --from-literal=MYSQL_ROOT_PASSWORD=root123 \
  -n todo
```

## Verify

```bash
kubectl get cm -n todo
kubectl get secrets -n todo
```

---

# ✅ Step 2: MySQL Pod

## mysql.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mysql-pod
  namespace: todo
spec:
  containers:
  - name: mysql
    image: mysql:5.7
    ports:
      - containerPort: 3306
    envFrom:
      - configMapRef:
          name: db-cm
      - secretRef:
          name: db-secret
```

## Apply

```bash
kubectl apply -f mysql.yaml
```

## Expose Service

```bash
kubectl expose pod mysql-pod \
  --port=3306 \
  --target-port=3306 \
  --name=mysql-svc \
  -n todo
```

---

# ✅ Step 3: phpMyAdmin

## ConfigMap

```bash
kubectl create configmap phpadmin-cm \
  --from-literal=PMA_HOST=mysql-svc \
  --from-literal=PMA_PORT=3306 \
  -n todo
```

## Secret

```bash
kubectl create secret generic phpadmin-secret \
  --from-literal=PMA_USER=root \
  --from-literal=PMA_PASSWORD=root123 \
  -n todo
```

## phpmyadmin.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: phpmyadmin-pod
  namespace: todo
spec:
  containers:
  - name: phpmyadmin
    image: phpmyadmin
    ports:
      - containerPort: 80
    envFrom:
      - configMapRef:
          name: phpadmin-cm
      - secretRef:
          name: phpadmin-secret
```

## Apply

```bash
kubectl apply -f phpmyadmin.yaml
```

## Expose

```bash
kubectl expose pod phpmyadmin-pod \
  --type=NodePort \
  --port=8080 \
  --target-port=80 \
  --name=phpmyadmin-svc \
  -n todo
```

---

# ✅ Step 4: PHP Todo App

## Prepare Code

```bash
git clone https://github.com/Fir3eye/php-todo-app.git
cd php-todo-app

# Keep only src folder
find . -mindepth 1 -maxdepth 1 ! -name src -exec rm -rf {} +
```

---

## 🔥 IMPORTANT: Update DB Connection

### ❌ Wrong

```php
mysqli_connect('10.x.x.x', ...)
```

### ✅ Correct

```php
mysqli_connect('mysql-svc', 'root', 'root123', 'todo');
```

---

## Build & Load Image

```bash
docker build -t formycore/phptodo:060403 .
minikube image load formycore/phptodo:060403
```

---

## Create Pod YAML

```bash
kubectl run phptodo-pod \
  --image=formycore/phptodo:060403 \
  --dry-run=client -o yaml > phptodo.yaml
```

## Apply

```bash
kubectl apply -f phptodo.yaml -n todo
```

## Expose

```bash
kubectl expose pod phptodo-pod \
  --type=NodePort \
  --port=8055 \
  --target-port=80 \
  --name=phptodo-svc \
  -n todo
```

---

# 🧪 Access Application

```bash
minikube service phptodo-svc -n todo
```

---

# 🧠 Key Learnings

| Mistake ❌        | Fix ✅                 |
| ---------------- | --------------------- |
| Using IP address | Use `mysql-svc`       |
| Missing env vars | Use `envFrom`         |
| Wrong namespace  | Always use `-n todo`  |
| Hardcoded config | Use service-based DNS |

---

# 🚀 Next Improvements

* Use **Deployment instead of Pods**
* Add **Persistent Volume for MySQL**
* Use **ConfigMap + Secret for app config**
* Convert to **Helm chart**

---

# ✅ Final Status

* MySQL → Running
* phpMyAdmin → Running
* PHP App → Connected via `mysql-svc`

---

🎉 Your Kubernetes PHP stack is now fully working!
