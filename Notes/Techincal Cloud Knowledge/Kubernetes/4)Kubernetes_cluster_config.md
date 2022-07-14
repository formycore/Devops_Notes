on-premises
cloud
vm
platform as service

-------------------
on-premises
    - kubernetes has services like
    - scheduler
    - api server
    - controller
    - coredns
- kubeadm takes care of all the intilazation
- we can also use file method configuration 
- with file method configuration
    - we have manually creates
        - api
        - scheduler
        - controller
- with file method configuration method we can place the api scheduler & controller on
different nodes also
- while with kubeadm all the above components are configured on the same node
----------------------------------
**cloud**
- with Kops only for AWS
- 

- **kubeadm is used for start from the intilaze state**
- **with Kops**
    - **it will create master and nodes with kubeadm,kubelet,kubectl**
    - **autoscalling,loadbalancing**
----------------------------

**platform as service**
- Google - GKE
- AZUre - AKS
- AWS - EKS
- redhat - openshift
  
-----------------------
katacoda
minikube