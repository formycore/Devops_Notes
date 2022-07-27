-- 
# ansible notes
- copy the pem or private file to ansible control server
- in the node server make sure for password authentication is enabled
- chmod 600 to the file
- in the ansible hosts file or in the host file 
  10.138.x.x ansible_user=maanya ansible_ssh_private_key_file=/home/maanya/id_rsa ansible_connection=ssh
- copy the **ansible.cfg, hosts and roles** to the present working directory
- chown -R maanya:maanya to the present working directory
- **changes** the ansible.cfg file 
  - **inventory = present working directory<./hosts>**
  - **#host_key_checking = False**
-----------------------------------
- change owner ship of the file/folder to the user
$ chown -R maanya:maanya /home/maanya/
---------------------------------------------
under node
  - useradd <user>
  - mkdir -p /home/<user>
  - chown -R <user>:<user> /home/<user>
  - chmod -R 700 /home/<user>
  - ssh-keygen -t rsa -b 4096 -f /home/<user>/.ssh/id_rsa -N ""
  - cd .ssh
  - cat id_rsa >> authorized_keys
  - chmod 700 authorized_keys
------------------------------------------
configure on master server
  - Copy the slave node's public key[id_rsa.pub] to Master Node's known_hosts file
  - ssh-keyscan -H SLAVE-NODE-IP-OR-HOSTNAME >>/var/lib/jenkins/.ssh/known_hosts
-------------------------------------------------------------------------------
**_how to keep inventory_hostname_**
[pen]
docker ansible_host=10.138.x.x ansible_user=xxxxx ansible_ssh_private_key_file=/home/xxxxx/id_rsa ansible_connection=ssh
jenkins ansible_host=10.128.0.2 ansible_user=xxxxx ansible_ssh_private_key_file=/home/xxxxx/id_rsa ansible_connection=ssh
-----------------------------------------------------------------
# **how to sync with the slave node**
**_server1 and server2 should have rsync installed and ssh-copy-id setup_**

```---
- name: Sync Pull task - Executed on  the Destination host "{{groups['app'][1]}}"
  hosts: "{{groups['check'][0]}}" # it will check the first host in the group
  user: maanya
  tasks:   
    - name: Copy the file from jenkins to docker using Method Pull
      tags: sync-pull
      synchronize:
        src: "{{ item }}"
        dest: "{{ item }}"
        mode: pull
      delegate_to: "{{groups['check'][1]}}" # this will check the second host in the group
      register: syncfile
      run_once: true
      with_items:
       - /home/maanya/intel # this is the source file
```
