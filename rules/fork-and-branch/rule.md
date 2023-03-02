---
type: rule
title: Git - Do you know when to create a fork or a branch?
uri: fork-and-branch
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
  - title: Christian Morford-Waite
    url: https://www.ssw.com.au/people/christian-morford-waite
related: []
created: 2023-03-01T04:25:25.111Z
archivedreason: ""
guid: 7ef3fe5d-0114-49b1-98c1-fad32caafb5e
---
<!--StartFragment-->

When starting to work on a project, it's common to wonder whether to fork an existing repository or create a new branch for it. In making this decision, it's important to consider the key differences between the two options.

### <!--EndFragment-->

<!--StartFragment-->

When you want to work on someone's repository without affecting the original code, it is recommended to create a fork of the repository. This allows you to make changes to the code in your own copy, collaborate with others, and submit pull requests to merge your changes back into the original repository.

<!--EndFragment-->

### Tip

<!--StartFragment-->

If your answer is 'no' to any of the following questions, then you should go for a fork:

<!--EndFragment-->

<!--StartFragment-->

1. Do you have access to the existing repository to clone a new branch?
2. Is the change going to be part of that project and has it been approved by the product owner?
3. Do you or anyone you're working with on that project own the existing repository?

<!--EndFragment-->

<!--StartFragment-->

<!--StartFragment-->

The following table summarizes the main differences between forking and branching a repository

<!--EndFragment-->

<!--EndFragment-->

<!--StartFragment-->

|                                           | Fork                                                                                   | Branch                                                                    |
| ----------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Purpose**                               | Create a separate copy of a repository for significant changes or different directions | Develop new features or fix bugs without disrupting the main codebase     |
| **Relationship to the original codebase** | Completely independent                                                                 | Parallel version of the original repository                               |
| **Ownership**                             | Owned by the user who created them                                                     | Owned by the repository owner                                             |
| **Scope of changes**                      | Can involve significant changes to the codebase                                        | Typically involve smaller changes                                         |
| **Collaboration**                         | Can be used to collaborate with others who have different ideas for the project        | Can be used to collaborate with team members working on the same codebase |
| **Integration**                           | Require a pull request to merge changes back into the original repository              | Can be merged directly into the main codebase                             |
| **Visibility**                            | Can be public or private                                                               | Typically only visible to those with access to the repository             |

<!--EndFragment-->