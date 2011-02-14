---
type: rule
archivedreason: 
title: Do you name your Virtual Machines with a standadized naming convention?
guid: 95d89bf5-a456-4ccf-b636-5bd7e56300f6
uri: do-you-name-your-virtual-machines-with-a-standadized-naming-convention
created: 2011-02-14T05:06:05.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---


When your Hyper-V environment is spread across multiple hosts and contains many Virtual Servers, it can get very confusing to find the one you are looking for&#160;amongst them all. This is why you should use a standard naming convention for all your Virtual machines.

<br><excerpt class='endintro'></excerpt><br>

  <img alt="How do you know what machine is what?" src="/PublishingImages/naming-badexample.jpg" />
  <br>
<strong class="ms-rteCustom-FigureBad">Bad Example - How do you know what machine is what?</strong>The standard we use for Production Virtual Machine naming is as follows&#58;<br>
<br>
<strong>&#160;&#160;&#160;&#160;NetBIOSName-ServiceName<br>
<br>
&#160;&#160;&#160;&#160;</strong>For example&#58; <strong>Falcon-SCVMM<br>
</strong><br>
The standard we use for Development Virtual Machine naming is as follows&#58;<br>
<br>
&#160;&#160;&#160;&#160;<strong>DEV-NetBIOSName-ServiceName-DeveloperInitials<br>
</strong><br>
&#160;&#160;&#160;&#160;For example&#58;&#160;<strong>DEV-demo2010a-SP2010MSInfoWorker-JL</strong><br>
<br>
<img alt="It is easy to tell which VM is which when they are named to a standard" src="/PublishingImages/naming-goodexample.jpg" /><br>
<font class="ms-rteCustom-FigureGood" size="+0">Good Example - It is easy to tell which VM is which when they are named to a standard<br>
</font>



