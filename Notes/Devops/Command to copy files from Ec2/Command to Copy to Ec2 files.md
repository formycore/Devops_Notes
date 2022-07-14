<<<<<<< HEAD
<pre>
# LOCAL TO REMOTE
scp -i "C:\xxxx\xxxx\xxxx\key.pem" -r chef-repo ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:~
scp -i "C:\xxxx\xxxx\xxxx\key.pem" (folder or file) ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:~

# REMOTE TO LOCAL

scp -i "xxxx.pem" ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:/etc/default/tomcat7 .

=======
<pre>
# LOCAL TO REMOTE
scp -i "C:\xxxx\xxxx\xxxx\key.pem" -r chef-repo ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:~
scp -i "C:\xxxx\xxxx\xxxx\key.pem" (folder or file) ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:~

# REMOTE TO LOCAL

scp -i "xxxx.pem" ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:/etc/default/tomcat7 .

>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
</pre>