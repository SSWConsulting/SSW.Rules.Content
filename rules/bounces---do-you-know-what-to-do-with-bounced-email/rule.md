---
type: rule
archivedreason: 
title: Bounces - Do you know what to do with bounced email?
guid: e21a0c88-e1a5-4b66-acc6-0dfb7fffbf12
uri: bounces---do-you-know-what-to-do-with-bounced-email
created: 2011-08-25T19:54:59.0000000Z
authors: []
related: []

---


Having people report bounce back emails is frustrating and time consuming. The first thing to try when you get a report is to check that your mail server isn’t on a spam blacklist. An easy way to check this is via <a target="_blank" href="http&#58;//mxtoolbox.com/">MX Toolbox</a>.
<br><excerpt class='endintro'></excerpt><br>
<img class="ms-rteCustom-ImageArea" alt="Enter the domain to check" src="/Communication/RulesToBetterEmail/PublishingImages/MXToolbox-1.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Enter the domain to check</span>

<img class="ms-rteCustom-ImageArea" alt="Then select Blacklist Check" src="/Communication/RulesToBetterEmail/PublishingImages/MXToolbox-2.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Then select &quot;Blacklist Check&quot;</span>

<img class="ms-rteCustom-ImageArea" alt="not blacklisted" src="/Communication/RulesToBetterEmail/PublishingImages/MXToolbox-3.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Getting a zero is good, so you know that you are not blacklisted… so Step 1 is good</span>

<p>Next step check that you have primary and secondary (and even better tertiary) MX records setup and working.</p>

<img class="ms-rteCustom-ImageArea" alt="SMTP test" src="/Communication/RulesToBetterEmail/PublishingImages/MXToolbox-4.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Seeing at least 2 MX records is good... Run an SMTP Test to test mail servers. So Step 2 is good</span> 

<p>If success on both steps the error is most likely on the senders side. Send them the an email to check their mail settings.</p>

<div class="greyBox">
Dear xxx
As per this rule on bounced emails http&#58;//xxxxx

I have checked Step 1 – it is good
I have checked Step 2 – it is good

The problem is likely your end
</div>
<span class="ms-rteCustom-FigureNormal">Figure&#58; What to send the person </span>



