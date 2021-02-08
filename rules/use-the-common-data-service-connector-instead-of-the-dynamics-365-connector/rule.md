---
type: rule
archivedreason: 
title: Do you use the Common Data Service connector instead of the Dynamics 365 connector when using flows?
guid: 57167b92-8ff7-4aac-bfa0-d0de627e17d2
uri: use-the-common-data-service-connector-instead-of-the-dynamics-365-connector
created: 2020-06-25T22:21:36.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-use-the-common-data-service-connector-instead-of-the-dynamics-365-connector-when-using-flows

---


<p>When creating a Flow that connects to CRM, Flow gives you the choice of&#58;<br></p><ul><li>Dynamics 365&#160;</li><li>Common Data Service</li><li>Common Data Service (Current Environment)​<br></li></ul>​<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">​While it may seem like the obvious choice to pick Dynamics 365, but this would be a bad choice. The Dynamics 365 is deprecated as of April 2019. Use the Common Data Service (Current Environment) connector, it supports more data types and broader trigger scenarios.​<br></p><p class="ssw15-rteElement-P">Common Data Services (Current Environment) is only available if the Flow being developed is inside a solution. The advantage of using &quot;Current Environment&quot; is when the Flow is deployed across environments (Dev, Test, Prod) the connection is sticky to the environment to which it is being deployed. If a Flow is being developed outside of a solution, then use Common Data Services.<br><br></p><dl class="badImage"><dt><img src="/PublishingImages/bad-connector-use.png" alt="bad-connector-use.png" /></dt><dd>Bad Example&#58; Using the deprecated Dynamics 365 connector</dd></dl>

<dl class="goodImage">
<dt><img src="/PublishingImages/good-connector-use.png" alt="good-connector-use.png" /></dt><dd>Good Example&#58; Using the Common Data Service connector</dd></dl>


