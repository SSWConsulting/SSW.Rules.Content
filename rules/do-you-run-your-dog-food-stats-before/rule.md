---
type: rule
archivedreason: 
title: Do you run your dog food stats (before)?
guid: 7a788db9-fac6-4107-8751-339a3524f103
uri: do-you-run-your-dog-food-stats-before
created: 2009-11-05T10:14:53.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---


<div><ol><li>Run the excellent DogFoodStats by Grant Holliday. These are queries on the TFS2008 database to give you stats about number of files, number of users etc.<br><a href="http&#58;//blogs.msdn.com/bharry/archive/2007/12/02/tfs-statistics-update.aspx" shape="rect">http&#58;//blogs.msdn.com/bharry/archive/2007/12/02/tfs-statistics-update.aspx</a> <ol><li>Record the Number of files </li>
<li>Record the number of Iterations </li></ol></li></ol></div>
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
<div><span class="ms-rteCustom-FigureNormal">Example&#58; Dog Food Stats on TFS2008</span>Make sure that you save the numbers so you can compair it to TFS 2010 later...</div>
<br><excerpt class='endintro'></excerpt><br>



