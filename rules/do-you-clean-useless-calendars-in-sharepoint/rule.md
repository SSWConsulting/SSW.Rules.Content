---
type: rule
archivedreason: 
title: Do you clean useless calendars in SharePoint?
guid: 1e12b128-b34c-4435-af21-81bdef31f061
uri: do-you-clean-useless-calendars-in-sharepoint
created: 2013-09-05T23:49:53.0000000Z
authors:
- id: 9
  title: William Yin
- id: 34
  title: Brendan Richards
related: []

---


Most SharePoint site templates contain a calendar list, this will bring lots of useless calendars.<p></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​Use the below PowerShell&#160;script to clean them&#58;<span style="line-height&#58;1.6;">​​</span></p><p class="ssw15-rteElement-CodeArea">$site = Get-SPSite(&quot;http&#58;//&lt;site collection URL&gt;/&quot;); # Specify url here​<br>​foreach ($web in $site.AllWebs) &#123;&#160; &#160;&#160;​<br>&#160; &#160; $lists = $web.Lists<br>&#160; &#160; for ($i=($lists.Count-1);$i -gt 0; $i--) &#123; &#160;<br>&#160; &#160; &#160; &#160; $list = $lists[$i]<br>&#160; &#160; &#160; &#160; #Write-host $i &#160;$list.Title $list.BaseTemplate.ToString()<br>&#160; &#160; &#160; &#160; if ($list.BaseTemplate.ToString().ToLower().contains('events')) &#123; &#160; &#160; &#160;<br>&#160; &#160; &#160; &#160; &#160; &#160; if ($list.Items.Count -eq 0)<br>&#160; &#160; &#160; &#160; &#160; &#160; &#123;​<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; Write-Host $list.Items.Count &quot;items in the list&quot; $list.Title '('$list.BaseTemplate') at '$web.Url &quot;- cleaning it!&quot;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; $list.Recycle()<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; #$list.Delete()<br>&#160; &#160; &#160; &#160; &#160; &#160; &#125;<br>&#160; &#160; &#160; &#160; &#125;<br>&#160; &#160; &#125;<br>&#125;&#160;<br></p><p>This script will put the calendars which do not have any events into <strong>Site Settings</strong> |&#160;<strong>Recycle Bin</strong>&#58;<br></p><dl class="ssw15-rteElement-ImageArea">​<img src="/PublishingImages/EmptyCalendarsInRecyckeBin.png" alt="EmptyCalendarsInRecyckeBin.png" style="margin&#58;5px;width&#58;650px;height&#58;236px;" /></dl><dd class="ssw15-rteElement-FigureNormal">​Figure&#58; Empty Calendars in Recycle Bin folder</dd><p class="ssw15-rteElement-P">​<br></p>


