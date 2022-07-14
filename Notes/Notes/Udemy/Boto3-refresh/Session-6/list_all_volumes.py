<<<<<<< HEAD
import boto3
ec2=boto3.resource('ec2',region_name='us-east-2')

for each_vol in ec2.volumes.filter(
                                Filters=[{'Name': 'status', 'Values': ['available']}]
                                ):
                                print(each_vol)

=======
import boto3
ec2=boto3.resource('ec2',region_name='us-east-2')

for each_vol in ec2.volumes.filter(
                                Filters=[{'Name': 'status', 'Values': ['available']}]
                                ):
                                print(each_vol)

>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
