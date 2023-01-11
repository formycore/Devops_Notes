# Attach disk to aws
- create a new volume 
```
aws ec2 create-volume \
> --volume-type gp2 \
> --size 1 \
> --availability-zone ap-south-1b \
> --tag-specification 'ResourceType=volume,Tags=[{Key=Check,Value=demo}]'
```
- connect to the server 
- to see the partition
```lsblk```
- to attach the disk, note the availibilty zone of the server, volume should in the same zone only
- select the volume
  - Actions
  - Attach volume
  - select the instance
  - Name it (it will be the name of the disk, but it shows that recommended name is d-p for data centers)
  - sdb
- s will be replaced with xv once attached to the server
- check the disk size, other disks
```df -hT```
- T is for type
- newly create disk is not availaible
- we need to mount that
##  create a mount point and attach that to disk
  - here we have partition, but not a file system
  - we need to formated with xfs files system
  ```
  sudo mkfs -t <file system> /path
  sudo mkfs -t xfs /dev/xvdf 
  ```
  - to check the file system of the /dev/xvdf 
  ```sudo lsblk -f```
-----------------------------------------------------------------------
# After reboot the mount point will lost
# to make it permanent, add the uuid to the /etc/fstab
use tabs here
vi /etc/fstab
UUID= <mount_point> <file_system> defaults
