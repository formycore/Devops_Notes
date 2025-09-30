#!/bin/bash # Specify the script should run with bash
commit=$1 # Assign the first argument to 'commit'
git add . # Stage all changes
if [ -z "$commit" ] # Check if 'commit' is empty
# demo # (Commented) Placeholder or note
# why -z ? # (Commented) Explanation for -z
# -z checks if the string is empty # (Commented) Explanation
then
    commit="update" # If empty, set default commit message
fi
git commit -m "$commit" # Commit with the message
# Make sure we are up to date before pushing
git pull origin main --rebase   # Pull latest changes and rebase

# Push only to main (Actions workflow will deploy to gh-pages)
git push origin main # Push to main branch

# 🔹 Why -z?

# -z "$commit" checks “is the string empty?”

# If you ran the script like this:

# ./myscript.sh "first commit"

# → $1 = "first commit", so -z "$commit" is false, and commit stays "first commit".

# If you ran the script with no argument:

# ./myscript.sh

# → $1 is empty, so -z "$commit" is true, and commit becomes "update".