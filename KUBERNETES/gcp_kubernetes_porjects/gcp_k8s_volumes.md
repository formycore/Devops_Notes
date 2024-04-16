# Setup Persistent Volume For GKE
# Create a storage class for GKE
# Create a Persistent Volume using PVC on GKE( for dynamic provisioning first pvc then pv)
# Creating Persistent Volumes From Existing Google Compute Disks
# Example GKE Pod With Persistent Volume
# Example GKE Deployment With Persistent Volume Claim
- #################################################################### -
# Setup Persistent volume for gke
```
1) create a storage class
2) provision the persistent volume using the storage class
3) Test a deployment with persistent volume

kubectl api-resources | grep -i storageclass
storageclasses                    sc                  storage.k8s.io/v1                      false        StorageClass
--------------------------------storage-class-------------------------------------
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gold
provisioner: kubernetes.io/gce-pd
volumeBindingMode: Immediate
allowVolumeExpansion: true
reclaimPolicy: Delete
parameters:
  type: pd-standard
  fstype: ext4
  replication-type: none
------------------------------------------------------
# Create a Persistent Volume using PVC on GKE
So PVC (Request) –> Storage Class (Defines Type of disk) –> Persistent Volume (Google Persistent Disk)
----------------------------------------------
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  storageClassName: gold
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi

------------------------------------------------------------------------
# Creating Persistent Volumes From Existing Google Compute Disks


```
- #################################################################### -
```
- crete a gke with standard with default values
- connect with cloud shell with command 
    - gcloud container clusters <clusteName> --region <region> --project <projectName>
-----------------------------------------------------------------------
We will do the following.

Create a storage class
Provision a Persistent volume using the storage class.
Test a deployment with the persistent volume.


storage class
  persistent disk
        pd-standard
        pd-ssd(mostly for databases)
pv
pvc
-----------------------------------------------
Create a storage class for GKE

Note: There are default storage classes available in GKE which are backed by pd-standard disks. If you don’t specify a storage class while provisioning a PV, the default storage class is considered.

Lets create a gold storage class.




```

# IN DYNAMIC PROVISIONING
```
- users created the pvc first
```

# IN STATIC PROVISIONING
```
- users create the pv first
```
# Steps for the pv & pvc
```
In Kubernetes, the order of creation between PersistentVolumes (PVs) and PersistentVolumeClaims (PVCs) can be flexible:

Static Provisioning: In this scenario, the administrator creates the PV first. It acts like a pre-defined storage resource with details like capacity and access mode. Then, users create PVCs requesting storage that matches the available PVs. Kubernetes binds the PVC to the matching PV.

Dynamic Provisioning: Here, users create PVCs first, specifying their storage requirements. Kubernetes uses StorageClasses to identify a suitable storage provisioner and automatically creates a corresponding PV. This approach simplifies storage management for users.

Here's a breakdown of the roles:

PV (Persistent Volume): The actual storage resource provided by the cluster administrator or dynamically provisioned by Kubernetes. It's like a physical hard drive or cloud storage space.

PVC (PersistentVolumeClaim): A user's request for storage, specifying size, access mode, and potentially storage class for dynamic provisioning. It acts like an application's request for a specific amount of storage from the available resources.

So, the order of creation depends on the provisioning method:

Static: PV -> PVC
Dynamic: PVC -> PV (dynamically created)
```

--------------------------------------------------------------
