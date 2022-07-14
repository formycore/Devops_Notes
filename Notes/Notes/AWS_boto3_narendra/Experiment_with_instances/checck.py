<<<<<<< HEAD
import boto3
iam_cli=boto3.client('iam')
response=iam_cli.list_users()['Users']
for each in response:
    print(each)
=======
import boto3
iam_cli=boto3.client('iam')
response=iam_cli.list_users()['Users']
for each in response:
    print(each)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    break