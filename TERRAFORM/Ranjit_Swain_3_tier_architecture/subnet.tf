# here the count is 2 (0,1)
# it will create 2 subnets and 2 cidr blocks
# the first subnet is created under the first availability_zone
# second subnet is created under the second availability_zone
resource "aws_subnet" "public-subnet" {
  vpc_id = aws_vpc.vpc-demo.id # here the vpc id is taken from the vpc.tf file
  # here the vpc-demo is the name of the resource in vpc.tf file
  cidr_block = var.cidr[count.index] # here the var value is taken from variable.tf file
  availability_zone = var.az[count.index] # here the var value is taken from variable.tf file
  count = 2

  tags = {
    Name = "public-sub"
  }
  
}
# for private subnet
resource "aws_subnet" "private-subnet" {
    vpc_id = aws_vpc.vpc-demo.id
    cidr_block = "10.0.3.0/24" # after this success, try to create the two private subnets
    # just like the public subnets
    availability_zone = "ap-south-1b"
    tags = {
        Name = "private-sub"
    }
}