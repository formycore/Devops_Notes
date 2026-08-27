# This enable part is first step to enable the path and then write, read and delete secrets for that path. 
## Enable the path
To enable the path, you need to follow these steps:
1. Enable the KV secrets engine at the desired path (e.g., "secret/") using the following command:
```
vault secrets enable -path=secret kv

vault secrets enable -<specify the path as -path>=<name of the path> <type of the secret engine>

ex:
vault secrets enable -path=my kv
```
# Write a secret
To write a secret to the enabled path, use the following command:
```
vault kv put secret/my-secret my-value="This is a secret value"

ex:
vault kv put my/path my-key-1=value-1


```
# Read a secret
To read a secret from the enabled path, use the following command:
```
vault kv get secret/my-secret
vault kv get --format=json secret/my-secret

ex:
vault kv get my/path
vault kv get --format=json my/path

---
list all the secrets in the enabled path, use the following command:
vault secret list

```
# Delete a secret
To delete a secret from the enabled path, use the following command:
```
vault kv delete secret/my-secret
```
