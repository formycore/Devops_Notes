#!/bin/bash
start_folder_name=$2
end_folder_name=$3
day_name=$1
for i in $(seq "${start_folder_name}" "${end_folder_name}");
do
    mkdir "${day_name}${i}"
done