import boto3
ec2_cli = boto3.client('ec2')
response = ec2_cli.describe_key_pairs()
#print(response['KeyPairs'])
for i in response['KeyPairs']:
	print(i['KeyName'])