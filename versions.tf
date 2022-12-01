terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
        version = "3.32.0"
    }
  }
  required_version = ">= 0.13"
}


provider "azurerm" {
  subscription_id = var.subscription_id
  features {}
}
