# Create Ansible SSH Key setup through playbook 
- copy the pem or id_rsa file to the remote server
- on the local server where the pem or id_rsa file is present
- scp -i <pem_file> or <id_rsa> <filename> <remote_user>@<remote_ip>:/home/<remote_user>/
- scp -i <pem_file> <pem_file> <remote_user>@<remote_host>:<remote_path>
- scp -i <id_rsa> <id_rsa> <remote_user>@<remote_host>:<remote_path>
```
[master]
dock ansible_host=xx.xx.xx.xx

[master:vars]
ansible_user=<remote_user>
ansible_private_key_file=<private_key_file>
ansible_connection=ssh 
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```
## Now create the ssh-keygen on the ansible server
- ssh-keygen -t rsa
- complete the ssh-keygen process
- copy the path where <entire file is saved in the key>
```
---
- name: Install keys on the Nodes
  hosts: all
  become: yes
  tasks:
    - name: Install keys on the Nodes
      authorized_key:
        user: xxxx
        key: "{{ lookup('file', '/home/xxxxx/.ssh/id_rsa.pub') }}"
        state: present
```
- ansible-playbook -i inventory.yml <playbook_name>.yml
- ssh <remote_server>
## on the remote server the user with ansible is running like ansadmin or ansible or ubuntu or ec2-user must be present on the remote server also 
