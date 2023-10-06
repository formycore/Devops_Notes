import boto3
s3 = boto3.client('s3')
for i in dir(s3):
	if i.startswith('l'):
		print(i)
response = s3.list_buckets()['Buckets']
for bucket in response:
	print("Bucket name is: {}, Created on : {} ".format(bucket['Name'],bucket['CreationDate']))

