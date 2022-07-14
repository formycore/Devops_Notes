<<<<<<< HEAD
import boto3
from pprint import pprint
region = input ("Enter the region name:")
ec2_cli = boto3.client('ec2',region_name=region)
response = ec2_cli.describe_instances()['Reservations']
for each_in in response:
    for each in each_in['Instances']:
        pprint(each)    
=======
import boto3
from pprint import pprint
region = input ("Enter the region name:")
ec2_cli = boto3.client('ec2',region_name=region)
response = ec2_cli.describe_instances()['Reservations']
for each_in in response:
    for each in each_in['Instances']:
        pprint(each)    
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
