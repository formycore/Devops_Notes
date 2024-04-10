#!/bin/bash
# Destination Repo 
source_repo="https://github.com/jaiswaladi246/Microservice.git"
destination_repo="https://github.com/formycore/devops_shack_11_microservices.git"

# Destination to clone the repo

git clone $source_repo 
cd Microservice


# Fetch all the branches from the source repo
git fetch --all

for branch in $(git branch -r | grep -v '\->'); do
    branch_name="${branch##*/}"
    git checkout -b "$branch_name" "$branch"
    echo "-----------------------------------------"
    echo "the branch name is $branch_name"
    echo "-----------------------------------------"
    git push "$destination_repo" "$branch_name"
done    