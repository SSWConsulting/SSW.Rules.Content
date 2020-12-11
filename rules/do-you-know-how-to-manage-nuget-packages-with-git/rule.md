---
type: rule
archivedreason: 
title: Do you know how to manage NuGet packages with Git?
guid: eb767a37-edb7-44cd-981a-5207fafa41e5
uri: do-you-know-how-to-manage-nuget-packages-with-git
created: 2014-10-23T04:30:48.0000000Z
authors:
- id: 38
  title: Drew Robson
- id: 44
  title: Duncan Hunter
related: []

---

Do you know the best way to manage NuGet packages with Git? You can get into all sorts of trouble by including your packages in source control. 
<!--endintro-->




** Do not check packages into Git **

The following are a few issues that are related to having your NuGet packages in source control:

1. Over time the packages will grow to be too many and cloning the repository will be slow.
2. You could get duplicate NuGet packages in your packages folder as new versions are updated.
3. NuGet shows packages to update that have already been updated. This can happen if you have duplicate NuGet packages but they are different versions.
4. It becomes harder to "clean" your solution of any unused package folders, as you need to ensure you don't delete any package folders still in use.




 **Nuget will automatically restore packages with out checking them in to source control** 

Beginning with NuGet 2.7, the NuGet Visual Studio extension integrates into Visual Studio's build events and restores missing packages when a build begins. This feature is enabled by default and packages.config will be automatically included in souce control.





**Here's how it works:**



1. On project or solution build, Visual Studio raises an event that a build is beginning within the solution.
2. NuGet responds to this event and checks for packages.config files included in the solution.
3. For each packages.config file found, its packages are enumerated and checked for existence in the solution's packages folder.
4. Any missing packages are downloaded from the user's configured (and enabled) package sources, respecting the order of the package sources.
5. As packages are downloaded, they are unzipped into the solution's packages folder.






**Support in legacy versions of NuGet**

It is highly recommended that you upgrade to the latest version of NuGet to to avoid having to configure your solution to not check in NuGet pagages to source control.



You can read more here [http://blogs.msdn.com/b/dotnet/archive/2013/08/22/improved-package-restore.aspx?PageIndex=3#comments](http&#58;//blogs.msdn.com/b/dotnet/archive/2013/08/22/improved-package-restore.aspx?PageIndex=3#comments).
