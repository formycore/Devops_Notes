<<<<<<< HEAD
import json
import boto3

def lambda_handler(event, context):
    ec2_re=boto3.resource('ec2')
    for each_in in ec2_re.instances.filter(Filters=[{"Name":"tag:Env","Values":["test"]}]):
    	print(each_in)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
=======
import json
import boto3

def lambda_handler(event, context):
    ec2_re=boto3.resource('ec2')
    for each_in in ec2_re.instances.filter(Filters=[{"Name":"tag:Env","Values":["test"]}]):
    	print(each_in)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
