# we dont have to login to kubernetes controller node 
* if the private n/w of the controller node is with in the range of the windows system then we can login to the controller node
* curl the site
* chmod +x kubectl
* sudo mv ./kuectl /usr/local/bin/kubectl
* kubectl version
* download the admin.conf file from the controller node ```/etc/kubernetes/admin.conf```
* copy the admin.conf file to the local machine
* rename admin.conf to kubeconfig
* now we can execute the kubectl commands from the linux machine
