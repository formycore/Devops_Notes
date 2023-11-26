import boto3
ec2_console = boto3.client('ec2')
response = ec2_console.start_instances(
    InstanceIds = ['i-010c868943eb9fcd9']
)

