---
type: rule
title: Do you know that WebAPI and tables name should be consistent?
uri: do-you-know-that-webapi-and-tables-name-should-be-consistent
created: 2015-04-28T13:30:47.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> When creating WebAPIs for your applications, it is useful to keep the naming consistent all the way from the back-end to the front-end. </span>

<p class="ssw15-rteElement-GreyBox"><strong>Table name&#58;</strong> Employees<br><strong>Endpoint&#58;</strong> /api/Users<br></p><dd class="ssw15-rteElement-FigureBad">​Bad Example&#58; The endpoint is different to the table name<br></dd><div><br></div><p class="ssw15-rteElement-GreyBox"><strong>​Table name&#58;</strong> Employees<br><strong>Endpoint&#58;</strong> /api/Employees<br></p><div><dd class="ssw15-rteElement-FigureGood">​Good Example&#58; Table name is the same as the WebAPI endpoint</dd><p><br></p><p>By making the endpoint the same as the table name, you can simplify&#160;development&#160;and maintenance of the WebAPI layer.</p><p>In some circumstances you may not have direct control over the database however. In these situations it may make sense to have different endpoint names if doing so will simplify development for consumers of your WebAPI endpoints.​</p></div>


