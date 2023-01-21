#### https://www.decodingdevops.com/how-to-install-ssm-agent-on-linux-ec2-instance/

# Configure ssm manger
1) Create a new role
2) Choose the service aws ec2
3) Attach the policy AmazonEC2RoleforSSM, AmazonSSMManagedInstanceCore and AmazonSSMFullAccess
4) create a role
5) Attach the role to the instance
## now install ssm agent on the instance

# Install SSM Agent on Amzon Linux
```
#!/bin/bash
sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
sudo start amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent
```
# Install SSM Agent on Ubuntu 18.04 and 16.04
```
#!/bin/bash
mkdir /tmp/ssm
cd /tmp/ssm
wget https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/debian_amd64/amazon-ssm-agent.deb
sudo dpkg -i amazon-ssm-agent.deb
sudo start amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent
```
# Install SSM Agent on Centos 7
```
#!/bin/bash
sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
```

### Now go to the Amazon system manager (ssm)
1) go to run command
2) click on run command
3) select the type of the job <like shell,playbook> 
4) paste the commands over there
```
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
echo "Hello World" > index.html
```
5) click on run
6) go to the instance and check the changes

# Output options
- Enable an S3 bucket
- Choose an S3 bucket name from the list

### Now for the patching
1) go to the ssm
2) go to patch manager
3) click on patch now
     - Patch instances now
     - Patching operation (Scan and install)
     - Instances to patch
     - Patch only the target instances I specify or Patch all instances
4) patch now


### Now for the session manager to connect to instance
- select the instance
- select connect option on the top
- connect 
- it will connected to the instance





























# roughly
    - create a role with ssm full access
    - attach that role to the instance
    - install ssm manager agent on the instance
    - go to ssm to run a command or patch the server


###############################################
aws ssm send-command --document-name "AWS-RunShellScript" --document-version "1" --targets '[{"Key":"InstanceIds","Values":["i-0dfe39f8771d3f760"]}]' --parameters '{"workingDirectory":[""],"executionTimeout":["3600"],"commands":["sudo yum install -y httpd","sudo systemctl start httpd","sudo systemctl enable httpd","cd /var/www/html","echo \"Hello World\" > index.html"]}' --timeout-seconds 60 --max-concurrency "50" --max-errors "0" --output-s3-bucket-name "awsmaanya" --region ap-south-1
####################################################################
