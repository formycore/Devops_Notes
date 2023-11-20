import paramiko
import shutil
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('3.109.55.1',username='ubuntu',key_filename=r'/home/maanya/Downloads/ubuntu_ssh/august.pem')
source = r"/home/ubuntu/docker_test/petclinic.war"
sftp_client = client.open_sftp()
sftp_client.get(source, 'petclinic.war')
sftp_client.close()
client.close()