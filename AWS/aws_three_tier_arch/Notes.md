# CIDR
```
classless inter-domain routing
- 10.0.0.0 - octanes
- 10.0.0.0/24 - 24 is subnet mask
- network portion - 24
- why 32 is taken here ?
- 0.0.0.0 is an octane octane is 8 bit so take 4 octanes 8*4=32
- host portion - (32-24=8)
- 2 power of 8 is 256
- so we get 256 ip address in this network

if we go with 
- 10.0.0.0/25
- 32-25=7 
- 2 power of 7 is 128

------------------------------
break the vpc into subnets
subnet 1
10.0.0.0/25 
network portion is 25
host portion is 32-25 = 7 
2 power of 7 is 128

subnet 2
10.0.0.128/25
network portion is 25
host portion is 32-25 = 7
2 power of 7 is 128



```