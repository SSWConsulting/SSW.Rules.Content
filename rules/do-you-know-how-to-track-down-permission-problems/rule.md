---
type: rule
archivedreason: 
title: Do you know how to track down permission problems?
guid: 5ed0bbd5-58ea-41f5-8251-3247a6caf874
uri: do-you-know-how-to-track-down-permission-problems
created: 2013-10-08T15:22:15.0000000Z
authors:
- title: Gerard Beckerleg
  url: https://ssw.com.au/people/gerard-beckerleg
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


<p class="p1">You need 
   <a href="http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx"> 
      <span class="s1">process monitor</span></a> to track down permissions problems.</p><p class="p1">E.g. 
   <strong>Problem</strong></p><p class="p1">To hunt down a problem where say the IIS server couldn’t write to a directory, even after you have given permissions to the app pool account.</p><p class="p1"> 
   <strong>Solution</strong></p><ol class="ol1"><li class="li1">Install and run 
      <a href="http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx"> 
         <span class="s1">process monitor</span></a></li><li class="li1">Apply filter</li><li class="li1">Rejoice</li></ol><dl class="image"><dt>
      <img src="process-monitor-filter.jpg" alt="" />
   </dt><dd>Figure: Apply filter to only show "ACCESS DENIED" results</dd></dl>​​
   <dl class="image"><dt>
         <img src="event-properties.jpg" alt="" />
      </dt><dd>Figure: And here we have the offending account</dd></dl>
<br><excerpt class='endintro'></excerpt><br>



