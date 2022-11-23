### Terraform tfstate and tfstate backup files
these are stored in the another path like
- aws s3
- terraform cloud
### to see the all of the resources we have
terraform state list
### to view more info the state files 
terraform state show <any one of the list files>
### to view the full show of the state files
terraform show - this will show the all of the resources
terraform state show - this will show only the resources
### to destroy the resources
terraform destroy - this will destroy the all of the resources
terraform plan -destroy 
terraform apply -destroy
### to destroy the specific resource
terraform destroy -target=<resource name>



- so we have tfstate and tfsate backup files,if we edit or delete the tfstate file then we can't get the resources back,so we have to take the backup of the tfstate file for that reason we have tfstate.backup file

- next part starts from https://www.youtube.com/watch?v=V53AHWun17s&list=PLB97yPrFwo5jXUZ5ZaBDVqZDnJQVwYsDL&index=4

