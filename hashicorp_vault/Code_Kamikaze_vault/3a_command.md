```
vault secrets enable -path=secret kv
path is secret
kv is secret engine

vault kv put secret/user_credentials username="" password=""
vault kv get secret/user_credentials

```
```json
{
    "username": "",
    "password": ""
}
```
