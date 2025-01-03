**https://harryhiyoshi.hashnode.dev/run-springboot-petstore-with-docker**

# Run Springboot Petstore with Docker and Docker Compose
**1) Clone Spring PetcClinic on the local directory where you want to store**
```
git clone https://github.com/spring-projects/spring-petclinic.git
cd spring-petclinic
echo "target" > .dockerignore
```
**2) Create volumes and network to persist the data in the repository**
```
docker volume create mysql_data
docker network create mysqlnet
```
**3) Run a container of MySQL**
```
docker run -it --rm -d -v mysql_data:/var/lib/mysql \
-v mysql_config:/etc/mysql/conf.d \
--network mysqlnet \
--name mysqlserver \
-e MYSQL_USER=petclinic -e MYSQL_PASSWORD=petclinic \
-e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=petclinic \
-p 3306:3306 mysql:8.0
```
**4) Create a docker file to run the spring boot java app**
```
vim Dockerfile


FROM eclipse-temurin:17-jdk-jammy

WORKDIR /app

COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./mvnw dependency:resolve

COPY src ./src
CMD ["./mvnw", "spring-boot:run", "-Dspring-boot.run.profiles=mysql"]
```
**6) Run the docker of the app**
```
docker run --rm -d --name springboot-server --network mysqlnet -e MYSQL_URL=jdbc:mysql://mysqlserver/petclinic -p 8080:8080 java-docker
```
### we can access the docker from the port 8080

## Creating the tables using the Database
```
docker cp :~/spring-petclinic/src/main/resources/db/mysql/*.sql mysqlserver:/*.sql (do this for the all sql files 3 are there)
#docker login to the docker container 
  docker exec -it mysqlserver bash
mysql -u petclinic -p petclinic < /schema.sql
mysql -u petclinic -p petclinic < /data.sql
mysql -u root -p
mysql> SHOW DATABASES;
mysql> SHOW TABLES;
mysql> SHOW tables;
mysql> SELECT * FROM OWNERS;
mysql> SELECT * FROM owners;
```
## on the app 
```
create the user 
```
