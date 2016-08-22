---
type: rule
archivedreason: 
title: Do you use the best deployment tool?
guid: 7af442fc-db9a-43d2-afdd-7dfcbeb50f89
uri: do-you-use-the-best-deployment-tool
created: 2015-01-02T01:35:53.0000000Z
authors:
- id: 23
  title: Damian Brady
- id: 1
  title: Adam Cogan
related:
- do-you-know-when-to-use-an-on-premises-build-server-with-visual-studio-online
- do-you-estimate-all-tasks-at-the-start-of-the-sprint
- do-you-use-the-lifecycles-feature-in-octopus-deploy

---


Often, deployment is either done manually&#160;or as part of the build process. But deployment is a completely different step in your lifecycle. It's important that deployment is automated, but done&#160;separately&#160;from the build process.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>There are two main reasons you should separate your deployment from your build process&#58;</p><ol><li>
      <span style="line-height&#58;20.8px;">You're not dependent on your servers for your build to succeed. Similarly, if you need to change deployment locations, or add or remove servers, you don't have to edit your build definition and risk breaking your build.<br></span></li><li>
      <span style="line-height&#58;20.8px;">You want to make sure you're deploying the <strong>*same*</strong>&#160;(tested)&#160;build of your software to each environment. If your deployment step is part of your build step, you may be rebuilding each time you deploy to a new environment.</span></li></ol><div>
   <span style="line-height&#58;20.8px;">The best tool for&#160;deployments is <a href="http&#58;//octopusdeploy.com/">Octopus Deploy </a>.</span></div><dl class="image"><dt> <img src="/PublishingImages/SugarLearningOctopus.png" alt="SugarLearningOctopus.png" style="margin&#58;5px;width&#58;550px;" /> </dt><dd> Figure&#58; Good Example - SSW uses Octopus Deploy to deploy Sugar Learning</dd></dl><p>Octopus Deploy allows you to package your projects in Nuget packages, publish them to the Octopus server, and deploy&#160;the package to your configured environments. Advanced users can also perform other tasks as part of a deployment like&#160;running&#160;integration and smoke tests, or&#160;notifying&#160;third-party services of a successful deployment.</p><p> 
   <a href="http&#58;//octopusdeploy.com/blog/2.6">Version 2.6 of Octopus Deploy</a> introduced the ability to create&#160;a new release and trigger a deployment when a new package is pushed to the Octopus server. Combined with Octopack, this makes continuous integration very easy from Team Foundation Server.</p><h3>What if you need to sync files manually?<br></h3><p>Then you should use an FTP client, which allows you to update files you have changed. <b>FTP Sync</b> and <b>Beyond Compare</b> are recommended as they compare all the files on the web server to a directory on a local machine, including date updated, file size and report which file is newer and what files will be overridden by uploading or downloading. you should only make changes on the local machine, so we can always upload files from the local machine to the web server.&#160;</p><p>This process allows you to keep a local copy of your live website on you machine - a great backup as a side effect.&#160;</p><p>Whenever you make changes on the website, as soon as they are approved they will be uploaded. You should tick the box that says &quot;sync sub-folders&quot;, but when you click sync be careful to check any files that may be marked for a reverse sync. You should reverse the direction on these files. For most general editing tasks, changes should be uploaded as soon as they are done. Don't leave it until the end of the day. You won't be able to remember what pages you've changed. And when you upload a file, you should sync EVERY file in that directory. It's highly likely that un-synced files have been changed by someone, and forgotten to be uploaded. And make sure that deleted folders in local server &#160;are deleted in remote server.&#160;<br></p><dl class="image"><dt><img src="/PublishingImages/ticksubfolders.jpg" alt="ticksubfolders.jpg" style="width&#58;750px;" /> </dt> </dl>
<p>If you are working on some files that you do not want to&#160;sync then put a <b>_DoNotSyncFilesInThisFolder_XX.txt </b>file in the folder. (Replace XX with your initials.) So if you see files that are to be synced (and you don't see this file) then find out who did it and tell them to sync. The reason you have this TXT file is so that people don't keep telling the web</p><p>
   <b> NOTE&#58; </b>Immediately before deployment of an ASP.NET application with FTPSync, you should ensure that the application compiles - otherwise it will not work correctly on the destination server (even though it still works on the development server).</p>


