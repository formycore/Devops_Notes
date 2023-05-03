#Input Variables
# ------------------------------AWS Region------------------------------
variable "aws_region" {
  description = "Region in which resource will be created"
  type        = string
  default     = "us-east-1"
}
# ------------------------------EC2 instance type------------------------------
variable "instance_type" {
  type    = string
  default = "t2.micro"
  // if we want to give password input we use sensitive =true 
}
#------------------------------EC2 Key pair ------------------------------
variable "instance_keypair" {
  type    = string
  default = "april"

}