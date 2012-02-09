---
type: rule
archivedreason: 
title: Management - Is your client clear on the definition of a bug?
guid: ff5e3135-d63a-4d61-8c4f-56051fb8c2ee
uri: management-is-your-client-clear-on-the-definition-of-a-bug
created: 2009-02-28T09:42:39.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---


The answer to this question can make or break contracts. We think that it's such a fundamental issue it has to be captured clearly. This is how we strictly define a bug. 
​
<br><excerpt class='endintro'></excerpt><br>

  <p>
    <img src="/PublishingImages/bug-feature.png" alt="" />
    <br>
<br>A software issue can be classed as a bug&#160;where&#58;&#160;</p>
<ol><li>The application <strong>crashes to code </strong>(excluding bugs&#160;resulting from&#160;third party products (e.g. &quot;blue screen of death&quot; or crashing in a third party data grid that we cannot control); <strong>or </strong></li>
    <li>The application displays <strong>data inconsistent with the specified business rules</strong>;<strong> or</strong> </li>
    <li>The application is <strong>missing functionality&#160;<strong>specified&#160;</strong></strong>in the specification; <strong>or</strong> </li>
    <li>The <strong>page design/layout is substantially inconsistent</strong> with the agreed mock-ups </li>
</ol>
<p><strong>and </strong>the developers can reproduce the above on the test server <strong>and </strong>the application is not yet &quot;live&quot; <strong>and </strong>the issue has been reported in time (generally 30 days).</p>
<strong>Examples of what *could* constistute a bug&#58;</strong>
<ol>
    <li>The application crashes to code&#160;because it doesn't check that a connection is valid before running a stored procedure <strong>(this is likely covered because it crashes to code)<br>
    <span><img width="585" height="465" src="/PublishingImages/YellowScreenofDeath.jpg" alt="" /><br>
    <span style="font-weight&#58;normal;"><strong><span class="ms-rtecustom-figurenormal" style="display&#58;inline !important;">Figure&#58; Yellow screen of death</span></strong></span></span></strong> </li>
    <li>A sum total is negative instead of positive because the wrong operator (plus instead of minus) has been used to calculate the running balance <strong>(this is likely&#160;covered because data is inconsistent with the specified business rules)<br>
    <span><img src="/PublishingImages/IncorrectSum.jpg" alt="" /><br>
    <span style="font-weight&#58;normal;"><strong><span class="ms-rtecustom-figurenormal" style="display&#58;inline !important;">Figure&#58; An incorrect sum is likely to be a bug</span></strong></span></span></strong> </li>
    <li>The application is missing the Monthly Sales report <strong>(this is likely covered because the application is missing functionality specified in the specification)</strong> </li>
    <li>The output HTML in the application is formatted way out of line and does not display in the specified browser (e.g. Internet Explorer 9) <strong>(this is likely covered because it substantially inconsistent with the agreed mockup)<br>
    </strong></li>
</ol>
<strong>Examples of what is *not* a bug&#58;</strong>
<ol>
    <li>Any problem caused by software or an application not written by the organization&#160;supplying the software. </li>
    <li>The customer requirement was not included in the user interface/mock-ups/specifications. </li>
    <li>The client decides that they don't like the look of the current form even though it is the substantially the same as shown in the specification and wants the buttons at the bottom of the form instead of at the top. </li>
    <li>The original specification states that the total price excludes GST, but it really should have included GST. This is a change to the specification, and is not included in the contract. </li>
</ol>
<p><strong>Work items in TFS</strong></p>
<p>Using TFS&#160;allows you&#160;to create work items such as user stories, bugs, tasks, test cases etc. Only create bugs in TFS for defects, faults, flaws, or imperfections that fulfill your&#160;definition of a bug. For everything else use other work item types.</p>
<blockquote>
<p><strong><span><span style="font-weight&#58;normal;"><strong><span class="ms-rtecustom-figurenormal" style="display&#58;inline !important;"><img src="/PublishingImages/WorkItemsTFS.jpg" alt="" /><br>
Figure&#58; Do I create this as a bug, or a task?&#160;</span></strong></span></span></strong><strong><br>
</strong></p>
</blockquote>
<p><strong>Handling additional work for fixed-price contracts</strong><br>
<br>
Any new features or modifications (non-bug items) not in the original release plan are classed as additional work and are outside the scope of the contract. Any tasks which <strong>are</strong> bugs should be marked as additional items and be completed in the current release if possible. Most importantly, after the release plan has been sent, <strong>a task should NOT be entered as an item (additional or otherwise) in ANY sprints if they are not a bug</strong>. Instead, move all non-bug items to the product backlog for future review after the warranty period for the fixed price contract has passed.</p>
<p><strong>Handling additional work in a&#160;Scrum project</strong><br><br>Any new features or modifications (non-bug items) not in the original Product Backlog are classed as additional PBI's and placed on the Product Backlog.&#160;Any tasks which&#160;<strong>are</strong>&#160;bugs found during the current Sprint should be fixed within the current Sprint.&#160;Any tasks which&#160;<strong>are</strong>&#160;bugs found outside of the current Sprint should be added to the Product Backlog.</p>
<p><img src="/PublishingImages/62034c_tfs_preview_add_bug.png" alt="tfs_preview_add_bug.png" style="margin-top&#58;5px;margin-right&#58;5px;margin-bottom&#58;5px;margin-left&#58;5px;" /><br><strong>Figure&#58; Adding a bug to the Product Backlog in TFS Preview (TFS 2012)</strong><br><br></p>
<p>If you see a bug in any software product, e.g. SSW Code Auditor, it is best to report the issue following the steps outlined the <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Support/BugReportOrEnhancement.aspx">SSW Bug or Enhancement Reporting Standard</a>.</p>
<div class="greyBox">Note&#58; The above is our definition. Others have different definitions that we do <strong>not</strong> subscribe to&#58;
<ul>
    <li><a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Redirect/KB/KBQ720494JoelOnSoftware.htm" target="_blank">http&#58;//www.ssw.com.au/ssw/Redirect/KB/KBQ720494JoelOnSoftware.htm</a>&#160;<img width="17" height="11" alt="You are about to leave the SSW site" src="http&#58;//www.ssw.com.au/ssw/Images/LeaveSite.gif" /> </li>
</ul>
</div>
<div class="greyBox">You can also use the Wiki definition of &quot;Software Bug&quot; as a reference to understand this concept&#58;
<ul>
    <li><a shape="rect" href="http&#58;//en.wikipedia.org/wiki/Software_bug">Wikipedia Definition of Software Bug</a>&#160;<img width="17" height="11" alt="You are about to leave the SSW site" src="http&#58;//www.ssw.com.au/ssw/Images/LeaveSite.gif" /> </li>
</ul>
</div>



