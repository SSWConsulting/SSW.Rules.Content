---
type: rule
archivedreason: 
title: Do you know what errors to filter out?
guid: 76d190a7-1bb9-4085-9223-8c4615b50c7c
uri: what-errors-to-filter-out
created: 2016-10-25T16:49:58.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-know-what-errors-to-filter-out

---


You should always keep on top of your RayGun crashreporting and not let the errors spiral out of control. If use RayGun with a web application, then you’ll frequently get a lot of errors with robots scanning the site and creating 404s.  <br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt> <img src="raygun-fileter-bad.png" alt="raygun-fileter-bad.png" /> </dt><dd>Figure: Bad Example – Most of these errors are 404s cause by automated tools scanning for vulnerabilities</dd>  </dl><p>Luckily RayGun has built-in filtering to hide these frequent exceptions.</p><dl class="image"><dt> <img src="raygun-filter.png" alt="raygun-filter.png" /> </dt></dl><p>To enable filtering:</p><ol><li>Under <b>Crash Reporting</b> &gt; select <b>Filtering</b><br></li><li>SSW recommends you turn on the following rules<ol style="list-style:lower-alpha;"><li>Discard any requesters where the user-agent is a known crawler bot</li><li>Discard any request for non-existent resources (404)</li><li>Discard any requests related to phpMyAdmin access attempts</li></ol></li></ol><p>Now you should have a nice clean crash report page with actual errors.</p><dl class="goodImage"><dt> <img src="raygun-filter-good.jpg" alt="raygun-filter-good.jpg" /> </dt><dd>Figure: Good example – Now that the noise is gone, we can see the actual errors</dd></dl> <br>


