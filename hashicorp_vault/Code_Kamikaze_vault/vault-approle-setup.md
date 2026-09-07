# 🔐 HashiCorp Vault — AppRole Authentication & Application Policy

> **Purpose:** Configure Vault so an application can authenticate using **AppRole** and access only the secrets and Vault APIs it needs.

---

## 🗺️ Overview

```text
┌──────────────────────┐
│  1. Login to Vault   │
│     with admin token │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 2. Enable AppRole    │
│    authentication    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 3. Create HCL Policy │
│    for application   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 4. Write Policy      │
│    into Vault        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 5. Create AppRole    │
│    for application   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 6. Retrieve          │
│    Role ID / Secret ID│
└──────────────────────┘
```

---

# 🚀 Step 1 — Login to Vault

Authenticate to Vault using an administrative/root token.

```bash
vault login <VAULT_TOKEN>
```

Verify the current token:

```bash
vault token lookup
```

> ⚠️ **Security:** Never commit Vault tokens, root tokens, or Secret IDs to Git.

---

# 🔑 Step 2 — Enable AppRole Authentication

Enable the AppRole authentication method:

```bash
vault auth enable approle
```

Verify that AppRole is enabled:

```bash
vault auth list
```

You should see something similar to:

```text
Path      Type      Description
----      ----      -----------
approle/  approle   n/a
```

> 💡 **Note:** `approle` is the authentication method. The application role itself is created in a later step.

---

# 📜 Step 3 — Create the Application Policy

Create an HCL policy file.

For example:

```bash
vi my-policy.hcl
```

Add the following policy:

```hcl
# Permission for managing secrets, without delete option
path "secret/data/*" {
  capabilities = ["create", "read", "update", "list"]
}

# Permission for listing the secrets engines
path "sys/mounts" {
  capabilities = ["read", "list"]
}

# Permission for enabling and managing secrets engines
path "sys/mounts/*" {
  capabilities = ["create", "read", "update", "list"]
}

# Permission for token management
path "auth/token/lookup-self" {
  capabilities = ["read"]
}

path "auth/token/renew-self" {
  capabilities = ["update"]
}
```

### 🧩 What each policy path does

| Vault Path | Purpose | Capabilities |
|---|---|---|
| `secret/data/*` | Manage KV secrets | Create, Read, Update, List |
| `sys/mounts` | List secrets engines | Read, List |
| `sys/mounts/*` | Manage secrets engines | Create, Read, Update, List |
| `auth/token/lookup-self` | Look up current token | Read |
| `auth/token/renew-self` | Renew current token | Update |

### ⚠️ Important security consideration

The following permission is **very powerful**:

```hcl
path "sys/mounts/*" {
  capabilities = ["create", "read", "update", "list"]
}
```

If the application only needs to **read/write secrets**, it normally should **not** be allowed to manage secrets engines.

A more restrictive application policy is preferable when possible.

---

# 📝 Step 4 — Write the Policy to Vault

Upload the policy into Vault:

```bash
vault policy write <policy_name> <file_name>.hcl
```

### Example

If your policy is called `my-policy`:

```bash
vault policy write my-policy my-policy.hcl
```

Verify that the policy exists:

```bash
vault policy list
```

Read the policy:

```bash
vault policy read my-policy
```

---

# 👤 Step 5 — Create an AppRole for the Application

Create a role and attach the policy:

```bash
vault write auth/approle/role/<role_name> \
  token_policies="<policy_name>" \
  token_ttl=1h \
  token_max_ttl=4h
```

### Example

```bash
vault write auth/approle/role/my-role \
  token-policies="my-policy" \
  token_ttl=1h \
  token_max_ttl=4h
```

### ⏱️ Token lifetime

| Setting | Value | Meaning |
|---|---:|---|
| `token_ttl` | `1h` | Initial token lifetime |
| `token_max_ttl` | `4h` | Maximum renewable lifetime |

Verify the role:

```bash
vault read auth/approle/role/my-role
```

---

# 🆔 Step 6 — Retrieve Role ID and Secret ID

The application needs two values to authenticate through AppRole:

```text
Role ID
   +
Secret ID
   ↓
Vault AppRole Login
   ↓
Vault Token
```

## Retrieve the Role ID

```bash
vault read auth/approle/role/<role_name>/role-id
```

### Example

```bash
vault read auth/approle/role/my-role/role-id
```

Example output:

```text
Key        Value
---        -----
role_id    xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

---

## Retrieve the Secret ID

Generate a Secret ID for the role:

```bash
vault write -f auth/approle/role/<role_name>/secret-id
```

### Example

```bash
vault write -f auth/approle/role/my-role/secret-id
```

Example output:

```text
Key                   Value
---                   -----
secret_id             xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
secret_id_accessor    xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

> 🔐 **Important:** Treat the **Secret ID like a password**. Do not commit it to source control, put it in application logs, or share it unnecessarily.

---

# 🔄 AppRole Authentication Flow

Once the application has the `role_id` and `secret_id`, it can authenticate:

```text
                  ┌─────────────────┐
                  │   Application   │
                  └────────┬────────┘
                           │
                    Role ID + Secret ID
                           │
                           ▼
              ┌─────────────────────────┐
              │ Vault AppRole Auth      │
              │ auth/approle/login      │
              └────────────┬────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   Vault Token   │
                  └────────┬────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │   Application Policy   │
              │      my-policy         │
              └────────────┬────────────┘
                           │
                           ▼
                    Access to allowed
                    Vault paths only
```

---

# 🧪 Quick Verification

After creating the role, you can test AppRole authentication manually.

First obtain:

```bash
ROLE_ID=$(vault read -field=role_id auth/approle/role/my-role/role-id)
```

Generate a Secret ID:

```bash
SECRET_ID=$(vault write -field=secret_id -f auth/approle/role/my-role/secret-id)
```

Login:

```bash
vault write auth/approle/login \
  role_id="$ROLE_ID" \
  secret_id="$SECRET_ID"
```

Vault should return a client token.

You can then test the token:

```bash
vault token lookup
```

---

# 📌 Command Cheat Sheet

| Task | Command |
|---|---|
| Login | `vault login <VAULT_TOKEN>` |
| Enable AppRole | `vault auth enable approle` |
| List auth methods | `vault auth list` |
| Create policy file | `vi my-policy.hcl` |
| Write policy | `vault policy write my-policy my-policy.hcl` |
| List policies | `vault policy list` |
| Read policy | `vault policy read my-policy` |
| Create AppRole | `vault write auth/approle/role/my-role ...` |
| Read AppRole | `vault read auth/approle/role/my-role` |
| Get Role ID | `vault read auth/approle/role/my-role/role-id` |
| Generate Secret ID | `vault write -f auth/approle/role/my-role/secret-id` |
| AppRole login | `vault write auth/approle/login role_id="$ROLE_ID" secret_id="$SECRET_ID"` |

---

## 🔒 Security Checklist

- [ ] Do not use the **root token** inside an application.
- [ ] Store the **Secret ID** securely.
- [ ] Never commit Role IDs/Secret IDs to Git.
- [ ] Avoid logging Vault tokens.
- [ ] Give applications the **minimum required capabilities**.
- [ ] Avoid granting `sys/mounts/*` unless the application genuinely needs to manage secrets engines.
- [ ] Use short token TTLs where practical.
- [ ] Rotate/revoke credentials when an application is decommissioned.
