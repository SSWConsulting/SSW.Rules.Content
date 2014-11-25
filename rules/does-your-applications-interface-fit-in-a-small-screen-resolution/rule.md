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
​<div>Each user prefers to have their own resolution. You must check if your controls will fit on the user's screen. Think about on which computers your application will run, and what devices will display it. To be on the safe side, it is advisable to fit your controls on a 1024 x 768px screen. Our projector has that resolution and it may well be used for presenting your application to the client.</div>
<dl class="badImage"><dt><img alt="Bad Interface Design Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/InterfaceResBadExample.jpg" /></dt>
<dd>Figure&#58; Bad Example - Form is too large to fit inside 1024x768px resolution</dd></dl>
<dl class="goodImage"><dt><img alt="Good Interface Design Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/InterfaceResGoodExample.jpg" /></dt>
<dd>Figure&#58; Good Example - Form fits inside any screen resolution</dd></dl>
<div>The potential solutions for this problem are&#58;</div>
<ol><li>Reorder and move the controls around on the form.</li>
<li>Implement Tab pages.</li>
<li>Use a wizard type interface, with Next, Back and Finish.</li>
<li>Create multiple forms each containing a subset of the controls.</li>
<li>Create a menu based form where the items are categories that some form controls fall under.<br>Similar to VS. Net's Tools -&gt; Options. </li>
<li>Hide unimportant controls and add the option to show them if necessary</li></ol>
<div>Read our rule on<a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWebsitesLayout.aspx#Responsive" target="_blank"> Do you design your web pages to work on 1024x768px (not 800x600px)?</a> ​ <br><br><p>From <a href="http&#58;//www.adamcogan.com/2012/11/18/microsoft-is-onto-something-here/" target="_blank">Adam Cogan</a>  (<a href="http&#58;//www.adamcogan.com/2012/11/18/microsoft-is-onto-something-here/" target="_blank">http&#58;//www.adamcogan.com/2012/11/18/microsoft-is-onto-something-here/</a> )&#58;</p><p class="ssw15-rteElement-Reference">I am amazed how good the split screen is so you can be reading email while continuing to watch that movie.<br> One thing developers need to be aware of when building apps, is to consider the size for the different resolutions in particular when an application is snapped. On the Surface, the snap view divides the screen up into ¼ and ¾, but this will be different on different devices (actually the snap view is always 342 pixels) so you really need to get into responsive designing. For a good user experience, keep the left snap view for reading, not interactive stuff like filling in forms.<br> The great thing for developers is the way you test. With Visual Studio 2012, the emulator simulates the Surface perfectly.</p><dl class="ssw15-rteElement-ImageArea"><img alt="SurfaceScreen.jpg" src="/PublishingImages/SurfaceScreen.jpg" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureGood">Figure&#58; The Surface screen allows you to place two apps side by side.<br></dd></div>



