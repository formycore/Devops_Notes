<<<<<<< HEAD
import boto3
session=boto3.session.Session(profile_name="root")
ec2_re=session.resource('ec2')
for each_in in ec2_re.instances.all():
=======
import boto3
session=boto3.session.Session(profile_name="root")
ec2_re=session.resource('ec2')
for each_in in ec2_re.instances.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print("id: {}".format(instance.id))