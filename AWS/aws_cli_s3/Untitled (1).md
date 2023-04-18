```python
# Create s3 bucket with public deny access
# always start aws cmds with !aws
```


```python
!aws s3 mb s3://amonkincloudexample
```

    make_bucket: amonkincloudexample



```python
# Now attach the public deny access
```


```python
!aws s3api put-public-access-block \
--bucket amonkincloudexample \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```


```python
# upload files to S3 with boto3
```


```python
!aws s3 sync /home/maanya/Downloads/other_github/Serverless-Web-Application-on-AWS amonkincloudexample
```

    
    usage: aws s3 sync <LocalPath> <S3Uri> or <S3Uri> <LocalPath> or <S3Uri> <S3Uri>
    Error: Invalid argument type



```python
# Uploading the content to S3 bucket
```


```python
!aws s3 sync /home/maanya/Downloads/other_github/Serverless-Web-Application-on-AWS s3://amonkincloudexample
```

    upload: ../../../other_github/Serverless-Web-Application-on-AWS/index.html to s3://amonkincloudexample/index.html
    upload: ../../../other_github/Serverless-Web-Application-on-AWS/README.md to s3://amonkincloudexample/README.md
    upload: ../../../other_github/Serverless-Web-Application-on-AWS/style.css to s3://amonkincloudexample/style.css
    upload: ../../../other_github/Serverless-Web-Application-on-AWS/lambda-function.py to s3://amonkincloudexample/lambda-function.py
    upload: ../../../other_github/Serverless-Web-Application-on-AWS/script.js to s3://amonkincloudexample/script.js



```python
# Checking versioning enabled or not
aws s3api get-bucket-versioning --bucket bucket_name
```


```python
!aws s3api get-bucket-versioning --bucket amonkincloudexample
```


```python
# Empty the S3 bucket
aws s3 rm s3://<bucket_name> --recursive
```


```python
!aws s3 rm s3://amonkincloudexample --recursive
```

    delete: s3://amonkincloudexample/index.html
    delete: s3://amonkincloudexample/script.js
    delete: s3://amonkincloudexample/README.md
    delete: s3://amonkincloudexample/lambda-function.py
    delete: s3://amonkincloudexample/style.css



```python
# adding the files with exclude of 
```


```python

```


```python

```
