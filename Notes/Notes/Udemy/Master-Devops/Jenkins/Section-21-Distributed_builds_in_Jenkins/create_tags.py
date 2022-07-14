<<<<<<< HEAD
import boto3
client = boto3.client('ec2')
response = client.create_tags(
    Resources=['i-0b216f34725c517bc'],
    Tags=[
        {
            'Key':'Name',
            'Value': 'jenkins_slave'
        }
    ]
=======
import boto3
client = boto3.client('ec2')
response = client.create_tags(
    Resources=['i-0b216f34725c517bc'],
    Tags=[
        {
            'Key':'Name',
            'Value': 'jenkins_slave'
        }
    ]
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
)