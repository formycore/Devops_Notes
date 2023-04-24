variable "region" {
  default = "ap-south-1"
}
variable "ami" {
  default = "ami-06984ea821ac0a879"
}
variable "instance_type" {
  default = "t2.micro"
}
variable "key_name" {
  default = "jan"
}
variable "vpc_cidr" {
  default = "10.10.0.0/16"
}
variable "subnet_cidr" {
  default = "10.10.1.0/24"
}

variable "zone" {
  default = "ap-south-1a"
}