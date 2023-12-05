import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
collections_of_regions = []
for each_region in ec2_cli.describe_regions()['Regions']:
    #print(each_region['RegionName'])
    collections_of_regions.append(each_region['RegionName']) # here we add the above each_region with RegionName
print(collections_of_regions)


for each_region in collections_of_regions:
    #ec2_re = boto3.resource('ec2',each_region)
    print(f"\nInstances in region : {each_region}\n")
    ec2_re = boto3.resource('ec2',region_name=each_region)
    cnt=1    
    for each_ins_in_reg in ec2_re.instances.all():
        print(cnt,each_ins_in_reg.instance_id,
               each_ins_in_reg.instance_type,
               each_ins_in_reg.key_name,
              each_ins_in_reg.private_ip_address,
              each_ins_in_reg.public_ip_address,
              each_ins_in_reg.state,
              each_ins_in_reg.vpc_id)
        cnt+=1