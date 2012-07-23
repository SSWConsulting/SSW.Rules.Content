---
type: rule
title: Do you use NuGet?
uri: do-you-use-nuget
created: 2012-07-23T14:35:54.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>NuGet allows you to search for, install, upgrade, configure and remove 3rd party libraries from Visual Studio projects in a consistent and easy to use manner.</p> </span>

<p>NuGet makes it easy to manage 3rd party libraries in your projects by keeping track of the library and the files needed to make it work with the concept of a package.</p>
<p>The package contains all the information needed for the 3rd party library to work with your project including any dependencies it may require.</p>
<p>The concept of a package makes it very easy to upgrade and remove the libraries in the future with a single click.</p>

<img class="ms-rteCustom-ImageArea" src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/NuGet-bad-1.jpg" alt="NuGet" />
<span class="ms-rteCustom-FigureBad">Figure&#58; Do you download a package, save it locally and then add it to your project manually?</span>

<img class="ms-rteCustom-ImageArea" src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/NuGet-good-1.jpg" alt="NuGet" />
<span class="ms-rteCustom-FigureGood">Figure&#58; Step 1 Right click on your project in visual studio and select Manage NuGet Packages</span>

<img class="ms-rteCustom-ImageArea" src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/NuGet-good-2.jpg" alt="NuGet" />
<span class="ms-rteCustom-FigureGood">Figure&#58; Step 2 find the package you want and click install</span>

<p>Now all you need to do when you want to remove or upgrade the package is go back to the NuGet package manager.</p>




