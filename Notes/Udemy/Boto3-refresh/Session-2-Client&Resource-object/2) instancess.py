<<<<<<< HEAD
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="ap-south-1")
for each_in in ec2_con_re.instances():
    print(each_in.id)
ins_id=input("Enter the instance id: ")
for each_ins in ec2_con_re.instances(ins_id):
    print(each_ins)
    
=======
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="ap-south-1")
for each_in in ec2_con_re.instances():
    print(each_in.id)
ins_id=input("Enter the instance id: ")
for each_ins in ec2_con_re.instances(ins_id):
    print(each_ins)
    
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
