# we dont have to login to the controller node to work 
* if the private n/w of the controller node is with in the range of the windows system then we can login to the controller node
* copy the ```/etc/kubernetes/admin.conf``` file to the ```c:/users``` file in the windows system and rename the file as ```config```
* install kubectl on the windows system
* copy the config file path and add in environmental variable
* run the command ```kubectl get nodes``` to check the nodes in the cluster
* run the command ```kubectl get pods``` to check the pods in the cluster
