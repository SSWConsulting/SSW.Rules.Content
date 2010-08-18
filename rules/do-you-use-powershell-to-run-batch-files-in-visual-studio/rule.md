---
type: rule
archivedreason: 
title: Do you use PowerShell to run batch files in Visual Studio?
guid: 08b14dfe-0a3e-46f0-b685-9f717a97b326
uri: do-you-use-powershell-to-run-batch-files-in-visual-studio
created: 2009-05-11T09:12:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


Windows Command Processor (cmd.exe) cannot run batch files (.bat) in Visual Studio because it does not take the files as arguments. One way to run batch files in Visual Studio is to use PowerShell. 

<br><excerpt class='endintro'></excerpt><br>

  <dl class="badImage">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Image bad link" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/BadBatch_small.jpg" /> </dt>
    <dd>Bad example - Using Windows Command Processor (cmd.exe) for running batch files. </dd>
</dl>
<dl class="goodImage">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Image good link" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/goodbatch_small.jpg" /> </dt>
    <dd>Good example - Using PowerShell for running batch files</dd>
</dl>



