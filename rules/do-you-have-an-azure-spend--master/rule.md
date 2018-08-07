---
type: rule
title: Do you have an Azure Spend $ master?
uri: do-you-have-an-azure-spend--master
created: 2018-06-28T00:15:42.0000000Z
authors:
- id: 73
  title: Kaique Biancatti

---



<span class='intro'> Azure is Microsoft's Cloud service.&#160;However, you have to pay for every little bit of service that you use.&#160;<br> </span>

<p>Before diving in, it is good to have an understanding of the basic built-in user roles&#58;<br></p><dl class="image"><dt> <img src="/PublishingImages/tabl.png" alt="tabl.png" style="width&#58;809px;height&#58;254px;" /> </dt><dd>Figure&#58; Roles in Azure</dd></dl><p>
   <b>More info&#58;</b>&#160;<a href="https&#58;//docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles">https&#58;//docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles </a></p><p>It's <b>not</b> a good idea to&#160;give everyone&#160;'Contributor' access&#160;to Azure resources in your company. The reason is cost&#58;&#160;Contributors can add/modify the resources used, and therefore increase the cost of your Azure build at the end of the month. Although a single&#160;change might represent&#160;'just a couple of&#160;dollars',&#160;in the end, everything summed up may increase the bill significantly.<br></p><p>The best practice is to have an<strong> Azure Spend Master</strong>. This person will control the level of access granted to users. Providing &quot;Reader&quot; access to users that do not need to/should not be making changes to Azure resources and then &quot;Contributor&quot; access to those users that will need to Add/Modify resources, bearing in mind the cost of every change.</p><p><br>Also, keep in mind that you should be giving access to security groups and not individual users. It is easier, simpler, and keeps things much better structured.<br><br></p><dl class="badImage"><dt> <img src="/PublishingImages/tabl3.png" alt="tabl3.png" style="width&#58;800px;height&#58;179px;" /></dt><dd> Bad Example&#58; Contributor access to the Developers group</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/tabl2.png" alt="tabl2.png" style="width&#58;800px;height&#58;170px;" /></dt><dd> Good Example&#58;&#160;Reader access to the Developers group<br></dd></dl>


