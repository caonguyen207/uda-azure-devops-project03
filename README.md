
# Overview

For Udacity Azure DevOps Project 3 submission!

# Getting Started

1. Change the value in `terraform\environments\test\terraform.tfvars`
2. Create testing VM and expose as Gallery

```shell
Azure compute gallery:testgallery
Target VM image definition: linux-image
Version number: 0.0.1
```

3. Run command to create Azure pipeline agent

```shell
az vm create --resource-group Azuredevops --name my-agent-1 --image Ubuntu2204 --size Standard_DS1_v2 --data-disk-sizes-gb 20 --admin-username devopsagent --admin-password DevOpsAgent@123 --nsg-rule SSH --public-ip-sku Standard
```
4. Create Azure DevOps Org and connect agent
5. Create empty Environment named `test`
6. Install TFIntaller into your DevOps organization `https://marketplace.visualstudio.com/items?itemName=JasonBJohnson.azure-pipelines-tasks-terraform`
7. Run command to create SA, it will use to store TF state.
`./configure-tfstate-storage-account.sh`
8. Replace SA name and access key in `terraform\environments\test\main.tf`
9. Install JDK 8 in Azure pipeline agent.

Need install zip/unzip in agent
The google-chrome and chrome driver must be same in order to pass selenium test.
[Installation](https://skolo.online/documents/webscrapping/#step-1-download-chrome)
