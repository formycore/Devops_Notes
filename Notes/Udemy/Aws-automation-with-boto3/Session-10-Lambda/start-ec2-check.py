<<<<<<< HEAD
import json
import boto3

def lambda_handler(event, context):
    ec2_re=boto3.resource(service_name='ec2',region_name='us-east-2')
    test_env={"Name":"Env:tag","Values":["Testing"]}
    for each_in in ec2_re.instances.filter(Filters=[test_env]):
        each_in.start()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
=======
import json
import boto3

def lambda_handler(event, context):
    ec2_re=boto3.resource(service_name='ec2',region_name='us-east-2')
    test_env={"Name":"Env:tag","Values":["Testing"]}
    for each_in in ec2_re.instances.filter(Filters=[test_env]):
        each_in.start()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
