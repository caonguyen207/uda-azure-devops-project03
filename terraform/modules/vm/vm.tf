data "azurerm_shared_image" "test" {
  name                = "linux-image"
  gallery_name        = "testgallery"
  resource_group_name = "${var.resource_group}"
}

resource "azurerm_network_interface" "test" {
  name                = "nic-1"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "linux-vm-2"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS1_v2"
  admin_username      = "azureuser"
  network_interface_ids = [azurerm_network_interface.test.id]

  # For Azure pipeline, uncomment below part when testing in localhost
  admin_password = "Azureadmin@123"
  disable_password_authentication = false
  
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
