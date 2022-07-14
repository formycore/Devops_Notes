<<<<<<< HEAD
import boto3
session=boto3.session.Session(profile_name="root")
iam_cli=session.client(service_name="iam",region_name="us-east-2")
for user in iam_cli.list_users()['Users']:
 print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
 user['UserName'],
 user['UserId'],
 user['Arn'],
 user['CreateDate']
 )
=======
import boto3
session=boto3.session.Session(profile_name="root")
iam_cli=session.client(service_name="iam",region_name="us-east-2")
for user in iam_cli.list_users()['Users']:
 print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
 user['UserName'],
 user['UserId'],
 user['Arn'],
 user['CreateDate']
 )
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
 )