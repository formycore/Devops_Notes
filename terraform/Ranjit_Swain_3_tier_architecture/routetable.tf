# with vpc a default routetable created
resource "aws_route_table" "rtb" {
   vpc_id = aws_vpc.vpc-demo.id

   route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
   }
   tags = {
     "Name" = "Myroutedemo"
   }
}

# once the route table is crated we need to associate to the subnets
resource "aws_route_table_association" "public" {
  subnet_id = aws_subnet.public-subnet[count.index].id
  route_table_id = aws_route_table.rtb.id
  count = 2
}