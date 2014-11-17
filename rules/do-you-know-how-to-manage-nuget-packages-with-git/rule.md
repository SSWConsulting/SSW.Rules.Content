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


​​​​​​Do you know the best way to manage NuGet packages with Git? You can get into all sorts of trouble by including your packages in source control.
<br><excerpt class='endintro'></excerpt><br>
<div><p>
      <br>
   </p><p><strong><strong>Do not check packages into Git</strong></strong><br></p><p>The following are a few issues that are related to having your NuGet packages in source control&#58;</p><ol><li>Over time the packages will grow to be too many and cloning the repository will be slow.</li><li>You could get duplicate NuGet packages in your packages folder as new versions are updated.</li><li>NuGet shows packages to update that have already been updated. This can happen if you have duplicate NuGet packages but they are different versions.</li><li>It becomes harder to &quot;clean&quot; your solution of any unused package folders, as you need to ensure you don't delete any package folders still in use.</li></ol>
   <br></div><div><strong>Nuget will automatically restore packages with out checking them in to source control</strong></div><div>Beginning with NuGet 2.7, the NuGet Visual Studio extension integrates into Visual Studio's build events and restores missing packages when a build begins. This feature is enabled by default and packages.config will be automatically included in souce control.</div><div></div><div>
   <br>
   <p>
      <span style="line-height&#58;20px;"><strong>Here's how it works&#58;</strong></span><br></p></div><div><ol><li>
         <span style="line-height&#58;20px;">On project or solution build, Visual Studio raises an event that a build is beginning within the solution.</span><br></li><li>
         <span style="line-height&#58;20px;">NuGet responds to this event and checks for&#160;packages.config&#160;files included in the solution.</span><br></li><li>
         <span style="line-height&#58;20px;">For each&#160;packages.config&#160;file found, its packages are enumerated and checked for existence in the solution's&#160;packages&#160;folder.</span><br></li><li>
         <span style="line-height&#58;20px;">Any missing packages are downloaded from the user's configured (and enabled) package sources, respecting the order of the package sources.</span><br></li><li>
         <span style="line-height&#58;20px;">As packages are downloaded, they are unzipped into the solution's&#160;packages&#160;folder.</span><span style="line-height&#58;20px;">​</span><br></li></ol><div><br></div><div><p><strong>Support in legacy versions of NuGet</strong></p><p>It is highly recommended that you upgrade to the latest version of NuGet to to avoid having to configure your solution to not check in NuGet pagages to source control.</p><br></div><p>You can read more here&#160;<a href="http&#58;//blogs.msdn.com/b/dotnet/archive/2013/08/22/improved-package-restore.aspx?PageIndex=3#comments" style="font-family&#58;calibri, sans-serif;font-size&#58;11pt;line-height&#58;1.6;">http&#58;//blogs.msdn.com/b/dotnet/archive/2013/08/22/improved-package-restore.aspx?PageIndex=3#comments</a>.</p>
  </div>


