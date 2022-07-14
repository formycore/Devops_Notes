<<<<<<< HEAD
# check whether docker is installed or not 
 $ rpm -qa | grep docker
# dokcer info
  $ docker info
# service is running or not
  $ service docker status
# we need to check for the nc for the docker api port connection check
  $ nc -v ip address 2375(docker api port number)
# we need to create a file
vi docker.conf
[Service]
=======
# check whether docker is installed or not 
 $ rpm -qa | grep docker
# dokcer info
  $ docker info
# service is running or not
  $ service docker status
# we need to check for the nc for the docker api port connection check
  $ nc -v ip address 2375(docker api port number)
# we need to create a file
vi docker.conf
[Service]
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock