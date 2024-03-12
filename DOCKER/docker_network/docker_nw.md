'''
- in a host there are 2 containers
- two scenarios
  - 1. two needs to be connected
  - 2. no need to be connected

- 1. two needs to be connected
    - docker0 is used to connect the containers
    - it is also called as virtual ethernet bridge(veth)
    - default network in docker is bridge
    - there are two types of network
        - bridge
        - host
---------------------------------------------------
1) connecting two containers
    - docker run -itd --name login nginx:latest
    - docker ps 
    - docker inspect login | grep -i ipaddress
    - check for the ip address and from the host machine ping the ip address, it will connect
    - docker run -itd --name db nginx:latest
    - docker inspect db | grep -i ipaddress
    - check for the ip address and from the host machine ping the ip address, it will connect
2) not connecting two containers
    - docker network create mynw
    - docker run -itd --name login --network mynw nginx:latest
    - docker ps 
    - docker inspect login | grep -i ipaddress
    - check for the ip address and from the host machine ping the ip address, it will not connect
    - docker run -itd --name db --network none nginx:latest
    - docker inspect db | grep -i ipaddress
    - check for the ip address and from the host machine ping the ip address, it will not connect


'''