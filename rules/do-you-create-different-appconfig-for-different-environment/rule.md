---
type: rule
archivedreason: 
title: Do You Create Different App.Config for Different Environment?
guid: 8c6e4f21-3c36-42bf-9246-f9da9b8c3c03
uri: do-you-create-different-appconfig-for-different-environment
created: 2009-12-10T05:23:58.0000000Z
authors:
- id: 11
  title: Andy Taslim
related: []

---


Every application has different settings depending on the environment it is running on, e.g. production, testing or development environment.<br>
It is much easier and efficient if app.config is provided in several environment types, so then the developer can just copy and paste the&#160;required app.config.<br>
<br>
<img alt="" src="/PublishingImages/AppConfigBad.jpg" /><br>
<br>
<font class="ms-rteCustom-FigureBad" size="+0">Figure&#58; Bad Example - Only 1 App.config provided</font><br>
<img alt="" src="/PublishingImages/App.config.jpg" /><br>
<br>
<font class="ms-rteCustom-FigureGood" size="+0">Figure &#58; Good Example - Several App.config are provided</font> 

<br><excerpt class='endintro'></excerpt><br>



