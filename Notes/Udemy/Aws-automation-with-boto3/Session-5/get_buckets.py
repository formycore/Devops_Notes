<<<<<<< HEAD
#!/usr/bin/python
import boto3
s3_re=boto3.resource("s3","us-east-2")
for each_bucket in s3_re.buckets.all():
=======
#!/usr/bin/python
import boto3
s3_re=boto3.resource("s3","us-east-2")
for each_bucket in s3_re.buckets.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print each_bucket