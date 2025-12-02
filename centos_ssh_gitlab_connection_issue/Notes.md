- generate the ssh with ssh-keygen -t rsa
- copy the public key to the server with ssh-copy-id user@server
- test the connection with ssh user@server
- if it fails, create a file ~/.ssh/config with the following content:
  Host server
      HostName server_address
      User user
      IdentityFile ~/.ssh/id_rsa