resource "aws_vpc" "vpc-demo" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "vpc-demo"
  }
}
