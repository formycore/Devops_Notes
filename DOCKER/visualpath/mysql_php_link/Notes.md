# Link mysql and phpadmin 
-- MYSQL_ROOT_HOST=%
For example, the value 172.17.0.1, which is the default Docker gateway IP, allows connections from the host machine that runs the container. The option accepts only one entry, but wildcards are allowed (for example, MYSQL_ROOT_HOST=172.*.*.* or MYSQL_ROOT_HOST=%).

docker container run -d --name mysql --hostname mysqldbserver -e MYSQL_ROOT_PASSWORD=test1234 -e MYSQL_ROOT_HOST=% mysql:5.7