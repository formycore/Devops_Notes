# https://www.youtube.com/watch?v=B3BtmyBetQo&t=2s
# Resource needed to be craeted
- custom vpc
    - aws_vpc
- 2 public subnet
    - aws_subnet
- 1 private subnet
- 2 EC2 instances
    - aws_instance
- Security group
    - aws_security_group
- Elastic IP
    - aws_eip
- NAT gateway
    - aws_nat_gateway
- Internet gateway
    - aws_internet_gateway
- Route table
    - aws_route_table
    - aws_route_table_association
- APplication load balancer
- Apache web server
- MYSQL database
# THROUGH NAT GATEWAY WE GIVE INTERNET ACCESS TO THE PRIVATE SUBNET


-- check the ami ami-08df646e18b182346
which ami instance is this ami-08df646e18b182346 ?
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html