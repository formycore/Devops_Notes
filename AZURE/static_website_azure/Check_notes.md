# How to Upload Batch Files to Azure Storage Account Using Azure CLI
## Uploading Bulk Files to Azure Storage Account
- Active Azure Subscription. If you don’t one, you can sign up here
- Azure CLI for Windows. You can download and install Azure CLI for Windows here
- Azure Storage Account with $web container created
- Clone or download a free website template and store the folder in the Desktop location on your PC
###  Step 1 – Login into Azure Portal via Azure CLI for Windows
```az login```
### Step 2 – Create Azure Resources such as Resource Group and Azure Storage Account
- Create a Resource Group which is a logical folder where resources on Azure are stored. To create a Resource Group using the Azure CLI, run:
```az group create --name myResourceGroup --location westus```
- The next thing is to create an Azure Storage Account. To do so, run:
```az storage account create --name <unique_name> --resource-group <resource-group>  --location <westus> --sku Standard_LRS --kind StorageV2```
### Step 3 – Enable static website hosting for your storage account
- Before you can run a static website on your Azure Storage Account you must first of all enable the static website hosting feature for the blob storage. To do so, run:
```az storage blob service-properties update --account-name $StorageAccountName --static-website --index-document index.html```
### Step 4 – Upload website folders from the local path
- To upload the website folders from the local path to the Azure Storage Account, run:
```az storage blob upload-batch -s $LocalPath -d '$web' --account-name $StorageAccountName```
-  --source <-s>
- --destination <-d>
### Step 5 – Display the website URL
```az storage account show -n $StorageAccountName --resource-group $ResourceGroup --query "primaryEndpoints.web" --output tsv```
# ------------------------------------------------------------------------------------------------------------------------------ #
# Clean up Azure Resources
``` az group delete --resource-group <ResourceGroupName> ```



