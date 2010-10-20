---
type: rule
archivedreason: 
title: Do you disable connections?
guid: 320b6c73-b779-4bae-80f9-eb84235aeb1b
uri: do-you-disable-connections
created: 2009-11-03T21:28:04.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---



  <p>Once you are ready to start you need to make sure that no one can access the existing TFS 2008 server while you do the migration.</p>
<ol>
    <li>You are ready to start </li>
    <li>Send out an email notifying all users that TFS2008 will be turned off.&#160;<br>
    Follow <span><a shape="rect" href="http&#58;//www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart" target="_blank">Rules to better Networks</a></span> </li>
    <li>Turn off the TFS Services so no one can check in files
    <ol>
        <li>Remote desktop into TFS 2008 </li>
        <li>Start IIS </li>
        <li>Right click Team Foundation Server | Stop <br>
        <span><img style="width&#58;500px;height&#58;412px;" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/StopTFSServices.png" /></span><br>
        <span style="font-size&#58;12px;font-weight&#58;bold;">Figure&#58;&#160;You need to stop anyone checking in files</span>&#160; </li>
    </ol>
    </li>
    <li>Confirm you can no longer get latest on the Northwind team project </li>
</ol>

<br><excerpt class='endintro'></excerpt><br>



