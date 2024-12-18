# Run docker as non root users
```
- cat /etc/group | grep docker
- create a user 
- attach the docker group to this user
- sudo adduser dev
- sudo usermod -aG docker dev
- su - dev
- login to the dev user
- dev : docker run hello-world
- we can run the docker from the dev user
- docker run --rm alpine id
$ uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
- docker run -u 1001:1001 --rm alpine id
$ uid=1001 gid=1001 groups=1001

# Create the uid and gid in the Dockerfile

FROM centos:7
RUN useradd -u 1001 testuser
USER testuser
RUN echo "i am $whoami" && echo "my ids are $id"
#CMD ["sh", "-c", "whoami && id"]
CMD ["/bin/sleep", "200"]


- docker build -t cloudyuga/test:learn .
- docker image ls
- docker run --rm -d --name testc cloudyuga/test:learn
- docker exec testc id
- docker exec testc ps aux 
- docker inspect testc --format '{{.Config.User}} {{.Name}}'


mine 

 docker exec -ti container_id id
  362  docker exec -ti container_id whoami
  363  docker exec -it container_id ps -aux
  364  docker inspect container_id
  365  docker inspect container_id --format '{{ .Config.User }}'
  366  docker inspect container_id --format '{{ .Config.User }} {{ Name }}'
  367  docker inspect container_id --format '{{ .Config.User }} {{ .Name }}'
  368  docker inspect container_id | grep User
  369  docker inspect container_id | grep Config
```