az storage blob upload-batch --account-name "" --destination "" --account-key "" --source ""
upload is for the files
upload-batch is for folders
az storage blob update-batch --account-name 
account-name is the storage account name
destination is the container name $web
account-keys is from storage account access keys
source is the folders/files which we need to upload


az storage blob upload-batch --account-name "storageaccountname" --destination "$web" --account-key "storageaccountkey" --source "C:\Users\user\Documents\Notes.md"
az storage blob upload-batch --s /home/maanya/Downloads/css_templates/cake-shop-website-template --d '$web' --account-name awsazmaanya