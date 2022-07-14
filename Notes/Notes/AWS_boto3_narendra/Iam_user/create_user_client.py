<<<<<<< HEAD
import boto3
iam_cli=boto3.client('iam')
user_name=input('Enter the User Name: ')
created_user=iam_cli.create_user(
              UserName=user_name,
              Tags=[
                  {
                      'Key':'Env',
                      'Value': 'Test'
                  }
              ]  
)
=======
import boto3
iam_cli=boto3.client('iam')
user_name=input('Enter the User Name: ')
created_user=iam_cli.create_user(
              UserName=user_name,
              Tags=[
                  {
                      'Key':'Env',
                      'Value': 'Test'
                  }
              ]  
)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(created_user)