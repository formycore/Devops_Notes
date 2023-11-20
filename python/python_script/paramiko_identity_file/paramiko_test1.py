import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('3.109.55.1',username='ubuntu',key_filename=r'/home/maanya/Downloads/ubuntu_ssh/august.pem')

remote_dir = r"/home/ubuntu/docker_test"
#dest = r"/home/maanya/Downloads/Devops_Notes/python/python_script/paramiko_identity_file/"
sftp_client = client.open_sftp()
sftp_client.get(remote_dir, 'docker_test')
sftp_client.close()
client.close()