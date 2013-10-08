---
type: rule
title: Do you know how to track down permission problems?
uri: do-you-know-how-to-track-down-permission-problems
created: 2013-10-08T15:22:15.0000000Z
authors:
- id: 33
  title: Gerard Beckerleg
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="p1">You need 
   <a href="http&#58;//technet.microsoft.com/en-us/sysinternals/bb896645.aspx"> 
      <span class="s1">process monitor</span></a> to track down permissions problems.</p><p class="p1">E.g. 
   <strong>Problem</strong></p><p class="p1">To hunt down a problem where say the IIS server couldn’t write to a directory, even after you have given permissions to the app pool account.</p><p class="p1"> 
   <strong>Solution</strong></p><ol class="ol1"><li class="li1">Install and run 
      <a href="http&#58;//technet.microsoft.com/en-us/sysinternals/bb896645.aspx"> 
         <span class="s1">process monitor</span></a></li><li class="li1">Apply filter</li><li class="li1">Rejoice</li></ol><dl class="image"><dt>
      <img src="/PublishingImages/process-monitor-filter.jpg" alt="" />
   </dt><dd>Figure&#58; Apply filter to only show &quot;ACCESS DENIED&quot; results</dd></dl>​​
   <dl class="image"><dt>
         <img src="/PublishingImages/event-properties.jpg" alt="" />
      </dt><dd>Figure&#58; And here we have the offending account</dd></dl> </span>




