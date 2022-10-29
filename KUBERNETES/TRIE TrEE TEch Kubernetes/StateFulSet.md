# STATEFULSETS
* it will deploy one after one
* like if we given the replica count as 3, first it will deploy the first one and then the second one and then the third one
* and this statefulset pods will have numbers to that and that same number will append the pod name
* we dont have random numbers to the pod
* it will ascending order to the pod depends on the replica count
* if the pod got deleted then the new pod will be deployed with the same name 
### Example
* headless service
* if we have three pods 
    * mysql-0
    * mysql-1 
    * mysql-2
* mysql-0 will be the master and mysql-1 and mysql-2 will be the slaves
* in this headless service the write access is given to master and then the read access is given to the slaves
* the master will replicate the data to the slaves
* if we **dont give the headless** service then the service will write on all the pods
* in headless service there wont be **ip address**
* headless service will only give the write access to the master only
* we can read from any of the pods master or slaves
***clusterIP: None***
* is the main purpose of this service
