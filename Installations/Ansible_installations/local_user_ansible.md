# first create a ssh-keygen
```
- first create a ssh-keygen on the main user 
- then create a demo user 
- sudo useradd -m -d /home/<username> -s /bin/bash <username>
- in the hosts file
host1 ansible_host=localhost ansible_user=demo
host2 ansible_host=10.160.0.7

```