<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
resp = ec2_cli.describe_instances()['Reservations']
#pprint(resp)
for each_item in resp:
    pprint(each_item['NetworkInterfaces'])
    #for each_item_list in each_item['NetworkInterfaces']:
        #pprint(each_item_list)
        #pprint(each_item_list['InstanceId'])
        #print(each_item)
        
=======
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
resp = ec2_cli.describe_instances()['Reservations']
#pprint(resp)
for each_item in resp:
    pprint(each_item['NetworkInterfaces'])
    #for each_item_list in each_item['NetworkInterfaces']:
        #pprint(each_item_list)
        #pprint(each_item_list['InstanceId'])
        #print(each_item)
        
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
