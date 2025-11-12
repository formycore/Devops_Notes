# choose aws rds for postgres 
- first create an aws rds instance for postgres
- make sure to set the vpc security group to allow inbound traffic on port 5432
- note the endpoint, port, username, and password for the rds instance
- public access is not required if the ec2 instance is in the same vpc
- like both the vpc for ec2 and rds should be the same
- ec2 and aws rds should have same security group
- add the posrtgres port 5432 to the security group inbound rules
- db subnet group create new
- additional configuration set to default
- maintaince not needed 
- 
# connect to aws rds from ec2 instance
- ssh into your ec2 instance
- install the postgres client if not already installed
  ```bash
  sudo apt-get update
  sudo apt-get install postgresql-client
  ```
- use the psql command to connect to the rds instance
  ```bash
  psql --host=<rds-endpoint> --port=<rds-port> --username=<rds-username> --password --dbname=<rds-dbname>
  ```
- enter the password when prompted
- you should now be connected to the postgres database on the rds instance
# troubleshooting
- if you cannot connect, check the following:
  - ensure the rds instance is in a public subnet or has a proper route to the ec2 instance
  - verify the security group rules for both the rds and ec2 instances
  - check the rds instance status to ensure it is available