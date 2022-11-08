# Steps to connect with remote with ansible with user and key
1) first copy the private key to ansible server
2) change the permission of the private key
```
chmod 400 <private_key>
```
3) in the ansible server first create a inventory with ini format
```
[master]
knode ansible_host=34.168.189.34

[master:vars]
ansible_user=maanya
ansible_ssh_private_key_file=/home/ansadmin/id_rsa
ansible_connection=ssh 
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```
