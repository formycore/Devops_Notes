# MultiStage Build for backend React
```
- under backend/.env.sample file update the value of VITE_API_PATH="http://<public-ip>:5000
```
```
# ------------------------------------------ Stage 1 Build Stage--------------------------------------------------------------
# Base Image
FROM node:21 AS fronend-builder
# Set the working dir to app
WORKDIR /app
# Copy the package.json and package-lock.json and dependencies
COPY packag*.json /
# Install dependencies
RUN npm i
# Copy the rest of the application
COPY . .
--------------------------------------------Stage 2---------------------------------------------------------------------------
# Base Image
FROM node:21-slim
# Set the working dir to app
WORKDIR /app
# Copy the build assests and dependencies from fronend-builder stage 
COPY --from=fronend-builder /app .
# Copy the .env.sample file to  .env.local
COPY .env.sample .env.local
# Expose the port 5173 for nodejs application
EXPOSE 5173
# Run the code
CMD ["npm", "run", "dev", "--", "--host"]
#################################################################################################################################
```
# MultiStage Build for Frontend Nodejs
```
- if we are going with dockerization 
- use MONGODB_URI="mongodb://mongo/wanderlust"
- CORS_ORIGIN="<public-ip>:5173
```
```
# ------------------------------------------ Stage 1 Build Stage--------------------------------------------------------------
# Base Image
FROM node:21 AS fronend-builder
# Set the working dir to app
WORKDIR /app
# Copy the package.json and package-lock.json and dependencies
COPY package*.json ./ # this part is imp it needs to be in the docker container
# Install dependencies
RUN npm install
# Copy the rest of the application
COPY . .
#--------------------------------------------Stage 2---------------------------------------------------------------------------
# Base Image
FROM node:21-slim
# Set the working dir to app
WORKDIR /app
# Copy the build assests and dependencies from fronend-builder stage 
COPY --from=fronend-builder /app .
# Copy the .env.sample file to  .env.local
COPY .env.sample .env.local
# Expose the port 5173 for nodejs application
EXPOSE 5173
# Run the code
CMD ["npm", "run", "dev", "--", "--host"]
#################################################################################################################################
```
# Docker-compose file
- on the root folder 
- 
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
## if we access the webpage we will get the issue 
```
- docker exec -it <name of the container> (mongoimport --db wanderlust --collection posts --file ./data/sample_posts.json --jsonArray)
- docker exec -it mongo mongoimport --db wanderlust --collection posts --file ./data/sample_posts.json --jsonArray
```

# with the update of the redis on the code 
```
- go to backend/.env.sample 
- change the value 
- REDIS_URL="127.0.0.1:6379"
- REDIS_URL="redis/redis:6379"

under the compose file
redis:
  container_name: redis
  restart: unless-stopped
  image: redis:7.0.5-alpine
  expose:
    - 6379
  depends_on:
    - mongodb
  
```