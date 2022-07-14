<<<<<<< HEAD
import boto3
s3_re=boto3.resource('s3')
for each in s3_re.buckets.all():
=======
import boto3
s3_re=boto3.resource('s3')
for each in s3_re.buckets.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each.name)