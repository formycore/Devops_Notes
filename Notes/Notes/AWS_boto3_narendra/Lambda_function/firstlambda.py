<<<<<<< HEAD
import json
import boto3
def lambda_handler(event, context):
    ec2_re=boto3.resource("ec2","us-east-2")
    for each in ec2_re.instances.all():
=======
import json
import boto3
def lambda_handler(event, context):
    ec2_re=boto3.resource("ec2","us-east-2")
    for each in ec2_re.instances.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
        print(each.id)