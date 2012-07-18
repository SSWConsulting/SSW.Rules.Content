---
type: rule
archivedreason: 
title: Do you use PowerShell script to create duplicated work item types?
guid: 966ffc8c-7734-4557-8511-75e80e9b67c8
uri: do-you-use-powershell-script-to-create-duplicated-work-item-types
created: 2012-07-18T07:41:10.0000000Z
authors:
- id: 10
  title: Lei Xu
related: []

---


<p class="MsoListParagraph">Sometime you will need to create duplicate work item
types, e.g. a task work item may be clones as PlatformDepTask, SystemDepTask;
both of these task work items are sharing the same fields, workflow or layouts,
but they are configured to be accessible by different department or some other
difference. </p>

<p class="MsoListParagraph">&#160;</p>

<p class="MsoListParagraph">You should create a WIT template and use a place
holder for the difference, e.g.<br><p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&lt;WORKITEMTYPE
name=&quot;xxxxDepNamexxxxTask&quot;&gt;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">…</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;10pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&lt;/WORKITEMTYPE&gt;</span></p>

<p class="MsoListParagraph">Figure&#58; WIT template with place holder&#160;</p></p>
<br><excerpt class='endintro'></excerpt><br>
​<span style="background-color&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">$original_file = '..\WorkItem
Tracking\TypeDefinitions\Task_Template_DONOTInstall.xml'</span>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&#160;</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">$destination_file =&#160; '..\WorkItem
Tracking\TypeDefinitions\Task_</span> PlatformDep<span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">.xml'</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">(Get-Content $original_file) | Foreach-Object &#123;</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&#160;&#160;&#160; $_ -replace
&quot;xxxxDepNamexxxx&quot;, &quot;</span>PlatformDep<span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&#160;&#160;&#160; &#125; | Set-Content $destination_file
-Encoding UTF8</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&#160;</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">$destination_file =&#160; '..\WorkItem
Tracking\TypeDefinitions\Task_</span>SystemDep<span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">.xml'</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">(Get-Content $original_file) | Foreach-Object &#123;</span></p>

<p class="MsoNormal" style="margin-left&#58;36pt;"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&#160;&#160;&#160; $_ -replace &quot;xxxxDepNamexxxx&quot;,
&quot;</span>SystemDep<span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&quot;</span></p>

<p class="MsoListParagraph"><span style="font-size&#58;9.5pt;font-family&#58;consolas;color&#58;black;background-color&#58;white;">&#160;&#160;&#160; &#125; |
Set-Content $destination_file -Encoding UTF8</span></p>

<p class="MsoListParagraph">Figure&#58; PowerShell script to create duplicate WITs
and replace the place holder with actual data </p>

<p class="MsoListParagraph">&#160;</p>

<p class="MsoListParagraph">Note&#58; if you are using non-English characters in your
template, make sure you add <b>–Encoding UTF8</b> otherwise you will have some
encoding problems. </p>

<p class="MsoNormal">&#160;</p>



