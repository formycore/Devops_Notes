# setup jenkins master slave setup with java 
# First thing we need to check is 
    1) Master and slave should have
         Same Java version
         Same Maven version
    2) In case Jave or Maven paths are referring to the agent system then aline it according to masters Global Tool Configuration
    3) In case the case of the AWS server make sure your Jenkins URL should be updated to the latest Public IP.
## Prerequisites
   1) Jenkins server up and running
   2) Slave server with java installed
   ```
   sudo yum install java-1.8.0-openjdk-devel
   ```
## Procedure
   1) Goto Manage Jenkins -> Manage Nodes and Clouds -> New Node
   2) Enter the node name and select Permanent Agent
   3) Enter the number of executors and remote root directory(it depends on the no of cpu cores in the slave server if you have 1 cores then enter 1)
   4) Enter the remote root directory
   5) Enter the labels
   6) Enter the usage
      Usage:
      1) Use this node as much as possible
      2) Only build jobs with label expressions matching this node
   7) Enter the Launch method
         a) Launch agent by connecting it to the master
         b) Launch agent via execution of command on the master
   8) if we need logs keep workdir
   9) Save
   10) Goto Manage Jenkins -> Manage Nodes and Clouds -> select the node 
   11) open the node
   12) Download the jar file in the slave
   13) copy the jar file to the slave server
   14) java -jar agent.jar -jnlpUrl http://xx.xx.xx.xx:8080/computer/ansible/jenkins-agent.jnlp -secret 9bdd1ab19ac5267e0e3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxf189494894113 -workDir "/home/centos/jenkins" &nohup
   15) it will connected to the master

## with ssh method
1) go to slave server
2) ssh-keygen 
3) cd ~/.ssh
4) cat id_rsa.pub >> authorized_keys
5) chmod 600 authorized_keys
6) install ssh-agent plugin in master server
7) go to credentials -> system -> global credentials -> add credentials -> ssh username with private key
8) copy the slave server private key to the master server here at the credentials part
9) go to manage jenkins -> manage nodes and clouds -> new node
10) enter the node name
11) select permanent agent
12) enter the number of executors (it depends on the no of cpu cores in the slave server if you have 1 cores then enter 1)
13) enter the remote root directory(create a directory in the slave server)
14) enter the labels
15) enter the usage
16) enter the launch method as ssh
17) enter the host name
18) enter the credentials
19) Save
## on the jenkins master
1) mkdir -p /var/lib/jenkins/.ssh
2) cd /var/lib/jenkins/.ssh
3) ssh-keyscan -H SLAVE-NODE-IP-OR-HOSTNAME >>/var/lib/jenkins/.ssh/known_hosts
(# ssh-keyscan -H 172.31.38.42 >>/var/lib/jenkins/.ssh/known_hosts)
chown jenkins:jenkins known_hosts
chmod 700 known_hosts
4) go to manage jenkins -> manage nodes and clouds -> select the node
5) open the node
6) it will connected to the master

