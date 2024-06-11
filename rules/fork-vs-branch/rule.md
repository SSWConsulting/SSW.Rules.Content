---
seoDescription: When deciding whether to fork or branch a repository, consider the purpose, relationship to the original codebase, ownership, scope of changes, and collaboration aspects.
type: rule
title: Git - Do you know when to create a fork vs a branch?
uri: fork-vs-branch
authors:
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related:
  - avoid-large-prs
created: 2023-03-01T04:25:25.111Z
archivedreason: ""
guid: 7ef3fe5d-0114-49b1-98c1-fad32caafb5e
---

When starting to work on a project, it's common to wonder whether to fork an existing repository or create a new branch for it. Before making this decision, it's important to consider the key differences between the two options.

<!--endintro-->

### Figuring out whether to fork or branch

Generally, branching is a default option if you're working on a team developing a product. However, if you run into someone else's product and have new ideas you want to try, then forking is a good option because you can work on your ideas in isolation.

**Tip:** If unsure ask yourself 3 questions...  
If your answer is 'no' to any of the following questions, then you should go for a fork:

1. Do you have access to the existing repository to clone a new branch?
2. Is the change going to be part of that project and has it been approved by the Product Owner?
3. Do you or anyone you're working with on that project own the existing repository?

### Summary - Forking vs Branching

|                                           | Fork                                                                                   | Branch                                                                |
| ----------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Purpose**                               | Create a separate copy of a repository for significant changes or different directions | Develop new features or fix bugs without disrupting the main codebase |
| **Relationship to the original codebase** | Completely independent repository                                                      | Linked to the original repository                                     |
| **Ownership**                             | Owned by the user who created them                                                     | Owned by the repository owner                                         |
| **Scope of changes**                      | Typically involve significant changes                                                  | Typically involve smaller changes                                     |
| **Collaboration**                         | Used to develop ideas in isolation from the main team                                  | Used to develop ideas that the main team is working on                |
