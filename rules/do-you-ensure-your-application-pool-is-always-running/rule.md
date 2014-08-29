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

<p>As per&#160;<a href="http&#58;//blogs.msdn.com/b/vijaysk/archive/2012/10/11/iis-8-what-s-new-website-settings.aspx">IIS 8 What's new – Website settings</a> you can use the Application Initialization feature to alleviate this behaviour. If this setting is not enabled, then IIS has default settings to spin down the application and release it from memory when it has been idle for 20 minutes.</p><p class="p1">When you set the startMode property of your application pool to AlwaysRunning a worker process is spawned as soon as IIS starts up and does not wait for the first user request. But this does not mean the web application is initialized.​</p><p class="p1">When you set preloadEnabled to true, IIS will simulate a user request to the default page (can be changed with initializationPage metabase setting) of the website/virdir so that the application initializes. The request is not logged in the IIS logs.​</p><h3 class="ssw15-rteElement-H3">IIS 8 configuration&#58;</h3><p class="p2">The feature is built-in to IIS 8</p><ol class="ol1"><li class="li2">Open Internet Information Services (IIS)</li><li class="li2">Browse to the website in question</li><li class="li2">Open Advanced settings

<dl class="image"><dt><img src="/WebSites/Rules-To-Better-IIS/Pages/ensure-your-application-pool-is-always-running.aspx?ControlMode=Edit&amp;DisplayMode=Design" alt="" /></dt><dd>Figure&#58; IIS</dd></dl></li><li class="li2">Change the “start mode” to “Always running”
<dl class="image"><dt><img src="/WebSites/Rules-To-Better-IIS/Pages/ensure-your-application-pool-is-always-running.aspx?ControlMode=Edit&amp;DisplayMode=Design" alt="" /></dt><dd>Figure&#58; Start mode</dd></dl></li><li class="li2">​Change Preload Enabled to True
<dl class="image"><dt><img src="/WebSites/Rules-To-Better-IIS/Pages/ensure-your-application-pool-is-always-running.aspx?ControlMode=Edit&amp;DisplayMode=Design" alt="" /></dt><dd>Figure&#58; Preload setting</dd></dl></li></ol>
​
<p class="p1">Can you please follow the instructions below for IIS 7.5&#58;</p><p class="p7">
   <br>
</p><ol class="ol1"><li class="li2">1.<span class="Apple-tab-span"> </span>On the application server install 
      <a href="http&#58;//www.iis.net/downloads/microsoft/application-initialization">
         <span class="s1">http&#58;//www.iis.net/downloads/microsoft/application-initialization</span></a> or it can be installed using the Web Platform installer</li><li class="li2">2.<span class="Apple-tab-span"> </span>Open 
      <strong>Internet Information Services (IIS)</strong></li><li class="li2">3.<span class="Apple-tab-span"> </span>Select the server&#160;</li><li class="li2">4.<span class="Apple-tab-span"> </span>Scroll down and select 
      <strong>Configuration Editor</strong></li></ol><p class="p7">
   <br>
</p><p class="p5">
   <br>
</p><p class="p2">
   <strong>Figure&#58; IIS</strong></p><p class="p7">
   <br>
</p><ol class="ol1"><li class="li2">5.<span class="Apple-tab-span"> </span>From the 
      <strong>Section</strong> menu select 
      <strong>system.applicationHost / applicationPools</strong></li></ol><p class="p7">
   <br>
</p><p class="p5">
   <br>
</p><p class="p2">
   <strong>Figure&#58; Configuration editor</strong></p><p class="p7">
   <br>
</p><ol class="ol1"><li class="li2">6.<span class="Apple-tab-span"> </span>Double click the 
      <strong>“…”</strong> to the right of 
      <strong>(Collection)</strong></li><li class="li2">7.<span class="Apple-tab-span"> </span>Find the Application Pool CFT is running on (it could be ComplyFirstTime or DefaultAppPool)</li><li class="li2">8.<span class="Apple-tab-span"> </span>In the 
      <strong>Properties</strong> window, scroll down and select 
      <strong>startMode</strong>, choose 
      <strong>AlwaysRunning</strong></li></ol><p class="p7">
   <br>
</p><p class="p5">
   <br>
</p><p class="p2">Figure&#58; Set “start Mode”</p><p class="p7">
   <br>
</p><ol class="ol1"><li class="li2">9.<span class="Apple-tab-span"> </span>On the top right select 
      <strong>Apply</strong></li><li class="li2">10.<span class="Apple-tab-span"> </span>There is a setting that has to be enabled in the applicationhost.config file which contains all of the top level configuration settings that IIS uses. This file is located at c&#58;\windows\system32\inetsvr\config on a standard install of IIS.</li></ol><p class="p4">I recommend making a backup of this file before continuing. You can use any text editor to update this file. Search for and locate the section named &lt;applicationPools&gt;. Within this section, you will see your application listed in this format&#58;</p><p class="p3">
   <br>
</p><p class="p4">&lt;add name=”<strong>Application Pool Name</strong>” managedRuntimeVersion=”v4.0″ /&gt;</p><p class="p7">
   <br>
</p><ol class="ol1"><li class="li2">11.<span class="Apple-tab-span"> </span>Save this file and perform an IISReset so that the change is read into the running memory of the IIS server.​</li></ol><p class="p1">
   <br>
</p>


