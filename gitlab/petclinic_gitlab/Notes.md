```
docker volume create sonarqube_data
docker run -d --name sonar -p 9000:9000 -v sonarqube_data:/opt/sonarqube/data sonarqube:lts-community

```
# Adding the sonarqube analysis to the pipeline
```
- open sonarqube and create a new project
- create new project manually
- give the name for the display
- select gitlab CI
- select Maven
- copy the line under the properties section
- open the pom.xml file and add the copied line under the properties section
- add the commit 
- on the sonarqube click continue
- Define the SonarQube Token environment variable.

In GitLab, go to Settings > CI/CD > Variables to add the following variable and make sure it is available for your project:
In the Key field, enter SONAR_TOKEN 
In the Value field, enter an existing token, or a newly generated one: Generate a token
Uncheck the Protect Variable checkbox.
Check the Mask Variable checkbox.


Define the SonarQube URL environment variable.

Still in Settings > CI/CD > Variables add a new variable and make sure it is available for your project:
In the Key field, enter SONAR_HOST_URL 
In the Value field, enter http://13.126.205.41:9000 
Uncheck the Protect Variable checkbox.
Leave the Mask Variable checkbox unchecked.