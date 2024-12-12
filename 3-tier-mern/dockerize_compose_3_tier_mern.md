# Dockerize 3 tier mern steps for run Manually
- here we need to follow the process 
	- first db
	- then backend
	- then frontend
```
- git clone https://github.com/LondheShubham153/wanderlust.git
- change to git branch to devops
	- git checkout devops
- first create the Dockerfile for the backend
1) Navigate to the Backend Directory
	- cd backend/
2) Install Required Dependencies
	- npm i (here npm is node)
3) Configure Environment Variables
	- cp .env.sample .env
4) Start the Backend Server
	- npm start
5) [BACKEND] Server is running on port 5000
	- open the port 5000

```
# Dockerfile for backend
- go inside the backend/
```
FROM node:21
WORKDIR /app
COPY . .
RUN npm i
COPY .env.sample .env
EXPOSE 5000
CMD ["npm", "start"]


```
## Build the Dockerfile
```
- docker build -t backend:v1 .
```


## Setup MongoDB
```
- docker run -detach -ports container_port:host_port --name of the container image
# Pulling the mongo image and running it 
- docker run -d -p 27017:27017 --name mongo mongo:latest 
# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                                           NAMES
4dc513786ed6   mongo:latest   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   mongo
# to check whether the mongo is running successfully
- go inside the docker container 
- docker exec -it <name of the container> bash
- docker exec -it mongo bash
- inside the docker container 
- run 
- mongosh
- exit() # to come out of the mongosh 
- exit # from the container

```
# Now run the Docker image for the backend
```
# with this we are running the docker build
- docker run -d -p 5000:5000 --name backend backend:v1
```
## Now setup the frontend
```
FROM node:21
WORKDIR /app
COPY . .
RUN npm i
COPY .env.sample .env.local
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]

- docker run -d -p 5173:5173 --name frontend frontend:v1

```
```
- if we check the site is up but not showing any content 
- f12
- network
- refresh the page
- featured
- check the status it is showing as local
- we need to change the env Variables of the frontend
- in the frontend
- cat .env.sample
- edit the value of the VITE_API_PATH to the public ip

```
### IF WE CHANGE THE CODE WE NEED TO BUILD DOCEKR FILE AGAIN

```
- all three containers are created but cannot communicate with each other
- 

```
# DOCKER COMPOSE
```
Install docker COMPOSE
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version

- create the docker-compose file on the root folder of the wanderlust
- 

```
# Docker compose file

```
version: '3.8'
services:
  mongodb:
    container_name: mongo
    image: mongo:latest
    ports:
      - "27017:27017"
  backend:
    container_name: backend
    build: ./backend
    env_file:
      - ./backend/.env.sample
    ports:
      - "5000:5000"
  frontend:
    container_name: frontend
    build: ./frontend
    env_file:
      - ./frontend/.env.sample
    ports:
      - "5173:5173"
```
- here we might get the error connection
- and we need to import the database also
- here is the update docker-compose FILE
```
# first mongodb should run till the backend should wait
# attach the sample database which is under the backend dir attached to this container with volume
version: '3.8'
services:
  mongodb:
    container_name: mongo
    image: mongo:latest
    volume:
      - ./backend/data:/data # we need to run sample database on the this so we have attached the ./backend/data to this volume
    ports:
      - "27017:27017"
  backend:
    container_name: backend
    build: ./backend
    env_file:
      - ./backend/.env.sample
    ports:
      - "5000:5000"
    depends_on:
      - mongodb
  frontend:
    container_name: frontend
    build: ./frontend
    env_file:
      - ./frontend/.env.sample
    ports:
      - "5173:5173"
volumes:
  data: # from the above lines we have created the data, here we are creating it 
  
```
- now the database is not there in the mongo container
- now we need to copy sample database to the container
- docker exec -it <container name>< command >
- docker exec -it <mongo><mongoimport --db wanderlust --collection posts --file ./data/sample_posts.json --jsonArray>
- now the database is not connected 
- now to connect with the frontend with backend 
- 
------------------------------------------------------------------------------------------------------------------------------------
# first mongodb should run till the backend should wait
# attach the sample database which is under the backend dir attached to this container with volume
```
version: '3.8'
services:
  mongodb:
    container_name: mongo
    image: mongo:latest
    volumes:
      - ./backend/data:/data # we need to run sample database on the this so we have attached the ./backend/data to this volume
    ports:
      - "27017:27017"
  backend:
    container_name: backend
    build: ./backend
    env_file:
      - ./backend/.env.sample
    ports:
      - "5000:5000"
    depends_on:
      - mongodb
  frontend:
    container_name: frontend
    build: ./frontend
    env_file:
      - ./frontend/.env.sample
    ports:
      - "5173:5173"
volumes:
  data: # from the above lines we have created the data, here we are creating it 
```
 - here we need Import sample data
 - mongoimport --db wanderlust --collection posts --file ./data/sample_posts.json --jsonArray
 - we need to go inside the mongo container
- docker exec -it mongo  mongoimport --db wanderlust --collection posts --file ./data/sample_posts.json --jsonArray
- open the frontend container
- with http only 
- still no data is present in the webpage
- there is an update in the backend/.env.sample file
- add the these lines in the
- CORS_ORIGIN="http://<public-ip>:5173"
- cors is cross origin site reference
- if we accessing this site from different origin it shows some issue
- NOW THERE IS CHANGE IN THE CODE 
- WE NEED TO BUILD AGAIN
- docker-compose down
- docker-compose up --build
- now we get the db connection error
- in containers if they needs to connect each other they do with names of the container
- cd backend/
- change the value of Mongodb_url under .env.sample 
- now change the Mongodb_url value from 127.0.0.1 to name of the mongodb container <mongo>
```