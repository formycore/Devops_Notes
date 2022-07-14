<<<<<<< HEAD
#!/usr/bin/python
import boto3
#session=boto3.session.Session(profile_name="root")
#ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
ec2_con_re=boto3.resource(service_name="ec2",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
=======
#!/usr/bin/python
import boto3
#session=boto3.session.Session(profile_name="root")
#ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
ec2_con_re=boto3.resource(service_name="ec2",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print each_in