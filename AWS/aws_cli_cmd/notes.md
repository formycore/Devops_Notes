# list of commands for the aws cli
 1410  aws ec2 describe-key-pairs
 1411  aws configure
 1412  aws describe-key-pairs
 1413  aws ec2 describe-key-pairs
 1414  aws ec2 describe-security-groups
 1415  aws configure
 1416  aws ec2 describe-security-groups
 1417  aws ec2 describe-security-groups --query "SecurityGroups[*].GroupName"
 1418  aws ec2 run-instances --image-id ami-xxxxxxxd63afc18 --instance-type t2.micro --key-name mumbai_april --security-groups allow_all 
 1419  aws ec2 describe-instances --filters "Name=docker_test,Values=running"
 1420  aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"
 1421  aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[]"
 1422  aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].{ID:InstanceID}"
 1423  aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].{ID:InstanceId}"
 1424  aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].{ID:InstanceId,Type:InstanceType,State:State.Name}"
 1425  aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].{ID:InstanceId,PrivateIP:PrivateIpAddress,PublicIP:PublicIpAddress}" --output table
 1426  aws stop-instances i-01bd716eabdbd09b6
 1427  aws ec2 stop-instances --instance-ids i-01bd716eabdbd09b6
