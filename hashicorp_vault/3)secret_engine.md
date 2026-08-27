# secret engines
```
vault secrets list
- it will list all the enabled secret engines in the vault server. The output will show the path, type, and description of each secret engine.
- cubbyhole
- identity
- kv
- secret
- sys
    - these are the default secret engines that are enabled in the vault server. You can enable additional secret engines as needed.
```
# disabling secret engines
```
vault secrets disable <path>
- it will disable the secret engine at the specified path. You need to provide the path of
ex:
    vault secrets disable aws<secret engine name>
```
# enabling secret engines
```
vault secrets enable <type>
- it will enable the secret engine of the specified type. You need to provide the type of
secret engine you want to enable.
ex:
    vault secrets enable aws
```
# dynamic secrets


- dynamic secrets are generated on-demand when a client requests them. They are typically used for short-lived credentials that are automatically revoked after a certain period of time. This helps to reduce the risk of long-lived credentials being compromised.
- dynamic secrets can be generated for various types of resources, such as databases, cloud providers, and other services. When a client requests a dynamic secret, the secret engine generates a new credential with a limited lifespan and returns it to the client. The client can then use the credential to access the resource for a limited time before it expires and is automatically revoked.
```
vault secrets enable -path=aws aws
- it will enable the AWS secret engine at the specified path. You can specify a custom path

