<<<<<<< HEAD
import boto3
session=boto3.session.Session(profile_name="root")
iam_group_cli=session.client(service_name="iam",region_name="us-east-2")
for each_grp in iam_group_cli.list_groups()['Groups']:
=======
import boto3
session=boto3.session.Session(profile_name="root")
iam_group_cli=session.client(service_name="iam",region_name="us-east-2")
for each_grp in iam_group_cli.list_groups()['Groups']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
	print ("Group Name={}\nGroup ID={}".format(each_grp['GroupName'],each_grp['GroupId']))