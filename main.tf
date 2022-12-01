
resource "azurerm_resource_group" "example" {
  name     = var.name_azurerm_resource_group
  location = "eastus"
  tags = {
    ambiente_implementacion = var.tags_grupo_de_recursos_ambiente
    fecha_implementaicon = var.tags_grupo_de_recursos_fecha_implementaicon
  } 
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-appserviceplan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  kind                = "Windows"
  

  sku {
    tier = "Standard"
    size = "B1"
  }
  
  tags = azurerm_resource_group.example.tags
}

resource "azurerm_app_service" "example" {
  name                = "exampleappservice"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
  https_only          = true
  
  
  site_config {
    linux_fx_version = ".NET|6.0"
    dotnet_framework_version = "v6.0"
    min_tls_version     = 1.2
    
  }
  
  tags = azurerm_resource_group.example.tags
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageaccount"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"

  tags = azurerm_resource_group.example.tags
}

resource "azurerm_sql_server" "example" {
  name                         = "examplemssqlserver"
  resource_group_name          = azurerm_resource_group.example.name
  location                     = azurerm_resource_group.example.location
  version                      = "12.0"
  administrator_login          = "admin"
  administrator_login_password = "Evolution2022"

  tags = azurerm_resource_group.example.tags
}

resource "azurerm_sql_database" "example" {
  name                = "examplesqldatabase"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  server_name         = azurerm_sql_server.example.name
  collation           = "SQL_LATIN1_GENERAL_CP1_CI_AS"
  edition             = "Standard"
  administrator_login          = "admin"
  administrator_login_password = "Evolution2022"
  authentication_type  = "SQL"
  

  tags = azurerm_resource_group.example.tags
}