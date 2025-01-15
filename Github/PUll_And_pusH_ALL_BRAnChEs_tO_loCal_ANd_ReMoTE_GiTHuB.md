# All branches are pulled from the source repo and pushed to the remote repository, follow these steps:

## 1_Clone the source repository:
```
git clone https://github.com/londheShubham153/wanderlust.git
cd wanderlust
```
## 2.Add the target repository as a remote:

```
git remote add target https://github.com/formycore/branches.git 
or with ssh

```
## 3.Fetch all branches from the source repository:
```
git fetch origin
```
## 4.Push each branch to the target repository:
```
for branch in $(git branch -r | grep -v '\->' | grep 'origin/' | sed 's/origin\///'); do
    git checkout $branch
    git push target $branch
done
```
## 5.Step by step process of for loop
```

 git branch -r
  origin/HEAD -> origin/main
  origin/dev
  origin/devops
  origin/feat-131-dockerize
  origin/main
  target/main

 git branch -r | grep -v '\->' # -v dont show this -> kept in the \ under ''
  origin/dev
  origin/devops
  origin/feat-131-dockerize
  origin/main
  target/main

git branch -r | grep -v '\->' | sed 's/origin\///' # origin have / so we used \ # then it becomes sed'origin\/' 
# 's/origin\///': The s command in sed stands for substitute. It replaces the text origin/ with an empty string ().
  dev
  devops
  feat-131-dockerize
  main
  target/main
- SEE here we are getting the target/main also we only need starting with origin so 

git branch -r | grep -v '\->' | grep 'origin/' | sed 's/origin\///'

$ for branch in $(git branch -r | grep -v '\->' | grep 'origin/' | sed 's/origin\///');
> do
> git checkout $branch
> git push target $branch
> done
Switched to a new branch 'dev'
branch 'dev' set up to track 'origin/dev'.
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (7/7), 1.18 KiB | 1.18 MiB/s, done.
Total 7 (delta 3), reused 7 (delta 3), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote:
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/formycore/all_branches/pull/new/dev
remote:
To github.com:formycore/all_branches.git
 * [new branch]      dev -> dev
Switched to a new branch 'devops'
branch 'devops' set up to track 'origin/devops'.
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (1/1), done.
Writing objects: 100% (3/3), 548 bytes | 548.00 KiB/s, done.
Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'devops' on GitHub by visiting:
remote:      https://github.com/formycore/all_branches/pull/new/devops
remote:
To github.com:formycore/all_branches.git
 * [new branch]      devops -> devops
Switched to a new branch 'feat-131-dockerize'
branch 'feat-131-dockerize' set up to track 'origin/feat-131-dockerize'.
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'feat-131-dockerize' on GitHub by visiting:
remote:      https://github.com/formycore/all_branches/pull/new/feat-131-dockerize
remote:
To github.com:formycore/all_branches.git
 * [new branch]      feat-131-dockerize -> feat-131-dockerize
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
Everything up-to-date

```