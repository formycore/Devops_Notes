<<<<<<< HEAD
import boto3
import pprint
ec2=boto3.client('ec2')
response=ec2.describe_instances()
for each in response['Reservations']:
    #pprint.pprint(each)
    for each_in in each['Instances']:
=======
import boto3
import pprint
ec2=boto3.client('ec2')
response=ec2.describe_instances()
for each in response['Reservations']:
    #pprint.pprint(each)
    for each_in in each['Instances']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
        pprint.pprint(each_in['ImageId'])