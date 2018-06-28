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

<p>Before diving in, see the basic about roles in Azure&#58;<br></p><dl class="image"><dt> <img src="/PublishingImages/tabl.png" alt="tabl.png" /> </dt><dd>Figure&#58; Roles in Azure</dd></dl><p>
   <b>More info&#58;</b>&#160;<a href="https&#58;//docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles">https&#58;//docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles </a></p><p>It's <b>not</b> a good idea to&#160;give everyone&#160;'Contributor' access&#160;to Azure resources in your company. The reason is costing&#58; Contributors can change the number of resources used, and&#160;therefore&#160;increase the spending on Azure at the end of the month. Although a single&#160;change might represent&#160;'just a couple of&#160;dollars',&#160;in the end, everything​ summed up may increase the bill significantly.<br></p><p>The best practice is&#160;to have an <b>Azure Spend Master </b>as the &quot;Owner&quot;. This person gives 'Reader' access to the&#160;employees who won't make changes to the resources. Other&#160;users who will truly need to make these resource&#160;changes should have Contributor access or higher, bearing in mind the costing of every change done.<br></p><dl class="badImage"><dt> <img src="/PublishingImages/tabl3.png" alt="tabl3.png" /></dt><dd> Bad Example&#58; Contributor access to the Developers group</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/tabl2.png" alt="tabl2.png" /></dt><dd> Good Example&#58;&#160;Reader access to the Developers group<br></dd></dl>


