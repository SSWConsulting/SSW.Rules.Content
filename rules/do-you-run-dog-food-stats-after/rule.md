---
type: rule
title: Do you run Dog Food Stats (After)?
uri: do-you-run-dog-food-stats-after
created: 2015-08-13T13:00:01.0000000Z
authors: []

---



<span class='intro'> <p>Running the&#160;<a href="http&#58;//blogs.msdn.com/b/granth/archive/2009/10/23/tfs2010-sql-queries-for-tfs-statistics.aspx" style="color&#58;#cc4141;border-bottom-color&#58;#cc4141;">DogFoodStats queries</a>&#160;&#160;&#160;over the new TFS 2015 server is a good way to see if the upgrade was successful.&#160; You should check the new values against the&#160;<a href="/ALM/RulesToBetterTFS2012Migration/Pages/DogfoodStatsBefore.aspx">stats you recorded from your TFS 2013 Update 4 databases</a>.</p><div><br></div> </span>

<p><span style="line-height&#58;1.6;">a.</span><span style="line-height&#58;1.6;">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; </span><span style="line-height&#58;1.6;">On your TFS 2015 databases, run the DogFoodStats queries and save the results.</span><br></p><p>b.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Check that the numbers are the same or very close.&#160; Note any big differences.<br> <strong>Note&#58;</strong>&#160;The numbers may not be identical due to schema changes.</p><p>Recent Users</p><p>31</p><p>&#160;</p><p>Users with Assigned Work Items</p><p>144</p><p>&#160;</p><p>Version Control Users</p><p>244</p><p>&#160;</p><p>Total Work Items</p><p>20608</p><p>&#160;</p><p>Areas and Iterations</p><p>1838</p><p>&#160;</p><p>Work Item Versions</p><p>93300</p><p>&#160;</p><p>Work Item Attachments</p><p>11332</p><p>&#160;</p><p>Work Item Queries</p><p>12768</p><p>&#160;</p><p>Compressed File Sizes</p><p>21230</p><p>&#160;</p><p>Uncompressed File Sizes</p><p>39504</p><p>&#160;</p><p>Checkins</p><p>53302</p><p>&#160;</p><p>Shelvesets</p><p>386</p><p>&#160;</p><p>Merge History</p><p>846922</p><p>&#160;</p><p>Pending Changes</p><p>947</p><p>&#160;</p><p>Workspaces</p><p>259</p><p>&#160;</p><p>Local Copies</p><p>4197428</p><p>&#160;</p><p>CheckIn&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 164</p><p>Get&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 474</p><p>Shelve&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 63</p><p>Upload&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 115</p><p>VCDownloadHandler&#160;&#160;&#160; 949</p><p>GetWorkItem&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 491</p><p>QueryWorkitems&#160;&#160;&#160;&#160; &#160; 601</p><p>Update &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;240</p><p><strong>Figure&#58; Example DogFoodStats after the upgrade</strong></p>


