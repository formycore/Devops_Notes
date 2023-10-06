import boto3
from botocore.exceptions import ClientError

#
# option 2: S3 resource object will return list of all bucket resources.
# This is useful if we want to further process each bucket resource.
#
s3 = boto3.resource('s3')
buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket)