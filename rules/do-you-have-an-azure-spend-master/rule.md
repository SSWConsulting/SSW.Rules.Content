---
type: rule
archivedreason: 
title: Do you have an Azure Spend $ master?
guid: ea05ddf7-1ff4-4f08-92af-e5c379331a83
uri: do-you-have-an-azure-spend-master
created: 2018-06-28T00:15:42.0000000Z
authors:
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects: []

---


Azure is Microsoft's Cloud service. However, you have to pay for every little bit of service that you use. <br>
<br><excerpt class='endintro'></excerpt><br>
<p>Before diving in, it is good to have an understanding of the basic built-in user roles:<br></p><dl class="image"><dt> <img src="tabl.png" alt="tabl.png" style="width:809px;height:254px;" /> </dt><dd>Figure: Roles in Azure</dd></dl><p>
   <b>More info:</b> <a href="https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles">https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles </a></p><p>It's <b>not</b> a good idea to give everyone 'Contributor' access to Azure resources in your company. The reason is cost: Contributors can add/modify the resources used, and therefore increase the cost of your Azure build at the end of the month. Although a single change might represent 'just a couple of dollars', in the end, everything summed up may increase the bill significantly.<br></p><p>The best practice is to have an<strong> Azure Spend Master</strong>. This person will control the level of access granted to users. Providing "Reader" access to users that do not need to/should not be making changes to Azure resources and then "Contributor" access to those users that will need to Add/Modify resources, bearing in mind the cost of every change.</p><p><br>Also, keep in mind that you should be giving access to security groups and not individual users. It is easier, simpler, and keeps things much better structured.<br><br></p><dl class="badImage"><dt> <img src="tabl3.png" alt="tabl3.png" style="width:800px;height:179px;" /></dt><dd> Bad Example: Contributor access to the Developers group</dd></dl><dl class="goodImage"><dt><img src="tabl2.png" alt="tabl2.png" style="width:800px;height:170px;" /></dt><dd> Good Example: Reader access to the Developers group<br></dd></dl>


