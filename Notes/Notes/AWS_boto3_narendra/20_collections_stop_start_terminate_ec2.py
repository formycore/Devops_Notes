<<<<<<< HEAD
import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
all_ins_id=[]
for each in ec2_re.instances.all():
    all_ins_id.append(each.id)
waiter=ec2_cli.get_waiter('instance_running')
ec2_re.instances.start()
waiter.wait(InstanceIds=all_ins_id)
=======
import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
all_ins_id=[]
for each in ec2_re.instances.all():
    all_ins_id.append(each.id)
waiter=ec2_cli.get_waiter('instance_running')
ec2_re.instances.start()
waiter.wait(InstanceIds=all_ins_id)
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print("Your instance are up and running")