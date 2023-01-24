resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc-demo.id

  tags = {
    Name = "igw_demo"
  }
}