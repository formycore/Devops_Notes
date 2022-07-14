<<<<<<< HEAD
import boto3
iam_re=boto3.resource('iam')
for each in iam_re.users.all():
=======
import boto3
iam_re=boto3.resource('iam')
for each in iam_re.users.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each.user_id,each.arn)