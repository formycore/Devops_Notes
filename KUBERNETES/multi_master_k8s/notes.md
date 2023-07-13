172.31.5.109  haproxy-lb
172.31.15.195  kubernetes-master1
172.31.5.132  kubernetes-master2
10.0.1.32  kubernetes-worker1

/etc/hosts
172.31.5.109  haproxy-lb
172.31.15.195  kubernetes-master1
172.31.5.132  kubernetes-master2


under haproxy 

/etc/haproxy/haproxy.cfg 


frontend kubernetes
bind 172.31.5.109:6443
option tcplog
mode tcp
default_backend kubernetes-master-nodes
backend kubernetes-master-nodes
mode tcp
balance roundrobin
option tcp-check
server kubernetes-master1 172.31.15.195:6443 check fall 3 rise 2
server kubernetes-master2 172.31.5.132:6443 check fall 3 rise 2

systemctl restart haproxy
systemctl enable haproxy