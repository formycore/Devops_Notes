<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
ec2_regions = [region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
print(len(ec2_regions))
=======
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
ec2_regions = [region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
print(len(ec2_regions))
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(ec2_regions)