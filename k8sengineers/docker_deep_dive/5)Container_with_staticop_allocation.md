# scenario 01: default bridge name
```
docker run -d --name nginx:default1 --ip 172.17.0.10 nginx

docker container inspect nginx-defaultnw | grep -i IP | awk '/IPAddress/{print $2}' | awk NR==2
"172.17.0.2",

-it is created with default ip(172.17.0.2) not the one i have given (172.17.0.10)
```
# scenario02 : user defind new nw
```
docker network create --subnet 10.10.0.0/16 --gateway 10.10.0.1 webapp
docker network ls

docker run -d --name nginx-webapp --network webapp --ip 10.10.0.10 nginx

docker container inspect nginx-webapp | grep -i IP | awk '/IPAddress/ {print $2}'
null,
"",
"10.10.0.10",

here we can get the desired ip address to the container
```


# scenario 03: add the same ip address to the new container
```
docker run -d --name nginx-webapp01 --network webapp --ip 10.10.0.10 nginx
docker: Error response from daemon: Address already in use.

docker logs nginx-webapp01 
there will be no logs becoz to view the logs the container should be started, it got failed even before staratd

Example:

there are below containers are running

173c1c133db1   nginx     "/docker-entrypoint.…"   3 minutes ago    Created                           nginx-webapp01
dce09be2c4a4   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes           80/tcp    nginx-webapp
423d9d057aff   nginx     "/docker-entrypoint.…"   27 minutes ago   Up 27 minutes           80/tcp    nginx-defaultnw
adb055c3807c   nginx     "/docker-entrypoint.…"   3 days ago       Exited (0) 3 days ago             test_host

- the ip 10.10.0.1 is allocated to nginx-webapp what if we stop this and allocate this to the nginx-webapp01 and start it 

- docker stop nginx-webapp
- docker ps
- docker start nginx-webapp01
- it is successfully started 
docker container inspect nginx-webapp01 | grep -i IP | awk -F '"' '/IPAddress/ {print $1,$4}'
             
             
                     10.10.0.10

- now start nginx-webapp
- docker start nginx-webapp
- it will throw the error
- docker ps -a
- docker logs nginx-webapp


```

