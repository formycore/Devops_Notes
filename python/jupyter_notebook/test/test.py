import paramiko
ssh = paramiko.SSHClient()
#ssh.connect(hostname='hostname',username='username',password='password',port=22)
# SSHException: Server '34.136.221.32' not found in known_hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='34.136.221.32',username='maanya',password='xxxx',port=22)
