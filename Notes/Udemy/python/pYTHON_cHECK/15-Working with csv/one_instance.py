<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
for each_in in ec2_cli.describe_instances()['Reservations']:
    for each_ins in each_in['Instances']:
        print(each_ins)
        print("---------")
=======
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
for each_in in ec2_cli.describe_instances()['Reservations']:
    for each_ins in each_in['Instances']:
        print(each_ins)
        print("---------")
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    break