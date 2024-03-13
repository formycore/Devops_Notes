'''
- docker pull jenkins/jenkins:lts
- docker inspect jenkins/jenkins:lts( to check for the volumes direcotory)
- docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

'''