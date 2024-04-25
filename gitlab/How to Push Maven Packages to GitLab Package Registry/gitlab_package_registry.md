### https://docs.gitlab.com/ee/user/packages/package_registry/


# How to Push Maven Packages to GitLab Package Registry ?
## Step #1:How to Create Project Access Token in GitLab
```
To generate a Project access token in GitLab, follow these steps: Access Your Repository Settings > Navigate to Access Tokens > Click on Add New Token
- select all if needed
```
## Step #2:Create setting.xml file in your GitLab repository and add below configuration in your settings.xml file
```
Create setting.xml file in your GitLab repository and add below configuration in your settings.xml file
-----------------------------------------------------------------------------------------
<settings>
  <servers>
    <server>
      <id>gitlab-maven</id>
      <configuration>
        <httpHeaders>
          <property>
            <name>Private-Token</name>
            <value>REPLACE_WITH_YOUR_PROJECT_ACCESS_TOKEN</value>
          </property>
        </httpHeaders>
      </configuration>
    </server>
  </servers>
</settings>
-----------------------------------------------------------------------------------------
```
## Step #3:Add variable in your GitLab repository
```
- to get the project id 
- from .gitlab-ci.yml file
- echo $CI_PROJECT_ID
---------------------------
- here we are using the project id
- Go to Your Repository Settings section > CI/CD > Variables
- Key: PROJECT_ID
- Value: REPLACE_WITH_YOUR_PROJECT_ID
- Add Variable
```
## Step #4:To add publishing details to your Maven pom.xml configuration file
```
<repositories>
  <repository>
    <id>gitlab-maven</id>
    <url>https://gitlab.com/api/v4/projects/${PROJECT_ID}/packages/maven</url>
  </repository>
</repositories>
<distributionManagement>
  <repository>
    <id>gitlab-maven</id>
    <url>https://gitlab.com/api/v4/projects/${PROJECT_ID}/packages/maven</url>
  </repository>
  <snapshotRepository>
    <id>gitlab-maven</id>
    <url>https://gitlab.com/api/v4/projects/${PROJECT_ID}/packages/maven</url>
  </snapshotRepository>
</distributionManagement>
```
## Step #5:Create .gitlab-ci.yml push maven packages to GitLab Package Registry
```
deploy:
  image: maven:latest
  script:
    - mvn deploy -s settings.xml


# Monitor the Pipeline
```
## Step #6:To check maven package push to GitLab package registery
```
Go to project/particular repository > Deploy section > package registry

```

