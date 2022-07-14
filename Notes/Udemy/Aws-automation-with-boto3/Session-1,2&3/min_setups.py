<<<<<<< HEAD
#!/bin/usr/python
import boto3
# Session
session=boto3.session.Session(profile_name="root")
# ec2 console
session_con_res=session.resource(service_name="ec2",region_name="us-east-2")
sesion_con_cli=session.resource(service_name="ec2",region_name="us-east-2")
# S3 console
s3_con_res=session.resource(service_name="s3",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
	print(each_in.id)


for each_in in ec2_con_re.instances.all():
=======
#!/bin/usr/python
import boto3
# Session
session=boto3.session.Session(profile_name="root")
# ec2 console
session_con_res=session.resource(service_name="ec2",region_name="us-east-2")
sesion_con_cli=session.resource(service_name="ec2",region_name="us-east-2")
# S3 console
s3_con_res=session.resource(service_name="s3",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
	print(each_in.id)


for each_in in ec2_con_re.instances.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each_in.id,each_in.state)