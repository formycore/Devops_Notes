# Git Workflow for Updating and Pushing Changes

```markdown

This Markdown file outlines the steps to clone a repository, update it, and push changes to a new remote repository. It includes commands and explanations for each step.

## Steps to Follow

### 1. Clone the Repository

```bash
git clone https://github.com/LondheShubham153/two-tier-flask-app.git .
```

- **Explanation**: This command clones the repository from the specified URL into the current directory. The `.` at the end indicates that the contents should be placed in the current directory.

### 2. Fetch All Branches

```bash
git fetch --all
```

- **Explanation**: This command retrieves all branches and their respective commits from the remote repository without merging them into your local branches. It ensures that you have the latest updates from the remote.

### 3. Set the Remote URL

```bash
git remote set-url origin git@github.com:formycore/two-tier-app.git
```

- **Explanation**: This command changes the URL of the remote repository named `origin` to the new repository URL. This is necessary if you want to push changes to a different repository.

### 4. Verify Remote URL

```bash
git remote -v
```

- **Explanation**: This command lists all configured remote repositories along with their URLs. It helps confirm that the remote URL has been set correctly.

### 5. Push All Remote Branches

```bash
for branch in $(git branch -r | grep -v '\->' | sed 's/origin\///'); do
    git checkout $branch
    git push origin $branch
done
```

#### Breakdown of the Command

1. **`git branch -r`**: Lists all remote branches in the repository.
2. **`| grep -v '\->'`**: Filters out symbolic references (like `HEAD -> origin/main`), ensuring only actual branch names are processed.
3. **`| sed 's/origin\///'`**: Removes the `origin/` prefix from each branch name, allowing for local checkout.
4. **`$(...)`**: Captures the output of the previous commands as a list of branch names for iteration.
5. **`for branch in ...; do`**: Starts a loop that iterates over each branch name.
6. **`git checkout $branch`**: Checks out the branch currently assigned to the variable `branch`, switching your working directory to that branch.
7. **`git push origin $branch`**: Pushes the currently checked-out branch to the remote repository named `origin`.
8. **`done`**: Marks the end of the `for` loop.

### 6. Checkout a Specific Branch

```bash
git checkout <branch-name>
```

- **Explanation**: Replace `<branch-name>` with the name of the branch you want to work on. This command switches your working directory to the specified branch.

### 7. Stage Changes

```bash
git add .
```

- **Explanation**: This command stages all modified files in the current directory for the next commit. It prepares your changes to be committed.

### 8. Commit Changes

```bash
git commit -m "Your change description"
```

- **Explanation**: This command commits the staged changes with a descriptive message. Replace `"Your change description"` with a meaningful message that describes the changes made.

### 9. Push Changes to Remote Branch

```bash
git push origin <branch-name>
```

- **Explanation**: This command pushes your committed changes to the specified branch in the remote repository. Replace `<branch-name>` with the name of the branch you are pushing to.

## Error Handling

### 404: Not Found

If you encounter a `404: Not Found` error while pushing, consider the following:

- **Check Repository URL**: Ensure that the remote URL is correct and that the repository exists on GitHub.
- **Permissions**: Verify that you have the necessary permissions to push to the repository.
- **Authentication**: Make sure you are authenticated correctly with GitHub.

---

This Markdown file serves as a guide for managing your Git workflow when updating and pushing changes to a new repository.
```

You can copy and paste this content into your Markdown file. It now includes a detailed breakdown of the command used to push all remote branches.
```
## 10. Step by step process of for loop
```

 git branch -r
  origin/HEAD -> origin/main
  origin/dev
  origin/devops
  origin/feat-131-dockerize
  origin/main

 git branch -r | grep -v '\->' # -v dont show this -> kept in the \ under ''
  origin/dev
  origin/devops
  origin/feat-131-dockerize
  origin/main
git branch -r | grep -v '\->' | grep 'origin/' | sed 's/origin\///'
' # origin have / so we used \ # then it becomes sed'origin\/' 
# 's/origin\///': The s command in sed stands for substitute. It replaces the text origin/ with an empty string ().
  dev
  devops
  feat-131-dockerize
  main




$ for branch in $(git branch -r | grep -v '\->' | grep 'origin/' | sed 's/origin\///');
> do
> git checkout $branch
> git push target $branch
> done
```