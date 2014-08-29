---
type: rule
title: Do you ensure your application pool is always running?
uri: do-you-ensure-your-application-pool-is-always-running
created: 2014-08-29T18:48:34.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> <p class="p1">Do users complain that at times their web application appears to be slow to run at times. The issue can be related to after IIS application pool recycles/reboots/crashes and the application pools are not automatically loaded back into into memory e.g. The first user in the morning complains about excessive load times for their web application.</p> </span>

<p>As per&#160;<a href="http&#58;//blogs.msdn.com/b/vijaysk/archive/2012/10/11/iis-8-what-s-new-website-settings.aspx">IIS 8 What's new – Website settings</a> you can use the Application Initialization feature to alleviate this behaviour. If this setting is not enabled, then IIS has default settings to spin down the application and release it from memory when it has been idle for 20 minutes.</p><p class="p1">When you set the startMode property of your application pool to AlwaysRunning a worker process is spawned as soon as IIS starts up and does not wait for the first user request. But this does not mean the web application is initialized.​</p><p class="p1">When you set preloadEnabled to true, IIS will simulate a user request to the default page (can be changed with initializationPage metabase setting) of the website/virdir so that the application initializes. The request is not logged in the IIS logs.​</p><h3>IIS 8 configuration&#58;</h3><p class="p2">The feature is built-in to IIS 8</p><ol class="ol1"><li class="li2">Open Internet Information Services (IIS)</li><li class="li2">Browse to the website in question</li><li class="li2">Open Advanced settings 
      <dl class="image"><dt> 
            <img src="/PublishingImages/iis8-1.jpg" alt="" /> 
         </dt><dd>Figure&#58; IIS</dd></dl></li><li class="li2">Change the “start mode” to “Always running” 
      <dl class="image"><dt> 
            <img src="/PublishingImages/iis8-2.jpg" alt="" /> 
         </dt><dd>Figure&#58; Start mode</dd></dl></li><li class="li2">​Change Preload Enabled to True 
      <dl class="image"><dt> 
            <img src="/PublishingImages/iis8-3.jpg" alt="" /> 
         </dt><dd>Figure&#58; Preload setting</dd></dl></li></ol> ​ 
<h3>Instructions below for IIS 7.5&#58;</h3>​ 
<ol class="ol1"><li class="li2">On the application server install 
      <a href="http&#58;//www.iis.net/downloads/microsoft/application-initialization"> 
         <span class="s1">http&#58;//www.iis.net/downloads/microsoft/application-initialization</span></a> or it can be installed using the Web Platform installer</li><li class="li2">Open 
      <strong>Internet Information Services (IIS)</strong></li><li class="li2">Select the server&#160;</li><li class="li2">Scroll down and select 
      <strong>Configuration Editor</strong> 
      <dl class="image"><dt> 
            <img src="/PublishingImages/iis7-1.jpg" alt="" /> 
         </dt><dd>Figure&#58; IIS</dd></dl></li><li class="li2">From the 
      <strong>Section</strong> menu select 
      <strong>system.applicationHost / applicationPools</strong> 
      <dl class="image"><dt> 
            <img src="/PublishingImages/iis7-2.jpg" alt="" /> 
         </dt><dd>Figure&#58; Configuration editor</dd></dl></li><li class="li2">Double click the 
      <strong>“…”</strong> to the right of 
      <strong>(Collection)</strong></li><li class="li2">Find the Application Pool CFT is running on (it could be ComplyFirstTime or DefaultAppPool)</li><li class="li2">In the 
      <strong>Properties</strong> window, scroll down and select 
      <strong>startMode</strong>, choose 
      <strong>AlwaysRunning</strong> 
      <dl class="image"><dt> 
            <img src="/PublishingImages/iis7-3.jpg" alt="" /> 
         </dt><dd>Figure&#58; Set &quot;start Mode&quot;</dd></dl></li><li class="li2">On the top right select 
      <strong>Apply</strong></li><li>There is a setting that has to be enabled in the applicationhost.config file which contains all of the top level configuration settings that IIS uses. This file is located at c&#58;\windows\system32\inetsvr\config on a standard install of IIS. 
      <p class="p4">I recommend making a backup of this file before continuing. You can use any text editor to update this file. Search for and locate the section named &lt;applicationPools&gt;. Within this section, you will see your application listed in this format&#58;</p><p class="ssw15-rteElement-CodeArea">&lt;add name=”Application Pool Name” managedRuntimeVersion=”v4.0″ /&gt;​</p></li><li class="li2">Save this file and perform an IISReset so that the change is read into the running memory of the IIS server.​</li></ol> ​


