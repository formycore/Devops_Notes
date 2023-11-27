import os
import paramiko

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh.connect(hostname='13.127.182.225', username='ubuntu', key_filename='/home/maanya/Downloads/ubuntu_ssh/august.pem')

# Create an SFTP client
sftp = ssh.open_sftp()

# Define the remote and local directories
remote_dir = '/home/ubuntu/remote_test'
local_dir = '/home/maanya/testa'

# Remove the existing destination directory if it exists
if os.path.exists(local_dir):
    os.rmdir(local_dir)

# Copy the directory from remote to local
sftp.get(remote_dir, local_dir)

# Close the SFTP and SSH connections
sftp.close()
ssh.close()