<<<<<<< HEAD
import json
import boto3

def lambda_handler(event, context):
    # Get the regions
    ec2_cli = boto3.client('ec2')
    regions=[region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
    # Itterate over each region
    for region in regions:
        ec2_re = boto3.resource('ec2',region_name=region)
        print("Regions are: ", region)
        # Get only running instances
        instances=ec2_re.instances.filter(Filters=[{'Name':'instance-state-name','Values':['stopped']}])
        for instance in instances:
            instance.start()
=======
import json
import boto3

def lambda_handler(event, context):
    # Get the regions
    ec2_cli = boto3.client('ec2')
    regions=[region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
    # Itterate over each region
    for region in regions:
        ec2_re = boto3.resource('ec2',region_name=region)
        print("Regions are: ", region)
        # Get only running instances
        instances=ec2_re.instances.filter(Filters=[{'Name':'instance-state-name','Values':['stopped']}])
        for instance in instances:
            instance.start()
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
            print("Stopped instances are: ",instance.id)