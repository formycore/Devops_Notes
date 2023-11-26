import boto3
ec2_console = boto3.client('ec2')
response = ec2_console.describe_instances()
for reservations in response[Reservations]:
    print(reservations)