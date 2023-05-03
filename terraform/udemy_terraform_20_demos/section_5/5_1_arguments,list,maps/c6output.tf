# Terraform Output Values
# ------------------------- Public IP ----------------------------------
# output "instance_public_ip" {
#   description = "Public ip"
#   value = aws_instance.myec2vm.public_ip    
# }
output "for_instance_list" {
  description = "for loop with list"
  value = [for instance in aws_instance.myec2vm: instance.public_ip]
  // here we are looking for the instances aws_instance.myec2vm
  // it does not matter how many are there we will get the public_ip 
  // suppose if we have two aws_instance.myec2vm it will run for 2 times 
  // for the first time aws_instance.myec2vm value will be in instance then we first instance public_ip
  // and for the second time aws_instance.myec2vm value will be in instance then we get the second instance public_ip
  
}
# ---------------------------- Public DNS --------------------------------
output "instance_public_dns" {
  description = "public dns"
  value = aws_instance.myec2vm.public_dns
}
# -------------------------- Private_IP ----------------------------
output "instance_private_ip" {
  value = aws_instance.myec2vm.private_ip
}
# ----------------------- private_dns---------------------------
output "instance_private_dns" {
  value = aws_instance.myec2vm.private_dns
}