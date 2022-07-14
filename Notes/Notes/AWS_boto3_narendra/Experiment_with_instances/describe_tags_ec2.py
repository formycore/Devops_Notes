<<<<<<< HEAD
import boto3
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_tags(
    Filters=[
        {
            'Name': 'resource-type',
            'Values': ['instance']
        },
    ],
)
for each in response['Tags']:
=======
import boto3
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_tags(
    Filters=[
        {
            'Name': 'resource-type',
            'Values': ['instance']
        },
    ],
)
for each in response['Tags']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each['Value'])