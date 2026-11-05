```
- dynamic secrets
  - dynamic secrets are generated on demand and have a limited lifetime.
  - they are typically used for database credentials, API keys, and other sensitive information.
  - dynamic secrets can be revoked or rotated automatically after a certain period of time.
  - they provide an additional layer of security by reducing the risk of long-lived credentials being compromised.
- with aws credentials, show me the example of dynamic secrets
  - when using AWS credentials, dynamic secrets can be generated using AWS IAM roles and temporary security tokens.
  - for example, you can use the AWS Security Token Service (STS) to generate temporary credentials that are valid for a limited time.
  - these temporary credentials can be used to access AWS services without exposing long-lived access keys.
  - once the temporary credentials expire, they can no longer be used, reducing the risk of unauthorized access.
```
```
- vault secrets enable -path=aws aws
- vault secret list
## set root config for aws with access key and secret key

- vault write aws/config/root access_key=<AWS_ACCESS_KEY> secret_key=<AWS_SECRET_KEY> region=us-east-1
```

# Step 3 - setup a role
- vault write aws/roles/my-ec2-role credential_type=iam_user policy_document=-<<EOF
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": "*"
    }
  ]
}
EOF
```
- Step 4 - generate dynamic secrets
- vault read aws/creds/my-ec2-role