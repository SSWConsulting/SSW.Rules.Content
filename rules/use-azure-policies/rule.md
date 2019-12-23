---
type: rule
archivedreason: 
title: Do you use Azure Policies?
guid: a35200d4-bb97-4258-a4cb-d85f3e6b7a9d
uri: use-azure-policies
created: 2019-12-23T22:10:23.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
- do-you-use-azure-policies

---


<p>If you use a strong naming convention and is using Tags to its full extent in Azure, then it is time for the next step.</p><p>Azure Policies is a strong tool to help in governing your Azure subscription. With it, you make it easier to fall in The Pit of Success when creating or updating new resources. Some features of it&#58;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>You can deny creation of a Resource Group that does not comply with the naming standards<br></li><li>You can deny creation of a Resource if it doesn't possess the mandatory tags</li><li>You can append tags to newly created Resource Groups</li><li>You can audit the usage of specific VMs or SKUs in your Azure environment</li><li>You can allow only a set of SKUs within Azure</li></ol><p>Azure Policy allow for making of initiatives (group full of policies) that try to achieve an objective e.g. a initiative to audit all tags within a subscription, to allow creation of only some types of VMs, etc...</p><p>You can delve deep on it here&#58;&#160;<a href="https&#58;//docs.microsoft.com/en-us/azure/governance/policy/overview">https&#58;//docs.microsoft.com/en-us/azure/governance/policy/overview</a></p>
<dl class="goodImage">
   <dt>
      <img src="/PublishingImages/compliant-initiative-azure-policy.png" alt="compliant-initiative-azure-policy.png" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Good Example - A fully compliant initiative in Azure Policy&quot;</dd></dl>


