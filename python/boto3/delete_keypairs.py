import boto3
ec2_cli = boto3.client('ec2')
response = ec2_cli.describe_key_pairs()
for i in response['KeyPairs']:
	print(i['KeyName'])
	ec2_cli.delete_key_pair(KeyName=i['KeyName'])

