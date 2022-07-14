<<<<<<< HEAD
import boto3
sts_cli=boto3.client('sts')
response=sts_cli.get_caller_identity()
=======
import boto3
sts_cli=boto3.client('sts')
response=sts_cli.get_caller_identity()
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print(response)