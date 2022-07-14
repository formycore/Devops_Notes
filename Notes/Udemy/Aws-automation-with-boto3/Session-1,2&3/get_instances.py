<<<<<<< HEAD
import boto3
session=boto3.session.Session(profile_name="root")
# session is a variable
# session_IAM=boto3.session.Session(profile_name="any_name")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
    print(each_in.id,each_in.state)
=======
import boto3
session=boto3.session.Session(profile_name="root")
# session is a variable
# session_IAM=boto3.session.Session(profile_name="any_name")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
    print(each_in.id,each_in.state)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
