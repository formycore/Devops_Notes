<<<<<<< HEAD
import boto3
iam = boto3.resource('iam')
user_name=input("Enter the user name")
user=iam.create_user(
    UserName=user_name
)
=======
import boto3
iam = boto3.resource('iam')
user_name=input("Enter the user name")
user=iam.create_user(
    UserName=user_name
)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(user)