<<<<<<< HEAD
import boto3
aws_mgm_con=boto3.session.Session(profile_name="root")
sts_con_cli=aws_mgm_con.client(service_name="sts",region_name="us-east-2")
response=sts_con_cli.get_caller_identity()
#print(response)
# FOR PICKING ONE IN DICTIONARY WE USE ['OPERATION NAME']
# print(response['Account']) OR
=======
import boto3
aws_mgm_con=boto3.session.Session(profile_name="root")
sts_con_cli=aws_mgm_con.client(service_name="sts",region_name="us-east-2")
response=sts_con_cli.get_caller_identity()
#print(response)
# FOR PICKING ONE IN DICTIONARY WE USE ['OPERATION NAME']
# print(response['Account']) OR
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(response.get('Account'))