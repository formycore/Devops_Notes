import boto3
s3 = boto3.client('s3')
for i in dir(s3):
	print(i)
	