for example
    * kubectl run nginx-pod --image=nginx --port=80
    * here run = kind of object <here it is pod>
         * if it is deployment we use deployment or deploy
    * nginx-pod is name of pod <object name>
    * then what are the components to require a pod
        * we need a container to create a pod
        * to create a container we use --image
    * --image=nginx is the image to use to create the container
    * --port=80 is the port to expose the container

    *  here we used 
        * object type <here it is pod>
        * object name <here it is nginx-pod>
        * object components <here it is container>
        * version using to create an object <here it is v1>

here 
* object type ---------------------- kind:pod
* object name ---------------------- metadata
* object components ------------------- spec
* version --------------------------- apiVersion:v1
---------------------------------------------------------------------------------------
**services**

    * the pod we created is running with in the node
    * to see the pod we use $ kubectl get pods
    * to see the pod we use $ kubectl get pods -o wide
    *  