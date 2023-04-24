echo "Installing apache"
sudo yum install httpd -y
sudo systemctl enable httpd 
sudo systemctl start httpd
sudo systemctl status httpd
sudo httpd -v
