# AWS RDS with Docker

## AWS RDS Setup

- Create a database
- Choose the version of any DB
- Set the instance type and storage
- Set the VPC and subnet group
- Set the security group to allow inbound traffic on the DB port
- Set the username and password
- Note the endpoint, port, username, and password for the DB instance
- Public access is not required if the EC2 instance is in the same VPC
- Public access is required if the EC2 instance is in a different VPC
- Create DB in a new security group
- Add the DB port to the security group inbound rules
- DB subnet group: create new
- Additional configuration: set to default
- Here we have created the MySQL DB with new security group
- Go to that security group and add custom rules to allow anywhere access 


## AWS EC2 Setup

- Create an EC2 instance in the same VPC as the DB instance
- Assign a different security group to the EC2 instance
- Add inbound rule to EC2 security group to allow outbound traffic on the DB port
- SSH into your EC2 instance
- Install the DB client if not already installed:

```bash
sudo yum install mariadb105
```

- Connect to the RDS instance:

```bash
mysql -h <rds-endpoint> -P 3306 -u admin -p
```

Replace `<rds-endpoint>` with your actual RDS endpoint


**Docker**
```
- docker image philippaul/node-mysql-app:02
- docker run -p 80:3000 \
     --name node-mysql-app \
    -e DB_HOST=<rds-endpoint> \
    -e DB_PORT=<rds-port> \
    -e DB_USER=<rds-username> \
    -e DB_PASSWORD=<rds-password> \
    -d philippaul/node-mysql-app:02
```

```


## Docker Setup

### Docker Image Variables

```bash
docker run -p 80:3000 \
  --name node-mysql-app \
  -e DB_HOST=<rds-endpoint> \
  -e DB_PORT=<rds-port> \
  -e DB_USER=<rds-username> \
  -e DB_PASSWORD=<rds-password> \
  -d philippaul/node-mysql-app:02
```

### Docker Example with Real Values

```bash
docker run -p 80:3000 \
  --name node-mysql-app \
  -e DB_HOST=database-1.12345666.us-east-1.rds.amazonaws.com \
  -e DB_USER=admin \
  -e DB_PASSWORD=password123 \
  -d philippaul/node-mysql-app:02
```

### Connect to MySQL in Docker

```bash
docker run -it mysql:8.0 mysql -h database-1.12345666.us-east-1.rds.amazonaws.com -u admin -p
```

### MySQL Commands

```sql
show databases;
use my_app_db;
show tables;
select * from contacts;
```

