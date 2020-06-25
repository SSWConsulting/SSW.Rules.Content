---
type: rule
archivedreason: 
title: Do you use the Common Data Service connector instead of the Dynamics 365 connector when using flows?
guid: 57167b92-8ff7-4aac-bfa0-d0de627e17d2
uri: do-you-use-the-common-data-service-connector-instead-of-the-dynamics-365-connector-when-using-flows
created: 2020-06-25T22:21:36.0000000Z
authors:
- id: 32
  title: Mehmet Ozdemir
related: []

---


When creating a Flow that connects to CRM, Flow gives you the choice of&#58;<br><ul><li>Dynamics 365&#160;</li><li>Common Data Service</li></ul>
<br><excerpt class='endintro'></excerpt><br>
<p>​While it may seem like the obvious choice to pick Dynamics 365, but this would be a bad choice. The Dynamics 365 is deprecated as of April 2019. Use the Common Data Service connector, it supports more datatypes and broader trigger scenarios.</p><dl class="badImage"><dt><img src="/PublishingImages/bad-connector-use.png" alt="bad-connector-use.png" /></dt><dd>Bad Example&#58; Using the deprecated Dynamics 365 connector</dd></dl>

<dl class="goodImage">
<dt><img src="/PublishingImages/good-connector-use.png" alt="good-connector-use.png" /></dt><dd>Good Example&#58; Using the Common Data Service connector</dd></dl>


