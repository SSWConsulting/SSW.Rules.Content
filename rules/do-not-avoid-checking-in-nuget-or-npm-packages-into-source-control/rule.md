---
type: rule
title: Do not avoid checking in nuget or npm packages into source control?
uri: do-not-avoid-checking-in-nuget-or-npm-packages-into-source-control
created: 2018-03-26T03:23:01.0000000Z
authors: []

---



<span class='intro'> Reasons for avoiding checking Nuget or Npm packages<br><div><br></div><div><ol><li>Distributed version control systems, such as Git, include full copies of every version of every file within the repository. Binary files that are frequently updated lead to significant bloat and lengthens the time it takes to clone the repository.</li><li>When packages are included in the repository, developers are liable to add references directly to package contents on disk rather than referencing packages through NuGet, which can lead to hard-coded path names in the project.<br></li></ol><div><br></div></div> </span>

<p>​<br><img src="/PublishingImages/nugetpackages.png" alt="nugetpackages.png" style="margin&#58;5px;padding&#58;15px;border-width&#58;1px;border-style&#58;solid;border-color&#58;#cccccc;background&#58;#eeeeee;overflow-x&#58;auto;display&#58;block;font-size&#58;1rem;font-weight&#58;bold;" /><span style="color&#58;#333333;font-size&#58;16px;font-weight&#58;700;">&#160;</span><span style="color&#58;#333333;font-size&#58;16px;font-weight&#58;700;">&#160;Figure&#58;&#160;</span><span style="color&#58;#333333;font-size&#58;16px;font-weight&#58;700;"></span><span style="color&#58;#333333;font-size&#58;16px;font-weight&#58;700;">&#160;Do not have a folder called &quot;packages&quot; or &quot;Node_Modules&quot;&#160;</span>​<br></p><p><a href="https&#58;//docs.microsoft.com/en-us/nuget/consume-packages/packages-and-source-control">Omitting NuGet packages in source control systems​​</a><br></p><p><br></p>


