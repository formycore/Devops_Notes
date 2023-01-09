- create a s3 bucket
- upload some object  <private>
- to access this <private> files we need to create a **CloudFront**
- with **CloudFront** we get an URL
- with this URL we can access those private files
- but to access those private files we need to have the user and pass to access those private files
- so the process is like this 
- ![A test image](.images/Screenshot%20from%202023-01-08%2023-05-24.png)

# create a s3 bucket
- create a bucket with unique name
- ACLs disable (recommended)
- create bucket
--------------------------
# upload all the files of css files from local to s3 bucket 
- download https://www.free-css.com/free-css-templates/page287/cakezone
- upload to the s3 bucket 
- aws s3 cp ~/cakezone s3://<bucket-name> -- recursive
- Amazon S3
    Buckets
    <bucket-name>
    <Static website hosting> Edit static website hosting 
    Enable
    Index document: index.html
--------------------------------------
# create a cloudfront distribution
    - create a cloudfront distribution
    - Origin Domain Name: <bucket-name>.s3.amazonaws.com
    - name: <bucket-name>
    - Origin access: Origin access control settings (recommended)
    - Origin access control
        -  Create control setting 
        - Signing behavior: Do not sign requests
        - https(2): Enabled
        - Default root object: index.html <if it is a html page>
        - create distribution
    - Now here we have to change the permission of the bucket
    - go to the bucket
    - Permissions
    - Bucket Policy
    - paste the below code
      {
            "Version": "2008-10-17",
            "Id": "PolicyForCloudFrontPrivateContent",
            "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::awssandeepchary/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::205449568396:distribution/E1XWPKE4G996JT"
                }
                        }
                    }
                ]
       }

