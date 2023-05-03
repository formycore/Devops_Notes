import paramiko
result = []
hostname = '34.136.221.32'
uname = 'maanya'
filename = '/home/maanya/Downloads/ubuntu_ssh/id_rsa'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username= uname,key_filename=filename)
stdin, stdout, stderr = ssh.exec_command('mkdir -p /home/maanya/python_test;cd python_test;touch file1;ls -ltr;pwd')
for each_line in stdout:
    result.append(each_line.strip('\n'))

for each_line in result:
    print(each_line.strip())
ssh.close()
