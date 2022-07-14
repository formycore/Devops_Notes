<<<<<<< HEAD
import boto3
ec2_re=boto3.resource('ec2')
# it will print all the availability snapshots around the aws
'''for each in ec2_re.snapshots.all():
    print(each)
'''
sts_cli=boto3.client('sts')
response=sts_cli.get_caller_identity()
print(response.get('Account'))
my_account=response.get('Account')
for each in ec2_re.snapshots.filter(OwnerIds=[my_account]):
=======
import boto3
ec2_re=boto3.resource('ec2')
# it will print all the availability snapshots around the aws
'''for each in ec2_re.snapshots.all():
    print(each)
'''
sts_cli=boto3.client('sts')
response=sts_cli.get_caller_identity()
print(response.get('Account'))
my_account=response.get('Account')
for each in ec2_re.snapshots.filter(OwnerIds=[my_account]):
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each)