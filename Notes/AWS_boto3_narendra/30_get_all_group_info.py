<<<<<<< HEAD
import boto3
iam_cli=boto3.client('iam')
response=iam_cli.list_groups()
for each_group in response['Groups']:
=======
import boto3
iam_cli=boto3.client('iam')
response=iam_cli.list_groups()
for each_group in response['Groups']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each_group['GroupName'])