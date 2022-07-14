<<<<<<< HEAD
import boto3
ec2_cli=boto3.client('ec2')
ec2_re=boto3.resource('ec2')
f1={"Name":"instance-id","Values":['i-08c45218b24fc34d9']}
for each in ec2_re.instances.filter(Filters=[f1]):
=======
import boto3
ec2_cli=boto3.client('ec2')
ec2_re=boto3.resource('ec2')
f1={"Name":"instance-id","Values":['i-08c45218b24fc34d9']}
for each in ec2_re.instances.filter(Filters=[f1]):
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
    print(each.id)