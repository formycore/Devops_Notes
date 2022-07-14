<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_instances()['Reservations']
for each_item in response:
	for each_ins in each_item['Instances']:
		print("======================")
		print("The Image id is: {}\nThe instance id is : {}\nThe Launch time is: {}".format(each_ins['ImageId'],
																						 each_ins['InstanceId'],
																						 each_ins['LaunchTime'].strftime("%Y-%m-%d")))
		print("======================")
=======
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_instances()['Reservations']
for each_item in response:
	for each_ins in each_item['Instances']:
		print("======================")
		print("The Image id is: {}\nThe instance id is : {}\nThe Launch time is: {}".format(each_ins['ImageId'],
																						 each_ins['InstanceId'],
																						 each_ins['LaunchTime'].strftime("%Y-%m-%d")))
		print("======================")
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
		