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


Sometime you will need to create duplicate work item
types, e.g. a task work item may be clones as PlatformDepTask, SystemDepTask;
both of these task work items are sharing the same fields, workflow or layouts,
but they are configured to be accessible by different department or there is some other minor differences.<br><br>You should create a WIT template and use a place
holder for the difference, e.g.
<span class="ssw-rteStyle-CodeArea">&lt;WORKITEMTYPE
name=&quot;xxxxDepNamexxxxTask&quot;&gt;<br><br>&#160; …
<br><br>&lt;/WORKITEMTYPE&gt;</span><span class="ssw-rteStyle-FigureNormal">Figure&#58; WIT template with place holder&#160;
​</span>
<br><excerpt class='endintro'></excerpt><br>
<p>
Then use the following PowerShell script to automatically clone the work item and replace the placeholder with actual text. 
</p>
<span class="ssw-rteStyle-CodeArea">​$original_file = '..\WorkItem Tracking\TypeDefinitions\Task_Template_DONOTInstall.xml'<br><br>$destination_file =&#160; '..\WorkItem Tracking\TypeDefinitions\Task_&#160;PlatformDep.xml'<br>(Get-Content $original_file) | Foreach-Object &#123;<br>&#160; &#160; $_ -replace &quot;xxxxDepNamexxxx&quot;, &quot;PlatformDep&quot;<br>&#160; &#160; &#125; | Set-Content $destination_file -Encoding UTF8<br><br>$destination_file =&#160; '..\WorkItem Tracking\TypeDefinitions\Task_SystemDep.xml'<br>(Get-Content $original_file) | Foreach-Object &#123;<br>&#160; &#160;$_ -replace &quot;xxxxDepNamexxxx&quot;, &quot;SystemDep&quot;<br>&#160; &#160;&#125; | Set-Content $destination_file -Encoding UTF8</span><span class="ssw-rteStyle-FigureNormal">Figure&#58; PowerShell script&#160;to create duplicate WITs and replace the place holder with actual data</span><span class="ssw-rteStyle-Tip">​Note&#58; if you are using non-English characters in your
template, make sure you add&#160;<b class="ssw-rteStyle-Tip" style="">–Encoding UTF8&#160;</b>otherwise you will have some
encoding problems.
​​​</span><br>


