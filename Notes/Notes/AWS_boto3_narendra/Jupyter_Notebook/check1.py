<<<<<<< HEAD
from collections import defaultdict
from pprint import pprint
import boto3
ec2_re=boto3.resource('ec2')
running_instances=ec2_re.instances.filter(Filters=[{'Name': 'instance-state-name','Values':['stopped']}])
ec2_info=defaultdict()
for instances in running_instances:
    for tags in instances.tags:
=======
from collections import defaultdict
from pprint import pprint
import boto3
ec2_re=boto3.resource('ec2')
running_instances=ec2_re.instances.filter(Filters=[{'Name': 'instance-state-name','Values':['stopped']}])
ec2_info=defaultdict()
for instances in running_instances:
    for tags in instances.tags:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
        print(tags)