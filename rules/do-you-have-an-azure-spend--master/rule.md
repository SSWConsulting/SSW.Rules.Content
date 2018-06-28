---
type: rule
title: Do you have an Azure Spend $ master?
uri: do-you-have-an-azure-spend--master
created: 2018-06-28T00:15:42.0000000Z
authors:
- id: 73
  title: Kaique Biancatti

---



<span class='intro'> ​Azure is a service from Microsoft that has many features and functionalities. However, you have to pay for every little bit of service that you use.<br> </span>

<p>Before diving in why, a little about roles in Azure&#58;<br></p><p><img src="/PublishingImages/tabl.png" alt="tabl.png" style="margin&#58;5px;" />&#160;</p><p><strong>Figure&#58; Roles in Azure.&#160;</strong></p><p>More here&#58;&#160;https&#58;//docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles<br><br>Based on this, it is not a good idea to&#160;give everyone in your company 'Contributor' access&#160;to Azure resources, because Contributors can change the number of resources used, and,&#160;therefore, increase the spending of Azure at the end of the month. When each one&#160;raises the spending and usage 'only a couple dollars', it ends up with a lot more spending at the end of the month.<br><br></p><p>It is a good idea and best practice to have an Azure Spend master with the Owner role, who gives 'Reader' access to employees who do not need to make changes to the specified resource. Only users whose will truly need to make changes to the resources should have Contributor access or higher.<br></p><p>​<img src="/PublishingImages/tabl3.png" alt="tabl3.png" style="margin&#58;5px;" /><br></p><dd class="ssw15-rteElement-FigureBad"> Bad Example&#58; Contributor access to the Developers group<br></dd><p><img src="/PublishingImages/tabl2.png" alt="tabl2.png" style="margin&#58;5px;" /><br></p><dd class="ssw15-rteElement-FigureGood"> Good Example&#58;&#160;Reader access to the Developers group<br></dd>


