provider "aws" {
  region  = var.region
  profile = "terra"
}
resource "aws_vpc" "demovpc" {
  cidr_block = var.vpc_cidr
  tags = {
    Name = "demovpc"
  }
}
resource "aws_subnet" "demosubnet" {
  vpc_id     = aws_vpc.demovpc.id
  cidr_block = var.subnet_cidr
  availability_zone = var.zone
  

  tags = {
    Name = "demosubnet"
  }
}
// Create Gateway 
resource "aws_internet_gateway" "demogw" {
  vpc_id = aws_vpc.demovpc.id

  tags = {
    Name = "demoigw"
  }
}
// Create Route Table
resource "aws_route_table" "demoroute" {
  vpc_id = aws_vpc.demovpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.demogw.id
  }

  tags = {
    Name = "demort"
  }
}
// Create subnet association
resource "aws_route_table_association" "demosubnetassociatte" {
  subnet_id      = aws_subnet.demosubnet.id
  route_table_id = aws_route_table.demoroute.id
}
// Create Security Group
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.demovpc.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
    tags = {
    Name = "allow_tls"
  }
}
// Create EC2 Instance
resource "aws_instance" "web" {
  ami           = var.ami
  key_name = var.key_name
  instance_type = var.instance_type
  subnet_id = aws_subnet.demosubnet.id
  vpc_security_group_ids = [aws_security_group.allow_tls.id]
  associate_public_ip_address = true

  tags = {
    Name = "HelloWorld"
  }
}