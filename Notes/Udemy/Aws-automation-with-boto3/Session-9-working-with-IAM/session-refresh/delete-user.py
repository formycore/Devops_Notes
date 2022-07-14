<<<<<<< HEAD
import boto3
session=boto3.session.Session(profile_name="root")
iam_client=session.client("iam")
delete_name=input("Enter the user to delete: ")
#PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
iam_client.delete_access_key(UserName=delete_name,AccessKeyId='AKIAS47BM5EZHIOP2HFJ')
iam_client.detach_user_policy(UserName=delete_name,PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
iam_client.delete_login_profile(UserName=delete_name)
iam_client.delete_user(UserName=delete_name)
=======
import boto3
session=boto3.session.Session(profile_name="root")
iam_client=session.client("iam")
delete_name=input("Enter the user to delete: ")
#PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
iam_client.delete_access_key(UserName=delete_name,AccessKeyId='AKIAS47BM5EZHIOP2HFJ')
iam_client.detach_user_policy(UserName=delete_name,PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
iam_client.delete_login_profile(UserName=delete_name)
iam_client.delete_user(UserName=delete_name)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
