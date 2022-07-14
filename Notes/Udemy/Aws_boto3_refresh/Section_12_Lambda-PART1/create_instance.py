<<<<<<< HEAD
import boto3
ec2_cli = boto3.client('ec2')
resp = ec2_cli.run_instances(
							ImageId="ami-0affd4508a5d2481b",
							InstanceType="t2.micro",
							MinCount=1,
							MaxCount=1,
							TagSpecifications=[
							{
							'ResourceType': 'instance',
							'Tags':[
							{
							'Key':'Name',
							'Value':'with_python'
							}]
							}
							]
	                        )
for instance in resp['Instances']:
=======
import boto3
ec2_cli = boto3.client('ec2')
resp = ec2_cli.run_instances(
							ImageId="ami-0affd4508a5d2481b",
							InstanceType="t2.micro",
							MinCount=1,
							MaxCount=1,
							TagSpecifications=[
							{
							'ResourceType': 'instance',
							'Tags':[
							{
							'Key':'Name',
							'Value':'with_python'
							}]
							}
							]
	                        )
for instance in resp['Instances']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
	print(instance['InstanceId'])