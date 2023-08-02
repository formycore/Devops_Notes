# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2023.html#install-phpmyadmin-lamp-server-2023

```
sudo yum update -y
sudo yum install install -y httpd wget php-fpm php-mysqli php-json php php-devel -y
sudo yum install -y mariadb105-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo mysql_secure_installation
sudo systemctl start httpd
sudo systemctl enable httpd
```
## To set file permission
```
Add your user (in this case, ec2-user) to the apache group.


[ec2-user ~]$ sudo usermod -a -G apache ec2-user
Log out and then log back in again to pick up the new group, and then verify your membership.

Log out (use the exit command or close the terminal window):


[ec2-user ~]$ exit
To verify your membership in the apache group, reconnect to your instance, and then run the following command:


[ec2-user ~]$ groups
ec2-user adm wheel apache systemd-journal
Change the group ownership of /var/www and its contents to the apache group.


[ec2-user ~]$ sudo chown -R ec2-user:apache /var/www
To add group write permissions and to set the group ID on future subdirectories, change the directory permissions of /var/www and its subdirectories.


[ec2-user ~]$ sudo chmod 2775 /var/www && find /var/www -type d -exec sudo chmod 2775 {} \;
To add group write permissions, recursively change the file permissions of /var/www and its subdirectories:


[ec2-user ~]$ find /var/www -type f -exec sudo chmod 0664 {} \;
```