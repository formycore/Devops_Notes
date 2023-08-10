# Terraform Block
terraform {
  required_version = "~> 0.15"
  required_providers {
    aws = {
        source  = "hashicorp/aws"
        version = "~> 3.0.0"
    }
  }
}


# provider block
provider "aws" {
  region = var.aws_region
}
#required_version = "~> 0.15" should be checked with terraform verison 
# - then change the required_version to the terraform version 