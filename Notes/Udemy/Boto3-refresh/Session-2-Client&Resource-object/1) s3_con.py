<<<<<<< HEAD
import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
s3_con=aws_mag_con.resource('s3')
for each_buckets in s3_con.buckets.all():
  print(each_buckets)
=======
import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
s3_con=aws_mag_con.resource('s3')
for each_buckets in s3_con.buckets.all():
  print(each_buckets)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
