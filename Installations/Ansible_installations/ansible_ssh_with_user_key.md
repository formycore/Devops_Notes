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
