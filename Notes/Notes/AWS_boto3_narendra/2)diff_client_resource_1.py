<<<<<<< HEAD
import boto3
aws_mgt=boto3.session.Session(profile_name='root')
iam_cli=aws_mgt.client('iam','us-east-2')
iam_re=aws_mgt.resource('iam','us-east-2')
#print(iam_cli.list_users())
#print(iam_cli.list_users()['Users'])
# above we get the list so we take for loop
for each in iam_cli.list_users()['Users']:
	#print(each)
=======
import boto3
aws_mgt=boto3.session.Session(profile_name='root')
iam_cli=aws_mgt.client('iam','us-east-2')
iam_re=aws_mgt.resource('iam','us-east-2')
#print(iam_cli.list_users())
#print(iam_cli.list_users()['Users'])
# above we get the list so we take for loop
for each in iam_cli.list_users()['Users']:
	#print(each)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
	print(each['UserName'],each['UserId'],each['Arn'])