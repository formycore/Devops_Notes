# Terraform settings Block
terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 4.0"
        }
    }
}
# providers Block
provider "aws" {
    profile = "default" # while aws configure we need to mention the profile name
    region = "us-east-1"
}

# Resource Block
resource "aws_instance" "ec2_demo" {
    ami = "ami-053b0d53c279acc90" # ami varies from regions to os images # for us-east-1
    instance_type = "t2.micro" # machine type
    # here we need to add the app1-install.sh, we use file function to read the content of the file
    # we need to create a file in the same directory with the name app1-install.sh
    user_data = file("${path.module}/app1-install.sh")
    tags = {
        "Name" = "ec2-demo"
    }

    
}