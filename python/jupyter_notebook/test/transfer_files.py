import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='34.136.221.32',username='maanya',key_filename = '/home/maanya/Downloads/ubuntu_ssh/id_rsa',port=22)
sftp_client = ssh.open_sftp()
sftp_client.get('')