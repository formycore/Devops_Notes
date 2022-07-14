<<<<<<< HEAD
#!/bin/usr/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_cli=session.client(service_name="ec2",region_name="us-east-2")
print dir(ec2_con_cli)


#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_console_resource=session.resource(service_name="ec2",region_name="us-east-2")
print dir(ec2_console_resource)
=======
#!/bin/usr/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_cli=session.client(service_name="ec2",region_name="us-east-2")
print dir(ec2_con_cli)


#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_console_resource=session.resource(service_name="ec2",region_name="us-east-2")
print dir(ec2_console_resource)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
