<<<<<<< HEAD
import boto3
iam_cli=boto3.client('iam')
ec2_cli=boto3.client('ec2')
s3_cli=boto3.client('s3')
# listing all users using client object
response=iam_cli.list_users()
resp=s3_cli.list_buckets()['Buckets']
for user in response['Users']:
    for s3_buc in resp:
=======
import boto3
iam_cli=boto3.client('iam')
ec2_cli=boto3.client('ec2')
s3_cli=boto3.client('s3')
# listing all users using client object
response=iam_cli.list_users()
resp=s3_cli.list_buckets()['Buckets']
for user in response['Users']:
    for s3_buc in resp:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
        print(user['UserName'],s3_buc['Name'])