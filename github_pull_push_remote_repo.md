If you want to clone all branches from the remote repository to your local system and then push them to your own remote repository, you can follow these steps:

Clone the Remote Repository:
Open a terminal or command prompt on your system and use the following command to clone the remote repository:

```
git clone https://github.com/formycore/boardgame_github_actions.git
cd Boardgame

Fetch All Branches:
Fetch all branches from the remote repository:

git fetch --all
List All Remote Branches:
You can list all remote branches to confirm that you have fetched them:
git branch -r

Checkout Each Branch and Push:
For each branch you want to push to your own remote repository, you need to checkout the branch and then push it:

git checkout <branch_name>
git push <your_remote_name> <branch_name>
Replace <branch_name> with the name of the branch you want to push and <your_remote_name> with the name of your own remote repository.

Repeat this step for each branch you want to push.

After completing these steps, all branches from the remote repository will be cloned to your local system and pushed to your own remote repository under the same branch names.
```
