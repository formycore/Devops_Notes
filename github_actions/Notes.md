# Deploying a React App to GitHub Pages using GitHub Actions

This guide explains how to deploy your React application to GitHub Pages automatically using GitHub Actions.

## Prerequisites

- A GitHub repository containing your React app (created with Create React App).
- The `homepage` field set in your `package.json` (e.g., `"homepage": "https://<username>.github.io/<repo-name>"`).

## Steps

### 1. Create a GitHub Actions Workflow

- In your repository, create the directory `.github/workflows/` if it doesn't exist.
- Add a workflow file, e.g., `demo.yml`.

### 2. Configure the Workflow

- The workflow should:
  - Trigger on pushes to the `main` branch.
  - Set up Node.js.
  - Install dependencies.
  - Build the React app.
  - Deploy the `build` folder to the `gh-pages` branch using the `JamesIves/github-pages-deploy-action`.

### 3. Example Workflow

See `.github/workflows/demo.yml` in this repo for a working example.

### 4. Enable GitHub Pages

- Go to your repository's Settings > Pages.
- Set the source branch to `gh-pages` and the folder to `/ (root)`.

### 5. Commit and Push

- Push your code to the `main` branch.
- The workflow will run and deploy your app to GitHub Pages.

### 6. Access Your Site

- Visit `https://<username>.github.io/<repo-name>` to see your deployed app.

---

**References:**
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [JamesIves/github-pages-deploy-action](https://github.com/JamesIves/github-pages-deploy-action)