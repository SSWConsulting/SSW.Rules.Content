---
type: rule
archivedreason: 
title: Do you run Dog Food Stats (After)?
guid: 4eb538fc-5a30-4cc3-9a13-62e0a8ddd9be
uri: do-you-run-dog-food-stats-after-2
created: 2015-08-13T13:00:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-run-dog-food-stats-(after)-(2)
- do-you-run-dog-food-stats-after
- do-you-run-dog-food-stats-(after)

---


<p>Running the&#160;<a href="https&#58;//devblogs.microsoft.com/bharry/team-foundation-dogfood-stats/">DogFoodStats​</a> queries&#160;over the new TFS 2015 server is a good way to see if the upgrade was successful.<br></p><p>You should check the new values against the&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=381d8269-1d39-45e2-baea-23c9eff46693">stats you recorded from your TFS 2013 Update 4 databases</a>​.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ul><li><span style="line-height&#58;1.6;">a.&#160;</span><span style="line-height&#58;1.6;">On your TFS 2015 databases, run the DogFoodStats queries and save the results.</span></li><li>b.&#160;Check that the numbers are the same or very close.&#160; Note any big differences.</li></ul><p> <strong>Note&#58;</strong>&#160;The numbers may not be identical due to schema changes.</p><p class="ssw15-rteElement-GreyBox">Recent Users<br>31<br><br>Users with Assigned Work Items<br>144<br><br>Version Control Users<br>244<br><br>Total Work Items<br>20608<br><br>Areas and Iterations<br>1838<br><br>Work Item Versions<br>93300<br><br>Work Item Attachments<br>11332<br><br>Work Item Queries<br>12768<br><br>Compressed File Sizes<br>21230<br><br>Uncompressed File Sizes<br>39504<br><br>Checkins<br>53302<br><br>Shelvesets<br>386<br><br>Merge History<br>846922<br><br>Pending Changes<br>947<br><br>Workspaces<br>259<br><br>Local Copies<br>4197428<br><br>CheckIn&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;164<br>Get&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; 474<br>Shelve&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160;63<br>Upload&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;115<br>VCDownloadHandler&#160;&#160;&#160; 949<br>GetWorkItem&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 491<br>QueryWorkitems&#160;&#160;&#160;&#160; &#160; 601<br>Update &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;240<br></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Example DogFoodStats after the upgrade<br></dd><br>


