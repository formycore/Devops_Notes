# TAINT AND TOLERATION
* taints and toleration are used to set restrictions on what pods can be scheduled on a node
    * add a tain on node to restrict pods from being scheduled
    * add a toleration on pod to allow specific pod to be scheduled on the tainted node
* for suppose we have 3 nodes
    node 1 
    node 2 
    node 3 
    
    and 4 pods
    pods-A 
    pods-B 
    pods-C 
    pods-D
    * for the application x if we need pod-A and pod-B should be on the same node we use this taint and tolerance
    * node1 is tainted one
    * and pod-A and pod-B has tolerance 
    * now pod-A and pod-B now allowed to be scheduled on the node even though it has taint on that node

## Taints - Node
    * kubectl taint nodes <node-name> key=value:taint-effect
    ```
    taint-effect has three options
        NoSchedule
        PreferNoSchedule
        NoExecute
    ```
    ### Example
    ```
    kubectl taint nodes node1 app=red:NoSchedule
    * from the above command no pod is scheduled on the node1 unless it has matching tolerance
    * so we need to have tolerance on the pod-A&B tolerance
    * below is the example for tolerance code
    ```
    apiVersion: v1
    kind: Pod
    metadata:
      name: myapp-pod
    spec:
      containers:
      - name: nginx-container
        image: nginx
      tolerantions:
        - key: "app"
          operator: "equal"
          value: red
          effect: "NoSchedule"
    ```
    





------------------------------------------------------------------------
* if we have two nodes 
    * node1
    * node2
* if node1 has taint and noscheduler enabled and node2 has nothing
* if pod1 is created with toleration noscheduler
* then pod1 may go on any node with or without taint and noscheduler
* if the pod2 is created with **nothing** about toleration noscheduler
* then pod2 **wont** go to node1 with **taint and noscheduler**
* pod2 will deploy on the node2 where there is no taint

* if we create a node with taint
    * the pod wont deploy on that node
    * untill and unless it has toleration on the pod 
