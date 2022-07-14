<<<<<<< HEAD
import boto3
ec2_re=boto3.resource('ec2')
response=ec2_re.instances.all()
#print(response)
for each in response:
    print(each.tags)
=======
import boto3
ec2_re=boto3.resource('ec2')
response=ec2_re.instances.all()
#print(response)
for each in response:
    print(each.tags)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each.instance_id)