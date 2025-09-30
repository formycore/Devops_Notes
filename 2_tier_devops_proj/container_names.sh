#!/bin/bash
containers=($(docker ps | awk 'NR>1 {print $NF}'))
for c in "${containers[@]}";
do
 if [ "$c"= "mysql" ];
 then 
   continue
  fi
 echo "$c"
 docker stop "$c"
 #docker rm "$c"
done

