# Kubernetes RBAC Hands-On Guide
```

              +---------------------------+
              |  RoleBinding /            |
              |  ClusterRoleBinding       |
              +------------+--------------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
+-----------------------+     +------------------------+
|   ServiceAccount      |     |   Role / ClusterRole   |
+-----------------------+     +------------------------+

- there is role/clusterrole which defines permissions
- there is serviceaccount which represents an identity
- there is rolebinding/clusterrolebinding which binds the role to the serviceaccount

```

## 📌 Overview

RBAC flow in Kubernetes:

```
ServiceAccount → Role/ClusterRole → RoleBinding/ClusterRoleBinding
```

### Core Concept

**RoleBinding = Role (permissions) + Subject (who)**

---

## 🏗️ Step-by-Step Implementation

### Step 1: Create Namespace

```bash
kubectl create namespace rbacdemo
```

### Step 2: Create ServiceAccount

Generate the YAML:
```bash
kubectl create serviceaccount foo -n rbacdemo --dry-run=client -o yaml
```

**serviceaccount.yml**
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: foo
  namespace: rbacdemo
```

Apply it:
```bash
kubectl apply -f serviceaccount.yml
```

### Step 3: Check Permissions (Before RBAC)

```bash
kubectl auth can-i --as system:serviceaccount:rbacdemo:foo get pods -n rbacdemo
```

**Output:** ❌ `no`

**Reason:** No role assigned yet

### Step 4: Create Role



#### ✅ Correct Role

**pod-reader-role.yaml**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: rbacdemo
rules:
  - apiGroups: [""]
    resources: ["pods"]         
    verbs: ["get","list","watch"]
```

Apply it:
```bash
kubectl apply -f pod-reader-role.yaml
```

### Step 5: Create RoleBinding

RoleBinding binds the Role to ServiceAccount

**rolebinding.yml**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: podreaderbinding
  namespace: rbacdemo
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: pod-reader
subjects:
- kind: ServiceAccount
  name: foo
  apiGroup: ""
```
## why subjects has apigroup is present and where as in roleRef it is not present?
- because in subjects we are referring to a core API resource (ServiceAccount) which does not belong to any API group, hence apiGroup is empty string. In roleRef we are referring to a resource that belongs to the rbac.authorization.k8s.io API group, so we specify that in roleRef.   


Apply it:
```bash
kubectl apply -f rolebinding.yml
```

### Step 6: Create ClusterRoleBinding

For cluster-wide permissions:

**clusterrolebinding.yml**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: pod-reader-cluster-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: foo
  apiGroup: ""
  namespace: rbacdemo
```

Apply it:
```bash
kubectl apply -f clusterrolebinding.yml
```

---

## 🔑 Key Concepts

### Role vs ClusterRole
- **Role**: Namespace-scoped permissions
- **ClusterRole**: Cluster-wide permissions

### RoleBinding vs ClusterRoleBinding
- **RoleBinding**: Binds Role to ServiceAccount in a specific namespace
- **ClusterRoleBinding**: Binds ClusterRole to ServiceAccount cluster-wide

### ServiceAccount
- Represents an identity within a namespace
- Used by pods to authenticate with the Kubernetes API

---

## ✅ Verification

After applying all resources, check permissions:

```bash
kubectl auth can-i --as system:serviceaccount:rbacdemo:foo get pods -n rbacdemo
```

**Expected Output:** ✅ `yes`

---

## 📋 Summary of RBAC Components

| Component | Purpose | Scope |
|-----------|---------|-------|
| ServiceAccount | Identity for applications | Namespace |
| Role | Define permissions | Namespace |
| RoleBinding | Bind Role to ServiceAccount | Namespace |
| ClusterRole | Define cluster-wide permissions | Cluster |
| ClusterRoleBinding | Bind ClusterRole to ServiceAccount | Cluster |

---

## 🚀 Quick Apply All

```bash
kubectl apply -f . -n rbacdemo
```

This applies all YAML files in the current directory to the rbacdemo namespace.
