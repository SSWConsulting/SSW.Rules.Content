---
type: rule
archivedreason: 
title: Do you run Dog Food Stats (after)?
guid: e2472404-8058-45f7-96e1-ddb6a8bdb49f
uri: do-you-run-dog-food-stats-after
created: 2009-11-08T02:01:52.0000000Z
authors: []
related: []

---


<p>Running the &quot;Dog Food&quot; stats on your new TFS 2010 server is a good way to see if the upgrade was successful. You should check the new values&#160;against the <a href="/Pages/DogfoodStatsBefore.aspx" shape="rect">stats you noted down from your TFS 2008 server</a>.</p>
<ol><li>On TFS2010, run the DogFoodStats queries and save the results<br>(<a class="ms-rteCustom-External" href="http&#58;//blogs.msdn.com/granth/archive/2009/10/23/tfs2010-sql-queries-for-tfs-statistics.aspx" shape="rect">http&#58;//blogs.msdn.com/granth/archive/2009/10/23/tfs2010-sql-queries-for-tfs-statistics.aspx</a>)&#160; </li>
<li>Compare the numbers are the same <ol><li>Note&#58; Number will differ slightly (usually increases as TFS2010 checks in a few more items) <br>Note&#58; Grant Holliday has never&#160;published exactly why they are not the same.</li></ol></li></ol>
<div><span class="ms-rteCustom-CodeArea"><div>TFS2008&#58;</div>
<div>===========================================</div>
<div>Files</div>
<div>-------- -----------</div>
<div>1 &#160; &#160; &#160; &#160;<font style="background-color&#58;#ffff00;">28052</font></div>
<div>2 &#160; &#160; &#160; &#160;<font style="background-color&#58;#ffff00;">335168</font></div>
<div>-- Compressed file size&#58;</div>
<div>--------------------</div>
<div>11837952896</div>
<div><br></div>
<div>-- Uncompressed file sizes&#58;</div>
<div>--------------------</div>
<div>24868196032</div>
<div>-- Areas &amp; Iterations&#58;</div>
<div>-----------</div>
<div><font style="background-color&#58;#ffff00;">1096</font></div></span></div>
<div><span class="ms-rteCustom-FigureNormal">Figure&#58; Have a look at the dogfoodstats you ran before</span></div>
<div><span class="ms-rteCustom-CodeArea"><div>TFS2010&#58;</div>
<div>=============================================</div>
<div>Areas and Iterations</div>
<div>--------------------</div>
<div><font style="background-color&#58;#ffff00;">1096</font></div>
<div><br></div>
<div>Files</div>
<div>-----------</div>
<div><font style="background-color&#58;#ffff00;">347629</font></div>
<div><br></div>
<div>Compressed File Sizes</div>
<div>---------------------</div>
<div>11296</div>
<div><br></div>
<div>Uncompressed File Sizes</div>
<div>-----------------------</div>
<div>23723</div></span></div>
<div><span class="ms-rteCustom-FigureNormal">Figure&#58; You should get the same number or more for your TFS2010 server. We’re not worried unless it’s slightly less</span></div>
<div>&#160;</div>
<br><excerpt class='endintro'></excerpt><br>



