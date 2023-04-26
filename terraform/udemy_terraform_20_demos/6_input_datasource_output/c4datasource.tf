# 679593333241  account ID belongs to the official CentOS Amazon Machine Image (AMI) 
data "aws_ami" "centos" {
  most_recent = true
  owners      = ["679593333241"]

  filter {
    name   = "name"
    values = ["CentOS 7*"]
    // when we search for the centos 7 image in the aws market place we get the name as CentOS 7*
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}
# it can called with data.aws_ami.centos.id
