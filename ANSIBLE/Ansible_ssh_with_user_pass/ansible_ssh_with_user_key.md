# Steps to connect with remote with ansible with user and key
1) first copy the private key to ansible server
2) change the permission of the private key
```
chmod 400 <private_key>
```
3) in the ansible server first create a inventory with ini format
```
[master]
knode ansible_host=xx.xx.xx.xx

[master:vars]
ansible_user=maanya
ansible_ssh_private_key_file=/home/ansadmin/id_rsa
ansible_connection=ssh 
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```
4) if we have two two servers with two different keys
   ```
   [master]
knode ansible_host=xx.xx.xx.xx

[master:vars]
ansible_user=maanya
ansible_ssh_private_key_file=/home/ansadmin/id_rsa
ansible_connection=ssh 
ansible_ssh_common_args='-o StrictHostKeyChecking=no'

[other_server]
othernode ansible_host=xx.xx.xx.xx

[other_server:vars]
ansible_user=another_user
ansible_ssh_private_key_file=/path/to/another/private/key
ansible_connection=ssh 
ansible_ssh_common_args='-o StrictHostKeyChecking=no'

[all_servers:children]
master
other_server
```
