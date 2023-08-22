# srpring boot docker
```
git clone https://github.com/vikash-kumar01/mrdevops-springboot-mongo-docker-application.git
check for the docker file 
install docker and docker compose in the machine

docker run -d -p 27017:27017 --name mrdevopsmongodb mongo:latest
docker build -t springboot-mongodb:1.0 .
docker run -p 8080:8080 --name springboot-mongodb --link mrdevopsmongodb:mongo -d springboot-mongodb:1.0

docker compose

version: "3"
services:
  mrdevopsmongodb:
    image: mongo:latest
    container_name: "mrdevopsmongodb"
    ports:
      - 27017:27017
  springboot-mongodb:
    image: springboot-mongodb:1.0
    container_name: "springboot-mongodb"
    ports:
      - 8080:8080
    links:
      - mrdevopsmongodb


```
