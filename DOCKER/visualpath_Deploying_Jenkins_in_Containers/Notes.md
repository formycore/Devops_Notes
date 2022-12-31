https://github.com/dubareddy/kubernetes_latest_manifest/blob/main/DockerEngine/T03-Docker-containers/02-Docker-containers-advanced.md


# how to ensure my container start with docker host boot time
- create a container with parameter
    - --restart policy
        - always
        - never
        - on-failure -- only works on the exit code is greater than 0 (exit > 0)
    # lets create a container with always restart policy
    ```
    docker container rund -d --name <container_name> -- hostname <hostname_name> \
    -p <outside>:<inside docker> --restart=always <image_name:version>
    docker container run -d --name ngnix_new --hostname webservernginx -p 8090:80 \
    --restart=always nginx:latest
    ```
    ex: 
    ```docker run -d --name webngix --restart always nginx:latest```
    # to check the docker ip address
        - docker inspect container_name | grep ip
        - docker container inspect webnginx --format "{{.NetworkSettings.IPAdress}}"
    # restart policy for the exited container
    - Yes, we can add few changes to existing containers like CPU, Memory, blkio and restart policy as well.
    - We can not add like port farwarding etc., once the conatiners are created.
    - We have to delete and recreate them with proper parameters.
    # docker container update
    ```docker container update --help ```
    ```docker container update <container_name> --restart always```
    - after restart the docker server containers will all up and running we can see that from the
      status 
    # delete the containers
    -- list only the container id
    ``` docker containers ps -aq```
    ``` for i in `docker containers ps -aq`;do docker container rm $i;done```
    - here we get some error becoz it will not remove the running containers
    ```
    for i in `docker container ps -aq`;
       do
        docker container stop $i;
        docker container rm $i;
       done
    ```
    - google search for the live restore docker
    - dockre image rm <image_name>
    - docker rmi <image_name>
    


