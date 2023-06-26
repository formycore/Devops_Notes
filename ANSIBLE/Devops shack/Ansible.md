# how to ssh communicate with remote host
```
server 1
# to generate ssh key without entering passphrase
ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
# to copy the public key to remote host
copy the content of ~/.ssh/id_rsa.pub from server 1 and paste in the end of the file for server2 ~/.ssh/authorized_keys
from server 1 
ssh server2 # ssh -o StrictHostKeyChecking=no user@remote-host # to avoid entering yes
it will connect to server2 without entering password
```