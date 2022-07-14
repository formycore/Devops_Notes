<<<<<<< HEAD
import boto3
aws_mgt_con=boto3.session.Session(profile_name="root")
iam_con=aws_mgt_con.resource('iam')
for each_user in iam_con.users.all():
=======
import boto3
aws_mgt_con=boto3.session.Session(profile_name="root")
iam_con=aws_mgt_con.resource('iam')
for each_user in iam_con.users.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
	print(each_user.name)