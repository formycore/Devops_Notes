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

resource "azurerm_resource_group" "mtc-rg" {
    name = "mtc-resources"
    location = "East Us"
    tags = {
        environment = "dev"
    }
}