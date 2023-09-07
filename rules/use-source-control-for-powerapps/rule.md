---
type: rule
title: Do you use source control for your Power Apps?
uri: use-source-control-for-powerapps
authors:
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy
created: 2023-09-04T00:49:11.525Z
guid: 436f0f99-26f1-4e2e-8f0b-58c00fc3f823
---

Source control is essential for any software development project, and Microsoft Power Apps solutions are no exception. Here are some reasons why you would want to use source control like GitHub or Azure DevOps for your Power Apps projects:

- **Versioning** - Keep track of changes made to your Power Apps solutions over time.
- **Collaboration** - Enable multiple developers to work on the same Power Apps project simultaneously.
- **Audit Trail** - Maintain a history of who made what changes and when.
- **Rollback** - Easily revert to a previous version if something goes wrong.
- **Branching and Merging** - Work on new features or bug fixes in isolation before integrating them into the main project.
- **Automated Deployment** - Integrate with CI/CD pipelines for automated testing and deployment.

<!--endintro-->

### How to Implement Source Control

#### Exporting Power Apps Solution

1. **Open Power Platform CLI**: Open a terminal and navigate to your project directory.

2. **Export Solution**: Use the Power Platform CLI to export your Power Apps solution. This will create a `.zip` file or a directory structure that represents your solution.

    ```bash
    pac solution export --path ./YourSolutionName --name YourSolutionName
    ```

#### Using GitHub

1. **Initialize a Git Repository**: Navigate to your project directory and run `git init`.

    ```bash
    git init
    ```

2. **Add Remote Repository**: Add GitHub as the remote repository.

    ```bash
    git remote add origin <Your-GitHub-Repository-URL>
    ```

3. **Commit and Push**: Add your Power Apps exported solution files to the Git repository, commit them, and push to GitHub.

    ```bash
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    ```

#### Using Azure DevOps

1. **Create a New Repository**: In Azure DevOps, create a new Git repository under your project.

2. **Clone the Repository**: Clone the repository to your local machine.

    ```bash
    git clone <Your-Azure-DevOps-Repository-URL>
    ```

3. **Commit and Push**: Add your Power Apps exported solution files to the Git repository, commit them, and push to Azure DevOps.

    ```bash
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    ```

#### Importing Power Apps Solution

1. **Open Power Platform CLI**: Open a terminal and navigate to the directory where your exported solution is stored.

2. **Import Solution**: Use the Power Platform CLI to import the solution into another environment.

    ```bash
    pac solution import --path ./YourSolutionName --name YourSolutionName
    ```

By following these steps, you can implement source control for your Power Apps solutions using either GitHub or Azure DevOps. This will help you manage your project more effectively, collaborate with others, and maintain a history of your changes.
