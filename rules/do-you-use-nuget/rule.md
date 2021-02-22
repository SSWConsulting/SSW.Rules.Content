---
type: rule
archivedreason: 
title: Do you use NuGet?
guid: 1afcf9bd-d729-490e-8553-1c890ac88557
uri: do-you-use-nuget
created: 2012-07-23T14:35:54.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

NuGet allows you to search for, install, upgrade, configure and remove 3rd party libraries from Visual Studio projects in a consistent and easy to use manner.

<!--endintro-->

NuGet makes it easy to manage 3rd party libraries in your projects by keeping track of the library and the files needed to make it work with the concept of a package.

The package contains all the information needed for the 3rd party library to work with your project including any dependencies it may require.

The concept of a package makes it very easy to upgrade and remove the libraries in the future with a single click.
![NuGet](NuGet-bad-1.jpg) Figure: Do you download a package, save it locally and then add it to your project manually? ![NuGet](NuGet-good-1.jpg) Figure: Step 1 Right click on your project in visual studio and select Manage NuGet Packages ![NuGet](NuGet-good-2.jpg) Figure: Step 2 find the package you want and click install 
Now all you need to do when you want to remove or upgrade the package is go back to the NuGet package manager.
