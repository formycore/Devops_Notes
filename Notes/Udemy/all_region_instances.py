<<<<<<< HEAD
import boto3
import pprint
session=boto3.Session(profile_name="root",region_name="us-east-2")
client=session.client(service_name='ec2')
all_regions=client.describe_regions()
#pprint.pprint(all_regions['Regions'])
# storing all the regions into a list
list_of_Regions=[]
for each_reg in all_regions['Regions']:
	#print(each_reg['RegionName'])
	list_of_Regions.append(each_reg['RegionName'])
	#print("List all the regions")
pprint.pprint(list_of_Regions)

for each_reg in list_of_Regions:
	session=boto3.Session(profile_name="root",region_name=each_reg)
	resource=session.resource(service_name="ec2")
	print("List of EC2 Instances from the region: ",each_reg)
	for each_in in resource.instances.all():
=======
import boto3
import pprint
session=boto3.Session(profile_name="root",region_name="us-east-2")
client=session.client(service_name='ec2')
all_regions=client.describe_regions()
#pprint.pprint(all_regions['Regions'])
# storing all the regions into a list
list_of_Regions=[]
for each_reg in all_regions['Regions']:
	#print(each_reg['RegionName'])
	list_of_Regions.append(each_reg['RegionName'])
	#print("List all the regions")
pprint.pprint(list_of_Regions)

for each_reg in list_of_Regions:
	session=boto3.Session(profile_name="root",region_name=each_reg)
	resource=session.resource(service_name="ec2")
	print("List of EC2 Instances from the region: ",each_reg)
	for each_in in resource.instances.all():
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
		print(each_in.id,each_in.state['Name'])