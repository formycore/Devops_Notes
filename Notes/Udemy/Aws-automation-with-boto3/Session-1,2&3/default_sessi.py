<<<<<<< HEAD
#!/bin/usr/python
import boto3
ec2_con_re=boto3.resource('ec2','us-east-2')
for each_in in ec2_con_re.instances.all():
=======
#!/bin/usr/python
import boto3
ec2_con_re=boto3.resource('ec2','us-east-2')
for each_in in ec2_con_re.instances.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
	print(each_in.id)