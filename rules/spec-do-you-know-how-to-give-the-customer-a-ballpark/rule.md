---
type: rule
archivedreason: 
title: Spec - Do you know how to give the customer a ballpark?
guid: 1ac29d3d-fc89-462a-b0c5-d17c6889e66c
uri: spec-do-you-know-how-to-give-the-customer-a-ballpark
created: 2009-11-04T08:35:51.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
- title: Justin King
  url: https://ssw.com.au/people/justin-king
related: []
redirects: []

---


<p><strong>How to create an Estimate For a Spec Review (Summary)</strong><strong><br></strong></p>
<p>This process can take up to a few days, so if you're just after a ballpark, use epics instead of PBIs (Product Backlog Items).</p>
<ol><li>Usually using the browser, list all of the PBIs in TFS, sizing them with story points.</li>
<li>Using Visual Studio, export the list of PBIs and Story Points to Excel.<br></li>
<li>In Excel, add a column called &quot;Hours&quot;​<br>Note&#58; Once we move to estimating in time, this is no longer Scrum.<br></li>
<li>In Excel, copy this list and paste into&#160;another spreadsheet called the <img title="Excel File" src="/Style%20Library/SSW/CoreImages/iconXls.png" alt="" /> <a href="/Documents/4.%20Estimates%20Calculator.xlsx?d=w6f09d6a75d074fbda81e5e5dd3e18c76" target="_blank" shape="rect">Estimates&#160;Calcul​ator</a>,&#160;in order to add all of the extra items (testing, DevOps,&#160;Project management, etc.).<br>Note&#58; It would be great if TFS Web Access had functionality to add <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx#StandardItems" shape="rect"><font color="#3a66cc">standard items to a Release</font></a> (aka iteration)<br></li>
<li>Run&#160;a <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d66a9404-2ca9-4d19-ad6c-df1618b4fc28" shape="rect">test please</a>&#160;on this.<br></li>
<li>Add this spreadsheet to your specification review document.<br></li>
<li>When the Estimate is approved by the client,&#160;start work following these rules&#58;&#160;<a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterProjectManagementWithTFS.aspx" shape="rect">Rules to Better Project Management with TFS</a>.<br></li></ol>
<br><excerpt class='endintro'></excerpt><br>

<p><strong>How to use the Estimates Calculator<br></strong><br>Open the <a href="/Documents/4.%20Estimates%20Calculator.xlsx?d=w6f09d6a75d074fbda81e5e5dd3e18c76">Estimates Calculator</a> and do the following&#58;<br></p><dl class="ssw15-rteElement-ImageArea"><img src="/PublishingImages/Resource%20tab.png" alt="Resource tab.png" style="margin&#58;5px;width&#58;808px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58; set the types and numbers of&#160;resources who will be working on the project<br><br></dd><dl class="ssw15-rteElement-ImageArea"><img src="/PublishingImages/Estimates%20tab.png" alt="Estimates tab.png" style="margin&#58;5px;width&#58;808px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure​&#58; Enter your PBIs and estimates<br></dd><p><br>Finally, you should copy and paste this estimates section&#160;into your proposal&#160;and present it&#160;to your client.&#160;<br></p><p><br></p><div><h3 class="ssw15-rteElement-H3">Why Microsoft Project isn't recommended<br></h3></div><div><p></p><ul class="ssw15-rteElement-P"><li><span style="line-height&#58;20px;">Tasks are auto scheduled based on dependency and resource allocation (who is assigned to it). This generates an estimated completion date which is never accurate, due to annual leave, public holidays and general shuffling of people in the team</span><br></li><li><span style="line-height&#58;20px;">It gets the summing wrong (the totals don't seem to update and no way to trigger it)</span><br></li><li><span style="line-height&#58;20px;">It's hard to synchronize with timesheets (as it doesn't connect to 3rd party timesheet systems out of the box –&#160;however, it does have&#160;its own time sheeting system, that is missing billing information!)</span><br></li><li><span style="line-height&#58;20px;">You cannot allocate two people to a task. This create a lot of additional overhead to get it right. **fixed in TFS 2008**</span></li></ul></div>


