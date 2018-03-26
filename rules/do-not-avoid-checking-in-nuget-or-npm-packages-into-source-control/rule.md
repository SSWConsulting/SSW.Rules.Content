---
type: rule
title: Do not avoid checking in nuget or npm packages into source control?
uri: do-not-avoid-checking-in-nuget-or-npm-packages-into-source-control
created: 2018-03-26T03:23:01.0000000Z
authors: []

---



<span class='intro'> Reasons for avoiding checking Nuget or Npm packages<br><div><ol><li>Distributed version control systems, such as Git, include full copies of every version of every file within the repository. Binary files that are frequently updated lead to significant bloat and lengthens the time it takes to clone the repository.</li><li>When packages are included in the repository, developers are liable to add references directly to package contents on disk rather than referencing packages through NuGet, which can lead to hard-coded path names in the project.<br></li></ol></div> </span>

<p class="ssw15-rteElement-GreyBox"><img src="/PublishingImages/nugetpackages.png" alt="nugetpackages.png" />&#160;&#160;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58;&#160;&#160;Do not have a folder called &quot;packages&quot; or &quot;Node_Modules&quot;&#160;​<br></dd><p><br></p><p>Read more about how to&#160;​<a href="https&#58;//docs.microsoft.com/en-us/nuget/consume-packages/packages-and-source-control" target="_blank">omit&#160;NuGet packages in source control system​</a><br></p><p>For better&#160;package management&#160;,&#160;may&#160;consider using&#160;the <a href="https&#58;//docs.microsoft.com/en-us/vsts/package/overview?view=tfs-2018" target="_blank">Package Management</a> tool in TFS<br></p>


