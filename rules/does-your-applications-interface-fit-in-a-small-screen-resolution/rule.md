---
type: rule
archivedreason: 
title: Does your application's interface fit in a small screen resolution?
guid: 2e41f20a-377a-4142-95c7-b64cd5177871
uri: does-your-applications-interface-fit-in-a-small-screen-resolution
created: 2012-11-27T02:02:11.0000000Z
authors: []
related: []

---


<p>One side effect of having busy forms is that it doesn't scale down.</p>
<br><excerpt class='endintro'></excerpt><br>
​<div>Each user prefers to have their own resolution. You must check if your controls will fit on the user's screen. Think about on which computers your application will run, and what devices will display it. To be on the safe side, it is advisable to fit your controls on an 1024 x 768px screen. Our projector has that resolution and it may well be used for presenting your application to the client.</div>
<dl class="badImage"><dt><img alt="Bad Interface Design Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/InterfaceResBadExample.jpg" /></dt>
<dd>Figure&#58; Bad Example - Form is too large to fit inside 1024x768px resolution</dd></dl>
<dl class="goodImage"><dt><img alt="Good Interface Design Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/InterfaceResGoodExample.jpg" /></dt>
<dd>Figure &#58; Good Example - Form fits inside any screen resolution</dd></dl>
<div>The potential solutions for this problem are&#58;</div>
<ol><li>Reorder and move the controls around on the form.</li>
<li>Implement Tab pages.</li>
<li>Use a wizard type interface, with Next, Back and Finish.</li>
<li>Create multiple forms each containing a subset of the controls.</li>
<li>Create a menu based form where the items are categories that some form controls fall under.<br>Similar to VS. Net's Tools -&gt; Options. </li>
<li>Hide unimportant controls and add the option to show them if necessary</li></ol>
<div>Read our rule on<a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWebsitesLayout.aspx#Resolution"> Do you design your web pages to work on 1024x768px (not 800x600px)?</a> to know more.</div>



