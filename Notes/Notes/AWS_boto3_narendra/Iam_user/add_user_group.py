<<<<<<< HEAD
import boto3
iam=boto3.client('iam')
response=iam.create_group(
    GroupName='Tester'
)
user_name=input("Enter the user name to add in the tester group: ")
# Adding the user to group
resp=iam.add_user_to_group(
    GroupName='Tester',
    UserName=user_name
=======
import boto3
iam=boto3.client('iam')
response=iam.create_group(
    GroupName='Tester'
)
user_name=input("Enter the user name to add in the tester group: ")
# Adding the user to group
resp=iam.add_user_to_group(
    GroupName='Tester',
    UserName=user_name
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
)