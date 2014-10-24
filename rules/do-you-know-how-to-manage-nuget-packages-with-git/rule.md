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


​​​​Do you know the best way to manage NuGet packages with Git? You can get into all sorts of trouble by including your packages in source control.
<br><excerpt class='endintro'></excerpt><br>
<p>The following are a few issues that are related to having your NuGet packages in source control&#58;</p><ol><li>Over time the packages will grow to be too many and cloning the repository will be slow.</li><li>You could get duplicate NuGet packages in your packages folder as new versions are updated.</li><li>NuGet shows packages to update that have already been updated. This can happen if you have duplicate NuGet packages but they are different versions.</li><li>It becomes harder to &quot;clean&quot; your solution of any unused package folders, as you need to ensure you don't delete any package folders still in use.</li></ol><p>​In order to track your repositories.config and make use of NuGet Package Restore to&#160;​restore missing packages when a build begins, complete the following steps&#58;</p><ol><li>​Read the NuGet offical documentation on http&#58;//docs.nuget.org/docs/reference/package-restore</li><li>Enable NuGet Package Restore for your solution by right clicking on your solution name in the Solution Explorer&amp; and selecting Enable NuGet Package Manage Restore from the drop down menu.
   <dl class="image"><dt><img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/Pages/Do-you-know-how-to-manage-NuGet-packages-with-Git/Enable%20package%20restore%202014-10-23_17-43-13.png" alt="nuget package restore2.png" style="width&#58;489px;" /></dt></dl></li><li>Go to Team Explorer in Visual Studio and select Settings.
   <dl class="image"><dt><img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/Pages/Do-you-know-how-to-manage-NuGet-packages-with-Git/Team%20explorer%20home%202014-10-23_14-39-49.png" alt="Team explorer home" />​</dt></dl></li><li>Choose Git Settings under Git. 
   <dl class="image"><dt><img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/Pages/Do-you-know-how-to-manage-NuGet-packages-with-Git/Team-Explorer-2014-10-23_14-40-48-compressor.png" alt="Team-Explorer compressor" /></dt></dl></li><li>Choose /.gitIgnore
   <dl class="image"><dt><img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/Pages/Do-you-know-how-to-manage-NuGet-packages-with-Git/Git%20Settings%202014-10-23_14-41-22.png" alt="Git Settings" /></dt></dl></li><li>In the gitIgnore file find and uncomment the repositories.config line to include it in source control.
   <dl class="image"><dt><img src="/TFS/RulesToBetterVersionControlWithGit/PublishingImages/Pages/Do-you-know-how-to-manage-NuGet-packages-with-Git/git-ignore-image-2014-10-23_14-27-55-compressor.png" alt="git-ignore-image-compressor.png" style="width&#58;550px;" /></dt></dl></li><li>rebuild your solution and you can now safely delete your packages folder and NuGet Package Restore will restore any missing NuGet packages on each new&#160;build. You will not need to add your package folder to your repository after these steps.​​​​​​</li></ol>
​


