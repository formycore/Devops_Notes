'''
install wordpress and mysql two containers
tis is wordpress official docker image
# https://hub.docker.com/_/wordpress
in the website the main thing we need is

-e WORDPRESS_DB_HOST=...
-e WORDPRESS_DB_USER=...
-e WORDPRESS_DB_PASSWORD=...
-e WORDPRESS_DB_NAME=...
-e WORDPRESS_TABLE_PREFIX=...



---------------------------------------------------
this is mysql official docker image 
# https://hub.docker.com/_/mysql

Env variables
MYSQL_ROOT_PASSWORD
MYSQL_DATABASE
MYSQL_USER, MYSQL_PASSWORD


here we using root username and root password with seperate database wordpress

## how to set a hostname for the container
-------------------------------------------------
# MYSQL_ROOT_HOST means whom you want to allow 
# give '%' as per /etc/host file
docker container run -d \
--name mysql-db \
-e MYSQL_ROOT_PASSWORD=test1234 \
-e MYSQL_DATABASE=wordpress \
-e MYSQL_ROOT_HOST='%' \
mysql
-------------------------------------------
# install mysql client on the host machine on amazon linux
# https://thomasstep.com/blog/installing-the-mysql-cli-on-an-ec2-instance
sudo yum install -y https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
sudo yum install -y mysql-community-client
mysql -u MY_USER -p`MY_PASSWORD` -h MY_HOST -P 3306
-------------------------------------------
- as this is the first container so basically the first ip of the container is 172.17.0.2
- mysql -h 172.17.0.2 -u root -p (enter)
- show databases;
- use wordpress;
- show tables;
- \q

----------------------------------------------------------------
# here the host is the ip of the mysql container
docker container run -d \
--name wordpress \
-e WORDPRESS_DB_HOST=172.17.0.2 \
-e WORDPRESS_DB_USER=root \
-e WORDPRESS_DB_PASSWORD=test1234 \
-e WORDPRESS_DB_NAME=wordpress \
-p 8090:80 \
wordpress





'''