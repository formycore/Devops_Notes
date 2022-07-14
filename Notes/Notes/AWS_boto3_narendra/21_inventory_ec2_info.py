<<<<<<< HEAD
import boto3
from pprint import pprint
import time
import csv
ec2_re=boto3.resource('ec2')
cnt=1
csv_ob=open("inventory.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_no","Instance_ID","Instance_type","Architecture","launch_time","public_ip_address","private_ip"])
for each in ec2_re.instances.all():
    print(cnt,
          each.instance_id,
          each.instance_type,
          each.architecture,
          each.launch_time.strftime("%Y-%m-%d"),
          each.public_ip_address,
          each.private_ip_address)
    csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.public_ip_address,each.private_ip_address])
    cnt+=1
csv_ob.close()
=======
import boto3
from pprint import pprint
import time
import csv
ec2_re=boto3.resource('ec2')
cnt=1
csv_ob=open("inventory.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_no","Instance_ID","Instance_type","Architecture","launch_time","public_ip_address","private_ip"])
for each in ec2_re.instances.all():
    print(cnt,
          each.instance_id,
          each.instance_type,
          each.architecture,
          each.launch_time.strftime("%Y-%m-%d"),
          each.public_ip_address,
          each.private_ip_address)
    csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.public_ip_address,each.private_ip_address])
    cnt+=1
csv_ob.close()
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
csv_w.wre