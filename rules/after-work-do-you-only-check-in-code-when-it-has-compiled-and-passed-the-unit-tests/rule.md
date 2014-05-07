---
type: rule
archivedreason: 
title: (After work) Do you only check-in code when it has compiled and passed the unit tests?
guid: 628ea729-95f9-4f55-8985-6ffe130b5a70
uri: after-work-do-you-only-check-in-code-when-it-has-compiled-and-passed-the-unit-tests
created: 2011-11-18T03:52:34.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 6
  title: Tristan Kurniawan
- id: 17
  title: Ryan Tee
related: []

---


Too many people treat Source Control as a networked drive. Don't just check-in when the clock ticks past 5 or 6 o'clock. If code doesn't pass its unit tests or won't even compile put your code in a <a shape="rect" href="http&#58;//msdn.microsoft.com/en-us/library/ms181403.aspx">shelveset</a> 

<br><excerpt class='endintro'></excerpt><br>

  <img class="ms-rteCustom-ImageArea" src="/PublishingImages/LeaveAMessToOthers.jpg" alt="" />&#160;<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Put your dishes straight in the dishwasher otherwise you leave a mess for others (aka &quot;Check in&quot; the right way otherwise you give other developers problems) </font>Other recommendations have included using //TODO or commenting the code out. However we recommend avoiding this practice as it increases the risk that the code is forgotten about. <br>
Note&#58; Having <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterVersionControlwithTFS%28AKASourceControl%29.aspx#MinimumBuilds">gated check-ins </a>will help prevent this from happening. <br>
Note&#58; A useful tool is <a shape="rect" href="http&#58;//visualstudiogallery.msdn.microsoft.com/en-us/080540cb-e35f-4651-b71c-86c73e4a633d">TFS Auto Shelve </a>- Protect your code by guaranteeing your pending changes are always backed up to the TFS server. 



