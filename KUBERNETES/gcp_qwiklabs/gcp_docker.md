```create a docker image
- tag it to <regional-repository>-docker.pkg.dev/my-project/my-repo/my-image.
```
------
# Create the target Docker repository
```
From the Navigation Menu, under CI/CD navigate to Artifact Registry > Repositories.

Click the +CREATE REPOSITORY icon next to repositories.

Specify my-repository as the repository name.

Choose Docker as the format.

Under Location Type, select Region and then choose the location : us-west1.

Click Create.
```
# Configure authentication
```
gcloud auth configure-docker us-west1-docker.pkg.dev


```
# Create an Artifact Registry repository (Using CLI)
```
gcloud artifacts repositories create my-repository --repository-format=docker --location=us-west1 --description="Docker repository"
```

# Push the container to Artifact Registry
```
cd ~/test
docker build -t us-west1-docker.pkg.dev/qwiklabs-gcp-02-e16bf0274727/my-repository/node-app:0.2 .
# docker images
- Push this image to Artifact Registry.
docker push us-west1-docker.pkg.dev/qwiklabs-gcp-02-e16bf0274727/my-repository/node-app:0.2
```
