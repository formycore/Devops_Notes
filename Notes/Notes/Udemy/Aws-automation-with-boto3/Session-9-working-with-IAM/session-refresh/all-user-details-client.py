<<<<<<< HEAD
#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
iam_cli=session.client("iam","us-east-2")
# in client we have to use dictionary operations
for each_user in iam_cli.list_users()['Users']:
=======
#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
iam_cli=session.client("iam","us-east-2")
# in client we have to use dictionary operations
for each_user in iam_cli.list_users()['Users']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print("User Name:{}\nUser ID:{}".format(each_user['UserName'],each_user['UserId']))