---
seoDescription: Staying up-to-date with NuGet package updates ensures improved stability and reduced risk of breaking changes or regressions.
type: rule
title: Do you update your packages regularly?
uri: do-you-update-your-packages-regularly
authors:
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
  - title: Zach Keeping
    url: https://www.ssw.com.au/people/zach-keeping
related: []
redirects: []
created: 2014-11-27T18:18:39.000Z
archivedreason: null
guid: eed63bcd-bdd8-47ed-baf2-8200f9f99547
---

NuGet makes it easy to find and apply package updates – but this still must be performed manually.

<!--endintro-->

Each package update should contain improvements but also involves a small amount of risk in the form of breaking changes or regressions.

Updating often can help mitigate this risk by ensuring that each individual update is smaller.

Recommended practice is to apply package updates at the start of a Sprint so that there is time to find and resolve issues introduced by the update.

![Figure: NuGet package updates](update-nuget.png)

### Updating packages

#### Visual Studio GUI

In Visual Studio, the **NuGet Package Manager** will give you a count of how many outdated packages are present in your solution and allow you to update these packages.

![Figure: The NuGet Package Manager in Visual Studio displays a convenient badge with the amount of outdated packages (2 in this example)](update-count.png)

#### CLI

If using the command line, you can use the following command to print the outdated packages in your solution:

```shell
dotnet list package --outdated
```

Outdated packages can then be updated by running the follow command, specifying the package and desired version:

```shell
dotnet add package <PACKAGE_NAME> -v <VERSION>
```

#### Package Manager Console

Visual Studio also provides a convenient command line tool for managing and updating packages using PowerShell, which allows for updating all packages easily. To access it, first open the Package Manager Console

**Tools | NuGet Package Manager | Package Manager Console**

![Figure: The Package Manager Console allows for easy management of packages using the command line](package-manager-console.png)

Now enter the following command:

```shell
Update-Package
```

This will update all packages in every project of your solution in one command.

To check for updates, you can use the following command:

```shell
Get-Package -Updates
```

Specific packages can be updated by specifying the package name:

```shell
Update-Package <PACKAGE_NAME>
```
