<<<<<<< HEAD
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
=======
import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
pprint(ec2_cli.create_key_pair(KeyName='ec2_key1'))