<<<<<<< HEAD
#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
iam_re=session.resource("iam","us-east-2")
for each_iam_usr in iam_re.users.all():
=======
#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
iam_re=session.resource("iam","us-east-2")
for each_iam_usr in iam_re.users.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print("User Name:{}\nUser ID:{}\nUser Create Date:{}".format(each_iam_usr.user_name,each_iam_usr.user_id,each_iam_usr.create_date))