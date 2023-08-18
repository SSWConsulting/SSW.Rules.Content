---
type: rule
title: Project setup - Do you make project setup as easy as possible?
uri: project-setup
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related:
  - awesome-documentation
redirects:
  - do-you-make-instructions-at-the-beginning-of-a-project-and-improve-them-gradually
created: 2009-05-13T06:12:34.000Z
archivedreason: null
guid: 3f837d99-dd94-4f21-8b07-7348151fb89d
---
Developers understand the [importance of the F5 experience](/developer-experience). Sadly, lots of projects are missing key details that are needed to make setup easy.

Let's look at the ways to optimize the experience. There are 4 levels of experience that can be delivered to new developers on a project:

<!--endintro-->

::: img-small
![](f5-key.png)
:::

### Level 1: Step by step documentation

This is the most important milestone to reach because it contains the bare minimum to inform developers about how to run a project.

The rule on [awesome documentation](/awesome-documentation) teaches us all the documents needed for a project and how to struture them.

The **README.md** and **Instructions-Compile.md** are the core documents that are essential for devs to get running on a project.

::: bad
![Bad example - A project without instructions](ProjectDocumentationBadExample.png)
:::

::: good
![Good example - A project with instructions](ProjectDocumentationGoodExample.png)
:::

::: greybox
**Tip:** In addition to pre-requisites, make sure to mention what isn't supported and any other problems that might come up.

E.g. Problems to check for:

* Windows 8 not supported
* Latest backup of the database
* npm version
  :::

::: greybox
**Tip:** Don't forget about the database, your developers need to know how to work with the database

![Figure: Don't forget about the database!](EFCoreMigrations.png)

:::

### Level 2: Less documentation using a PowerShell script

A perfect solution would need no static documentation. Perfect code would be so self-explanatory that it did not need comments. The same rule applies with instructions on how to get the solution compiling. A PowerShell script is the first step towards this nirvana.

**Note:** You should be able to get latest and compile within 1 minute. Also, a developer machine should **not have** to be on the domain (to support external consultants)

All manual workstation setup steps should be scripted with PowerShell, as per the below example:

::: greybox 

```powershell
PS C:\Code\Northwind&gt; **.\Setup-Environment.ps1**
```

**Problem:** Azure environment variable run state directory is not configured `\_CSRUN\_STATE\_DIRECTORY`.

**Problem:** Azure Storage Service is not running. Launch the development fabric by starting the solution.

**WARNING:** Abandoning remainder of script due to critical failures.

To try and automatically resolve the problems found, re-run the script with a `-Fix` flag.

:::

::: good
**Figure: Good example - A PowerShell script removes human error and identifies problems in the devs environment so they can be fixed**
:::

### Level 3: Less maintenance using Docker containerization

![Figure: Docker Logo](docker-logo.png)

PowerShell scripts are cool, but they can be difficult to maintain and they cannot account for all the differences within each developers environment. This problem is exacerbated when a developer comes back to a project after a long time away.

Docker can solve this problem and make the experience even better for your developers. Docker containerization helps to standardize development environments. By using docker containers developers won't need to worry about the technologies and versions installed on their device. Everything will be set up for them at the click of a button.

Learn more: [Project setup - Do you use Docker to containerize your SQL Server environment?](/containerize-sql-server)

### Level 4: More standardization using dev containers

Dev containers take the whole idea of docker containerization to another level. By setting up a repo to have the right configuration, the dev team can be certain that every developer is going to get the exact same experience. 

Learn more: [Project setup - Do you containerize your dev environment?](/dev-containers)

::: good
![Figure: Good example - After using dev containers you would be as happy as Larry!](HappyDevs.png)
:::
