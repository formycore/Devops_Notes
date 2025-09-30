# the docker commands 
- always run the *database* commands first
```
docker run -d \
    --name mysql \
    -v mysql-data:/var/lib/mysql \
    --network=twotier \
    -e MYSQL_DATABASE=mydb \
    -e MYSQL_USER=root \
    -e MYSQL_PASSWORD=admin \
    -e MYSQL_ROOT_PASSWORD=admin \
    -p 3306:3306 \
    mysql:5.7
```
- now run the flask app
```
docker run -d \
    --name flask-app \
    --network=twotier \
    -p 5000:5000 \
    -e MYSQL_HOST=mysql \
    -e MYSQL_USER=root \
    -e MYSQL_PASSWORD=admin \
    -e MYSQL_DB=mydb \
    flaskapp:v1
```
- edit the under mysql container
```
docker exec -it mysql bash
```
- login to mysql
```

```
mysql -u root -p
- enter the password `admin`
- create a table
```
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```
- exit mysql
```
exit
```
- exit the container
```