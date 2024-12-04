# steps in the canary deployment
```
- the traffic will be changed with the percentage like 25%,50%,75%,100%
- here we have two deployments 
- it should deployed along with the old deploy
- we need to mention the same label name in the old and new deploy files
- we will be having only one service file for the both old and new deploy
- we will use the same label in the service 
- this is manual process
- for suppose in the old deploy we have 4 replicas and the new deploy we will be having 1 replica 
- we need to deploy the old and new manifest files
- so here we have total 5 pods
- now we need to change the old deploy from 4 to 3 replicas
- apply again the old deploy
- the api will receive the one pod from the new deploy and 3 pods from the old deploy
- now the 25% looks good , then go with 50% 
- when the new deploy is up then only we need to update the old deploy
- now the replicas in the new deploy is 2 and old is still at 3 
- we need to update the values of the new deploy to 2 and then only we need to replace the old deploy replicas with 2
- we need to increase the replicas in the new deploy and decrease in the old deploy 
- we need the delete the old deploy
```