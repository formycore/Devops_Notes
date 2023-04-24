provider "aws" {
  region = "us-east-1"
}
# variable "vpc_cidr" {
#   default = [
#     "10.0.0.0/16", 
#     "10.0.0.0/24"
#     ]
#   // here we have two cidr values 
#   // we are using the for_each loop
# }
# resource "aws_vpc" "main"{
#     for_each = toset(var.vpc_cidr)
#     cidr_block = each.value
#     // here parameter for for_each is each.value
#     //the "for_each" argument must be a map, or set of strings
#     // here for_each = var.vpc_cidr given in the form on list of strings
#     // so we need to change the list of string to set of strings
    
# Now convert the list of strings to map 
variable "vpc_cidr" {
  default = {
    "dev" = "10.0.0.0/16", // this is mapping previous one is list of strings
    "prod" = "10.0.0.0/24"
  }
  // here we have two cidr values 
  // we are using the for_each loop
}
resource "aws_vpc" "main" {
  for_each = var.vpc_cidr
  cidr_block = each.value // here parameter for for_each is each.value
  tags = {
    "Name" = each.key // dev is value and cidr is key
  }
}