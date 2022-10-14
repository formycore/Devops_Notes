# Steps to connect with remote with ansible and encrypt the user password
1) first create a user with password 
2) check the password authentication
```
sed -ie 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
service sshd restart
```
3) in the ansible server first create a inventory with ini format
```
[master]
dock ansible_host=xx.xx.xx.xx

[master:vars]
ansible_user=<remote_user>
ansible_ssh_pass=<remote_user_password>
ansible_connection=ssh 
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```
4) with ansible vault we can change the hard coded password here
	4a) ```ansible-vault encrypt_string <password_HERE> --ask-vault-pass```
5) for some reason the ini format of inventory file does not support ansible vault
6) we need to convert the ini format inventory to yml format as inventory.yml
```
---
all:
  children:
    master:
      hosts:
        dock:
          ansible_host=xx.xx.xx.xx
  vars:
    ansible_user: <remote_user>
    ansible_ssh_pass: <remote_user_password>
    ansible_connection: ssh 
    ansible_ssh_common_args: '-o StrictHostKeyChecking=no'
```
6a) vars is mapped with children
7) now try to ping the servers
8) ansible -m ping all -i inventory.yml --ask-vault-pass