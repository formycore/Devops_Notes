# Create the Security group -- SSH traffic
resource "aws_security_group" "vpc_ssh" {
  name = "vpc_ssh"
  // vpc_id = as we going to put this in default vpc we dont need to mention
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] // allowing from entire internet
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] // allowing from entire internet
  }
  tags = {
    "Name" = "vpc-ssh"
  }
}
# Create Security group -- web traffic
resource "aws_security_group" "vpc-web" {
  name = "vpc-web"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }
  ingress { // for adding another ingress rule
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] // allowing from entire internet
  }
  tags = {
    "Name" = "vpc-web"
  }
}