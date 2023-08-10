# Availabilty zones data source
data "aws_availability_zones" "my_azones" {
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}
# names - List of the Availability Zone names available to the account
# data.aws_availability_zones.my_azones.names -- it will list all the names of AZs in the region
# Ec2 instance
resource "aws_instance" "myec2vm" {
  ami = data.aws_ami.amzlinux2.id
  instance_type = var.instance_type
  #instance_type = var.instance_type_list[1]  # For List
  #nstance_type = var.instance_type_map["prod"]  # For Map
  user_data = file("${path.module}/app1-install.sh")
  key_name = var.instance_keypair
  vpc_security_group_ids = [ aws_security_group.vpc-ssh.id, aws_security_group.vpc-web.id   ]
  # count = 2
  # tags = {
  #   "Name" = "Count-Demo-${count.index}"
  # }
  for_each = toset(data.aws_availability_zones.my_azones.names)
  availability_zone = each.key
  tags = {
    "Name" = "AZ-Demo-${each.key}"
  }
 

}
