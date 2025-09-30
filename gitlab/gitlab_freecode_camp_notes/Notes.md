- in the gitlab cicd under variables if we select the protected option, the variable will only be available in pipelines that run on protected branches or tags. like main 
- masked variables are not shown in job logs, which is useful for sensitive information like passwords or API keys.
- create s3 bucket
- configure aws cli
- select the bucket 
- properties - s3 website hosting - use this bucket to host a website - index document - index.html - save changes
- permissions - block public access - edit - uncheck all the options - acknowledge - save changes
- bucket policy - edit -
- fill it with json file
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucket10092025san/*"
        }
    ]
} 

----
we get the error 404 The specified key does not exist. because we have not uploaded any file yet
#- aws s3 sync build s3://$AWS_S3_BUCKET/build -- delete
      
      #Takes the build directory (without / at the end).
      # Creates a folder named build in the bucket.
      # Your files end up like:
      # s3:<//my-bucket/build/index.html> # it means it wont be visible to s3 bucket hosting
      # s3:<//my-bucket/build/static/js/main.js>
      # When S3 static hosting looks for index.html at the root, it won’t find it → ❌ 404 error.

- aws s3 sync build/ s3://$AWS_S3_BUCKET/ --delete 
        #        Takes the contents of build/ (because of the trailing slash).
        # Uploads them directly to the bucket root.
        # Your files end up like:
        # s3://my-bucket/index.html
        # s3://my-bucket/static/js/main.js
        # ✅ Works with S3 website hosting (index.html is at the root).
        # Keeps S3 in sync with only the files your new build generated.
        # Prevents users from accidentally loading old, unused assets.

-------------------------------------------------------------------------------------------
now the webpage is visible
http://bucket10092025san.s3-website-us-east-1.amazonaws.com/
- but this is from the feature branch
- deploy to s3 only from main branch
-----------------------------------------------------------------------------------------------
- in gitlab ci yml file
just like to run the deploy stage only on main branch

here we are using

rules:
    - if $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
    #- what is $CI_COMMIT_REF_NAME and $CI_DEFAULT_BRANCH
    #- CI_COMMIT_REF_NAME and CI_DEFAULT_BRANCH are predefined environment variables in GitLab CI
    #- CI_COMMIT_REF_NAME contains the name of the branch or tag that triggered the pipeline.
    #- CI_DEFAULT_BRANCH contains the name of the default branch of the repository, which is usually "main" or "master".
    #- By using the condition if $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH, you can ensure that the deploy stage only runs    # when the pipeline is triggered by a commit to the default branch.
    #- This is useful for scenarios where you want to restrict deployments to only occur from the main branch, ensuring that  only stable and reviewed code is deployed to production.
    # CI_DEFAULT_BRANCH -- The name of the project’s default branch. -- in this case it is main
    # CI_COMMIT_REF_NAME -- The branch or tag name for which project is built.

---------------------------------------------------
- here we are deploying only from main branch right then what is the point of having varaibles unchecked protected option

