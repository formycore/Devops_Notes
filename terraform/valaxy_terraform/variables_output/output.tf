output "public-ip" {
  description = "this for public ip"
  value = aws_instance.web.public_ip
}
output "private-ip" {
  description = "this is for private ip"
  value = aws_instance.web.private_ip
}