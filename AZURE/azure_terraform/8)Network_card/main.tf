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
# Now we are looking for security group
# azurerm _network_security_group
resource "azurerm_network_security_group" "mtc_security_group" {
    name = "mtc_security_group"
    location = azurerm_resource_group.mtc_rg.location
    resource_group_name = azurerm_resource_group.mtc_rg.name

    tags = {
        environment = "dev"
    }
}
# here we can add security_group rules 
# but here we are taking the new "azure_network_security_rule"
resource "azurerm_network_security_rule" "mtc_sg_rule" {
    # mtc_security_group_rule
  name                        = "mtc_sg_rule"
  priority                    = 100
  # if we have more rule then we have to change the priority 
  direction                   = "Inbound"
  # here we are trying to inward traffic to our instances with subnets
  access                      = "Allow"
  protocol                    = "*"
  # By default the protocol is TCP but with * we can use any ICMP or anything else
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  # we can edit the source_address_prefix to our ip address
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.mtc_rg.name
  network_security_group_name = azurerm_network_security_group.mtc_security_group.name
}
## here we are associating the security_group with subnets
# azurerm_subnet_network_security_group_association
resource "azurerm_subnet_network_security_group_association" "mtc_sga" {
    subnet_id = azurerm_subnet.mtc_subnet.id
    network_security_group_id = azurerm_network_security_group.mtc_security_group.id
}
# after this go to the console
# mtc_security_group is associated with Subnets <mtc_subnet>
#################
# Here we are talking about the public ip 
resource "azurerm_public_ip" "mtc_public_ip" {

    name="acceptanceTestPublicIp1"
    # here we are giving the name to the public ip
    # we can give any name, but it should be unique
    # 
    # we might name as to be something dynamic 
    # if we deploy multiple, if it is dynamic then it wont overlap
    resource_group_name = azurerm_resource_group.mtc_rg.name
    location = azurerm_resource_group.mtc_rg.location
    allocation_method = "Dynamic"
    # for static we have to pay
    # after we terraform plan, we get the public ip address = after apply
    # but it does not show in the console
    # to view the public ip it has to attach to some thing like instance
    tags = {
        environment = "dev"

    }
}
# after this <terraform state list>
# terraform state show <resource>
#############################
# here we will create the network interface that we attach to the instance in order to provide the network connectivity
# this NIC receives the public ip address from the public ip resource
resource "azurerm_network_interface" "mtc_nic" {
    name = "mtc_nic"
    location = azurerm_resource_group.mtc_rg.location
    resource_group_name = azurerm_resource_group.mtc_rg.name
    ip_configuration {
        name = "internal"
        subnet_id = azurerm_subnet.mtc_subnet.id
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id = azurerm_public_ip.mtc_public_ip.id
    }

    tags = {
        environment = "dev"
    }
}