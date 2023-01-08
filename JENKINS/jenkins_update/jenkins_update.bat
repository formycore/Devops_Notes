# update jenkins with windows batch
# 1. stop jenkins
net stop jenkins
# 2. backup jenkins
xcopy /E /I /Y /Q "C:\Program Files (x86)\Jenkins" "C:\Program Files (x86)\Jenkins_backup"
# backup jekins plugins 
xcopy /E /I /Y /Q "C:\Program Files (x86)\Jenkins\plugins" "C:\Program Files (x86)\Jenkins_backup\plugins"
# 3. download jenkins.war
curl -o "C:\Program Files (x86)\Jenkins\jenkins.war" http://mirrors.jenkins-ci.org/war/latest/jenkins.war
# 4. start jenkins
net start jenkins
