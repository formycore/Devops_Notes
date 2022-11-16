terraform {
  required_version = ">= 0.12"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
  }

}
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "mtc_rg" {
  name     = "mtc-resources"
  location = "East Us"
  tags = {
    environment = "dev"
  }
}

resource "azurerm_virtual_network" "mtc_vn" {
    name = "mtc-network"
    resource_group_name = azurerm_resource_group.mtc_rg.name
    location = azurerm_resource_group.mtc_rg.location
    address_space = ["10.0.0.0/16"] # same as the CIDR ranges in the aws

    tags = {
        environment = "dev"
    }
}