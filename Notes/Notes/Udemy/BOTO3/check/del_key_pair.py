<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
key_pairs=[]
for each in ec2_cli.describe_key_pairs()['KeyPairs']:
	key_pairs.append(each['KeyName'])
print(key_pairs)	
key_pairs.remove('samdevops')
for each_key in key_pairs:
	response=ec2_cli.delete_key_pair(KeyName=each_key)
=======
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
key_pairs=[]
for each in ec2_cli.describe_key_pairs()['KeyPairs']:
	key_pairs.append(each['KeyName'])
print(key_pairs)	
key_pairs.remove('samdevops')
for each_key in key_pairs:
	response=ec2_cli.delete_key_pair(KeyName=each_key)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(response)	