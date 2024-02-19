import boto3
ec2_cli = boto3.client('ec2')
response = ec2_cli.create_key_pair(KeyName='January')
print(response['KeyMaterial'])

with open("January.pem", 'w') as f:
	f.write(response['KeyMaterial'])