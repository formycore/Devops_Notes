# https://www.youtube.com/watch?v=fwtxi_BRmt0&t=395s
`step 1:
1) create a repo A on gitlab
2) create agent on gitlab
3) Install gitlab agent on k8s cluster
4) Register connection between k8s and gitlab

step 2:
- create repo B on gitlab
- create k8s manifest for our project
- push project data on repo B
- create image and push it to gitlab container Registery
- final cicd
-----------------------------------------------------------------------------
- build a container image with the source code 
- push it to container registry 
- pull the image from the container registry to kubernetes nodes
- to create the connection between the k8s and gitlab repo named (k8s-connection) we need to create a empty project 
- create a new repo (project k8s-data) to put the data`

-----------------------------------------------------------------------------
## steps to connect to gitlab to k8s
`https://docs.gitlab.com/user/clusters/agent/`

`- Connecting a Kubernetes cluster with GitLab
- To connect a Kubernetes cluster to GitLab, you must first install an agent in your cluster.`

`- https://docs.gitlab.com/user/clusters/agent/install/`
`- Installing the agent for Kubernetes
- Install the agent manually`

`- https://docs.gitlab.com/user/clusters/agent/install/#create-an-agent-configuration-file`

`- In the repository, in the default branch, create an agent configuration file at:
- .gitlab/agents/<agent-name>/config.yaml
- here we need to give a name for the agent-name (k8s-connection)
- create this file under the repo k8s-connection`
- go to k8s-connection repo create a new file
- paste the second line and change the agent-name to (k8s-connection)
- we have empty config.yaml file 
- it acts as firewall in this file we define 
    - which group
    -  username
    -  repository
    - to access to the kubernetes cluster

`
### Register the agent with GitLab
Option 1: Agent connects to GitLab
You can create a new agent record directly from the GitLab UI. The agent can be registered without creating an agent configuration file.

You must register an agent before you can install the agent in your cluster. To register an agent:

On the left sidebar, select Search or go to and find your project. If you have an agent configuration file, it must be in this project. Your cluster manifest files should also be in this project.

Select Operate > Kubernetes clusters.

Select Connect a cluster (agent).

In the Name of new agent field, enter a unique name for your agent (k8s-connection).

    - If an agent configuration file with this name already exists, it is used.
    - after selecting the name 
    - register 
    - copy the agent access token 
- go with helm process
    - 



