wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vault

vault -version

# start in the dev mode
vault server -dev
```
buntu@ip-172-31-2-45:~$ vault server -dev
==> Vault server configuration:

Administrative Namespace:
             Api Address: http://127.0.0.1:8200
                     Cgo: disabled
         Cluster Address: https://127.0.0.1:8201
   Environment Variables: DBUS_SESSION_BUS_ADDRESS, DEBUGINFOD_URLS, GOTRACEBACK, HOME, LANG, LESSCLOSE, LESSOPEN, LOGNAME, LS_COLORS, PATH, PWD, SHELL, SHLVL, SSH_CLIENT, SSH_CONNECTION, SSH_TTY, TERM, USER, XDG_DATA_DIRS, XDG_RUNTIME_DIR, XDG_SESSION_CLASS, XDG_SESSION_ID, XDG_SESSION_TYPE, _
              Go Version: go1.26.5
              Listener 1: tcp (addr: "127.0.0.1:8200", cluster address: "127.0.0.1:8201", disable_request_limiter: "false", max_json_array_element_count: "10000", max_json_depth: "300", max_json_object_entry_count: "10000", max_json_string_value_length: "1048576", max_request_duration: "1m30s", max_request_size: "33554432", tls: "disabled")
               Log Level:
                   Mlock: supported: true, enabled: false
           Recovery Mode: false
                 Storage: inmem
                 Version: Vault v2.0.4, built 2026-08-03T16:14:36Z
             Version Sha: c9e9d1d4ddd4b55aae79a8949adffa9e96338720
```
- 8200 is the port 
- for dev the storage is in memory and the root token is printed in the logs. You can use this token to login to vault.
- for production you will need to configure a storage backend and TLS. You can find more information about this in the official documentation: https://www.vaultproject.io/docs/configuration
- unseal key and root token are printed in the logs. You can use this token to login to vault. we need to set the environment variable VAULT_ADDR and VAULT_TOKEN to the vault server address and token respectively. In this case, it is http://127.0.0.1:8200
- open another terminal and run the following command to set the environment variables:
```
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='s.XXXXXXXXXXXXXXXXXXXXXXXX' # replace with the actual root token printed in the logs
```
- vault status command can be used to check the status of the vault server. It should return "Sealed: false" if the server is unsealed and ready to use.
              