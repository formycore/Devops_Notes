# automate the ssh connection
* while creating ec2 instances in the userdata script, the ssh connection is not established.
```
#!/bin/bash
sudo sed -ie 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo service sshd restart
```
* with this ssh password less communication is established
**************************************************************
* yum install epel-release
* yum install ansible -y
* copy the pem file to a directory
* chmod 700 the *.pem file
* create a directory for the ansible playbook
* in the directory create a file called hosts
* in the hosts file add the ip address of the ec2 instance
```
docker ansible_host=172.31.91.46
ansible_user=centos
ansible_ssh_private_key_file=<path of the pem file>
ansible_connection=ssh
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```
* ansible -m ping all -i hosts
*********************************************************************************
# the two nodes should have SSH Key-based authentication
## on the server1 machine
* create ssh key pair
* copy the public key to the other node
* ssh-keygen -t rsa -N "" -f /home/jenkins-slave-01/.ssh/id_rsa
* cd .ssh
* cat id_rsa.pub > authorized_keys
* chmod 700 authorized_keys
```
# ssh-key pair generation
- hosts: "{{groups['check'][1]}}"
  tasks:
    - name: ssh key pair generation
      shell: ssh-keygen -t rsa -b 4096 -f /home/centos/.ssh/id_rsa -N ''
      register: ssh_key_pair_gen
    - name: output of the ssh keys
      debug:
        var: ssh_key_pair_gen
      changed_when: ssh_key_pair_gen.rc == 0
    - name: copy the contents of id_rsa to authorized_keys
      shell: cat /home/centos/.ssh/id_rsa.pub >> /home/centos/.ssh/authorized_keys
      when: ssh_key_pair_gen.rc == 0
```
## on the server2 machine
* create ssh key pair
* copy the public key to the other node
* ssh-keygen -t rsa -N "" -f /home/centos/.ssh/id_rsa
* cd .ssh
* cat id_rsa.pub > authorized_keys


# install rysnc on the both the nodes for docker and jenkins
