# Terraform Output Values
# ------------------------- Public IP ----------------------------------
output "instance_public_ip" {
  description = "Public ip"
  value = aws_instance.myec2vm.public_ip    
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