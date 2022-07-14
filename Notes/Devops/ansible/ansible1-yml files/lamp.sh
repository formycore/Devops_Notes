<<<<<<< HEAD
sudo apt-get update
sudo apt-get install apache2 -y
sudo systemctl restart apache2
sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql -y
sudo systemctl restart apache2
echo <?php
phpinfo();
=======
sudo apt-get update
sudo apt-get install apache2 -y
sudo systemctl restart apache2
sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql -y
sudo systemctl restart apache2
echo <?php
phpinfo();
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
?> >> /var/www/html/info.php