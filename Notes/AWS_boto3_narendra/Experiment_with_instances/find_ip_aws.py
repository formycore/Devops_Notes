<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2',region_name='us-east-1')
response=ec2_cli.describe_instances()['Reservations']
for each in response:
    for each_in in each['Instances']:
        for each_tags in each_in['Tags']:
            print("=====================")
            print("The instance id is: {}\nThe Instance State is : {}\nThe Public Ip: {}\nThe Instance tag value: {}".format(each_in['InstanceId'],
                                                                                                                             each_in['State']['Name'],
                                                                                                                             each_in['PublicDnsName'],
=======
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2',region_name='us-east-1')
response=ec2_cli.describe_instances()['Reservations']
for each in response:
    for each_in in each['Instances']:
        for each_tags in each_in['Tags']:
            print("=====================")
            print("The instance id is: {}\nThe Instance State is : {}\nThe Public Ip: {}\nThe Instance tag value: {}".format(each_in['InstanceId'],
                                                                                                                             each_in['State']['Name'],
                                                                                                                             each_in['PublicDnsName'],
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
                                                                                                                             each_tags['Value']))