<<<<<<< HEAD
import boto3

ec2 = boto3.resource('ec2')
volume_iterator = ec2.volumes.all()
for v in volume_iterator:
    for a in v.attachments:
=======
import boto3

ec2 = boto3.resource('ec2')
volume_iterator = ec2.volumes.all()
for v in volume_iterator:
    for a in v.attachments:
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
        print ("{0} {1} {2}".format(v.id, v.state, a['InstanceId']))