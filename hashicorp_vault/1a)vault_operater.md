# vault operater
- used in production mode to initialize the vault server and unseal the vault server. In dev mode, the vault server is automatically unsealed and the root token is printed in the logs.
- this is a commmand 
```
vault operator init
```
- to initialize the vault server and generate the unseal keys and root token. The unseal keys are used to unseal the vault server and the root token is used to login to the vault server.
- after initializing the vault server, the unseal keys and root token are printed in the logs. You need to save these keys and token in a secure place as they are required to unseal the vault server and login to the vault server.
- with the master key we can use for encrypt and decrypt the data. this is generated with **vault operator init**
- when installed the vault server is in sealed state. In order to use the vault server, we need to unseal the vault server using the unseal keys generated during the initialization process.it gives 5 unseal keys and 1 root token. we need to use 3 unseal keys to unseal the vault server. we can use the following command to unseal the vault server.
```
vault operator unseal <unseal_key_1>
vault operator unseal <unseal_key_2>
vault operator unseal <unseal_key_3>
```
- after unsealing the vault server, we can use the root token to login to the vault server. we can use the following command to login to the vault server.
```
vault login <root_token>
```

------------------------
# practical example
- export VAULT_ADDR="http://your_public_ip_address:8200"
- vault operator init
- after this we get 5 unseal keys and 1 root token. we need to use 3 unseal keys to unseal the vault server. we can use the following command to unseal the vault server.
- then we can able to login to the vault server