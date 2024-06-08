---
type: rule
archivedreason: 
title: Do not avoid checking in nuget or npm packages into source control?
guid: e9ff253b-1587-4433-ad01-28261525f84c
uri: do-not-avoid-checking-in-nuget-or-npm-packages-into-source-control
created: 2018-03-26T03:23:01.0000000Z
authors: []
related: []
redirects: []

---

Reasons for avoiding checking Nuget or Npm packages

1. Distributed version control systems, such as Git, include full copies of every version of every file within the repository. Binary files that are frequently updated lead to significant bloat and lengthens the time it takes to clone the repository.
2. When packages are included in the repository, developers are liable to add references directly to package contents on disk rather than referencing packages through NuGet, which can lead to hard-coded path names in the project.


<!--endintro-->

![](nugetpackages.png)


::: bad
Figure:  Do not have a folder called "packages" or "Node\_Modules" 

:::



Read more about how to [omit NuGet packages in source control system](https://docs.microsoft.com/en-us/nuget/consume-packages/packages-and-source-control)

For better package management , may consider using the [Package Management](https://docs.microsoft.com/en-us/vsts/package/overview?view=tfs-2018) tool in TFS
