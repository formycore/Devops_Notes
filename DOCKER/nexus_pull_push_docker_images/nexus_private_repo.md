# Nexus private repo 
## Create nexus volume
```
docker volume created nexus-data
```
## Start the Nexus container with volume
```
docker run -d -p 8081:8081 --name nexus --mount source=nexus-data,target=/nexus-data sonatype/nexus3
- the above command will start the nexus container and mount the volume nexus-data to /nexus-data
- the nexus container will be accessible at http://localhost:8081
- the nexus data will be stored in the volume nexus-data
- cd /var/lib/docker/volumes/nexus-data/_data
- cat admin.password
- login to the nexus ui with the admin.password
- click gear icon on the top right corner and click repositories
- create a new repository of type docker hosted
- name it docker-private
- click on the new repository and enable http and add 8083 to it

```
## Login to nexus
```
login to nexus UI http://localhost:8081
- create a Docker hosted repository call it docker-private
``` 
## Stop and remove nexus container
```
docker stop nexus
docker rm nexus
```
## Start the nexus container with port mapping to the docker private repo
``` 
docker run -d --name nexus -p 8081:8081 -p 8083:8083 --mount source=nexus-data,target=/nexus-data sonatype/nexus3
```

## Accessing
```
- to pull and push we need to have insecure registry
- we are not using https so we need to add the insecure registry to the docker daemon
- add the following to /etc/docker/daemon.json
{
  "insecure-registries" : ["localhost:8083"]
}
- restart the docker daemon
- systemctl restart docker
- docker start nexus
- docker info (to check the insecure registry is added)
- docker images (to check the images)
- docker build -t localhost:8083/docker-private/hello-world .
- docker push localhost:8083/docker-private/hello-world
- 
```