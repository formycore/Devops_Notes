<<<<<<< HEAD
import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client("ec2")
req_ins=ec2_re.Instance("i-09cadc9593f35e6b5")
print("Instance starting...")
#print(dir(req_ins))
req_ins.start()
req_ins.wait_until_running()
print("your instance is up and running:",req_ins)
=======
import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client("ec2")
req_ins=ec2_re.Instance("i-09cadc9593f35e6b5")
print("Instance starting...")
#print(dir(req_ins))
req_ins.start()
req_ins.wait_until_running()
print("your instance is up and running:",req_ins)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
