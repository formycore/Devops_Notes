<<<<<<< HEAD
import boto3
import pprint
session=boto3.Session(profile_name="root")
ec2_re=session.resource(service_name='ec2',region_name='us-east-2')
client=session.client(service_name='ec2')
all_regions=client.describe_regions()
del_vol={'Name':'status','Values':['available']}
#print(reg)
list_of_regions=[]
for each_reg in all_regions['Regions']:
    #print(each_item['RegionName'])
    list_of_regions.append(each_reg['RegionName'])
pprint.pprint(list_of_regions)
for each_vol,each_reg in resource.volumes.filter(Filters=[del_vol]):
	session=boto3.Session(profile_name="root",region_name=each_reg)
	resource=session.resource(service_name="ec2")
	print("List of EC2 Instances from the region: ",each_reg)
	
=======
import boto3
import pprint
session=boto3.Session(profile_name="root")
ec2_re=session.resource(service_name='ec2',region_name='us-east-2')
client=session.client(service_name='ec2')
all_regions=client.describe_regions()
del_vol={'Name':'status','Values':['available']}
#print(reg)
list_of_regions=[]
for each_reg in all_regions['Regions']:
    #print(each_item['RegionName'])
    list_of_regions.append(each_reg['RegionName'])
pprint.pprint(list_of_regions)
for each_vol,each_reg in resource.volumes.filter(Filters=[del_vol]):
	session=boto3.Session(profile_name="root",region_name=each_reg)
	resource=session.resource(service_name="ec2")
	print("List of EC2 Instances from the region: ",each_reg)
	
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
		print(each_vol.id,each_vol.state,each_vol.tags)