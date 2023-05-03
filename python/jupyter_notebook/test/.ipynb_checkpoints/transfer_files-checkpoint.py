import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
	hostname = '34.136.221.32',
	username = 'maanya',
	key_filename = '/home/maanya/Downloads/ubuntu_ssh/id_rsa'
	)
sftp_client = ssh.open_sftp()
print(dir(sftp_client))