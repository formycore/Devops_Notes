<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
for each in ec2_cli.describe_instances()['Reservations']:
	for each_in in each['Instances']:
=======
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
for each in ec2_cli.describe_instances()['Reservations']:
	for each_in in each['Instances']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
		pprint(each_in)