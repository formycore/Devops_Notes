<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli = boto3.client('sts')
response = ec2_cli.get_caller_identity()
#pprint(response)
#print("The User Account id is : {}\nThe User id is: {}".format(response['Account'],response['UserId']))
=======
import boto3
from pprint import pprint
ec2_cli = boto3.client('sts')
response = ec2_cli.get_caller_identity()
#pprint(response)
#print("The User Account id is : {}\nThe User id is: {}".format(response['Account'],response['UserId']))
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print("The User Account id is : {}\nThe User id is: {}".format(response.get('Account'),response.get('UserId')))