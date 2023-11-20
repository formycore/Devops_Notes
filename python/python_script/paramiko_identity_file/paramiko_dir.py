import paramiko
from scp import SCPClient

remote_hostname = "3.109.55.1"
remote_username = "ubuntu"
remote_dir = "/home/ubuntu/docker_test/"
local_dir = "/home/maanya/Downloads/Devops_Notes/python/python_script/paramiko_identity_file/"
key_file = "/home/maanya/Downloads/ubuntu_ssh/august.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open(key_file, "rb") as f:
    key = f.read()

ssh.connect(hostname=remote_hostname, username=remote_username, pkey=key)

scp = SCPClient(ssh)
scp.get(remote_dir, local_dir)

scp.close()
