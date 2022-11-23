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
# here we are creating the subnet into the virtual network
# with this we have ip address used for virtual machines
# azurerm_subnet check into it
resource "azurerm_subnet" "mtc_subnet" {
    name = "mtc_subnet"
    resource_group_name = azurerm_resource_group.mtc_rg.name
    virtual_network_name = azurerm_virtual_network.mtc_vn.name
    address_prefixes = ["10.0.1.0/24"] 

}