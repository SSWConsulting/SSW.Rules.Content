---
uri: do-you-know-the-best-way-to-get-metrics-out-of-your-browser
title: Do you know the best way to get metrics out of your browser?
created: 2019-08-27 17:42:09
authors:
  - id: 78
    title: Matt Wicks
  - id: 34
    title: Brendan Richards
---




<span class='intro'> <p class="ssw15-rteElement-P">​​Lighthouse is an&#160;open-source tool built into Google Chrome that can audit for performance, accessibility, progressive web apps, and more. Allowing you to improve the quality of web pages.​​<br></p> </span>

<p>You can run Lighthouse&#58;</p><ul><li>In Chrome DevTools</li><li>From the command line​<br></li><li>As a Node module</li></ul><p class="ssw15-rteElement-P">It runs a series of audits against a URL and then it generates a report on how well the page did. From there, you can use the failing audits as indicators on how to improve the page. Each audit has a reference doc explaining why the audit is important, as well as how to fix it.</p>
<dl class="goodImage">
   <dt>
      <img src="/PublishingImages/lighthouse-100.png" alt="lighthouse-100.png" />
   </dt><dd>Figure&#58; Good Example - Google Chrome Lighthouse is showing 100%<br><br></dd><h3 class="ssw15-rteElement-H3">Lighthouse Level 1&#58; Throttling Off<br></h3><font color="#333333">For applications intended for use on a desktop and from within a well-connected office&#160;(such as your intranet or office timesheet application) test with throttling turned off.</font><br><h3 class="ssw15-rteElement-H3">Lighthouse Level 2&#58; Throttling On<br></h3><p class="ssw15-rteElement-P">To see how well your website would perform on low-spec&#160;devices and with poor internet bandwidth, use the throttling features. This is most important for high volume, customer-facing apps.&#160;<br></p><p class="ssw15-rteElement-P"><br>​<img src="/SiteAssets/the-best-way-to-get-metrics-out-of-your-browser/lighthouse_throttling.png" alt="lighthouse_throttling.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Lighhouse can simulate slow netwrking and CPU when performing tests<br></dd><p class="ssw15-rteElement-P">​<br></p><h3 class="ssw15-rteElement-H3">Lighthouse Level 3&#58; Automated testing<br></h3><p class="ssw15-rteElement-P">For business-critical pages, you may want to automate Lighthouse testing as part of your Continuous&#160;Delivery pipeline. This blog post by&#160;Andrejs Abrickis shows how to configure an Azure DevOps&#160;build&#160;pipeline that performs Lighthouse testing.<br><a href="https&#58;//medium.com/%40andrejsabrickis/continuously-audit-web-apps-performance-using-google-s-lighthouse-and-azure-devops-3e1623372f79">https&#58;//medium.com/@andrejsabrickis/continuously-audit-web-apps-performance-using-google-s-lighthouse-and-azure-devops-3e1623372f79​</a><br>​<br>​<br></p><p class="ssw15-rteElement-P"><br></p></dl>


