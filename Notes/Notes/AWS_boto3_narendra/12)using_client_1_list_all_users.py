<<<<<<< HEAD
import boto3
from pprint import pprint
# iam ,ec2, and s3
iam_cli=boto3.client('iam')
ec2_cli=boto3.client('ec2')
s3_cli=boto3.client('s3')

# list all iam users using client object
##print(iam_cli.list_users())
response=iam_cli.list_users()
#print(response['Users'])
for each in response['Users']:
=======
import boto3
from pprint import pprint
# iam ,ec2, and s3
iam_cli=boto3.client('iam')
ec2_cli=boto3.client('ec2')
s3_cli=boto3.client('s3')

# list all iam users using client object
##print(iam_cli.list_users())
response=iam_cli.list_users()
#print(response['Users'])
for each in response['Users']:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
	print(each['UserName'])