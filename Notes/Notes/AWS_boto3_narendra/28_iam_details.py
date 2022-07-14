<<<<<<< HEAD
import boto3
iam_re=boto3.resource('iam')
user=iam_re.User("admin")
#print(dir(user))
#print(user.user_name,user.user_id,user.arn,user.create_date)
print(user.user_name,user.user_id)

=======
import boto3
iam_re=boto3.resource('iam')
user=iam_re.User("admin")
#print(dir(user))
#print(user.user_name,user.user_id,user.arn,user.create_date)
print(user.user_name,user.user_id)

>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
