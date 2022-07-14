<<<<<<< HEAD
import boto3
import time
ec2_cli=boto3.client('ec2')
ec2_re=boto3.resource('ec2')
instance=ec2_re.Instance("i-09cadc9593f35e6b5")
print("starting the instance...")
instance.start()
while True:
    instance=ec2_re.Instance("i-09cadc9593f35e6b5")
    print("The current state of ec2 is :",instance.state['Name'])
    if instance.state['Name']=="running":
        break
    print("Waiting for get running state")
    time.sleep(5)

print(instance.state['Name'])    
=======
import boto3
import time
ec2_cli=boto3.client('ec2')
ec2_re=boto3.resource('ec2')
instance=ec2_re.Instance("i-09cadc9593f35e6b5")
print("starting the instance...")
instance.start()
while True:
    instance=ec2_re.Instance("i-09cadc9593f35e6b5")
    print("The current state of ec2 is :",instance.state['Name'])
    if instance.state['Name']=="running":
        break
    print("Waiting for get running state")
    time.sleep(5)

print(instance.state['Name'])    
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
print("Now your instance is up and running ")