---
type: rule
title: Do you know when to use Geo Redundant Storage?
uri: do-you-know-when-to-use-geo-redundant-storage
created: 2015-02-10T18:34:05.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>Data in Azure Storage accounts is protected by replication. Deciding how far to replicate it is a balance between safety and cost.​</p><dl class="image"><dt><img src="/PublishingImages/azure-graphic.jpg" alt="" /></dt><dd>Figure&#58; It is important to balance safety and pricing when choosing the right replication strategy for Azure Storage Accounts</dd></dl> </span>

<h4></h4><p class="p1"> 
   <strong>Locally redundant storage (LRS)</strong></p><ul class="ul1"><li class="li1">Ma<b></b>intains three copies of your data.&#160;</li><li class="li1">Is replicated three times within a single facility in a single region.&#160;</li><li class="li1">Protects your data from normal hardware failures, but not from the failure of a single facility.</li><li class="li1">Less expensive than GRS</li><li class="li1">Use when&#58; 
      <ul class="ul1"><li class="li1"> 
            <span class="s1">o<span class="Apple-tab-span"> </span></span>Data is of low importance – e.g. for test websites, or testing virtual machines</li><li class="li1"> 
            <span class="s1">o<span class="Apple-tab-span"> </span></span>Data can be easily reconstructed</li><li class="li1"> 
            <span class="s1">o<span class="Apple-tab-span"> </span></span>Data is non-critical</li><li class="li1"> 
            <span class="s1">o<span class="Apple-tab-span"> </span></span>Data governance requirements restrict data to a single region</li></ul></li></ul><p class="p1"> 
   <strong>Geo-redundant storage (GRS).</strong>&#160;</p><ul class="ul1"><li class="li1">The default when you create it storage accounts.</li><li class="li1">Maintains six copies of your data.&#160;</li><li class="li1">D<b></b>ata is replicated three times within the primary region, and is also replicated three times in a secondary region hundreds of miles away from the primary region</li><li class="li1">In the event of a failure at the primary region, Azure Storage will failover to the secondary region.&#160;</li><li class="li1">Ensures that your data is durable in two separate regions.</li><li class="li1">Use when&#58; 
      <ul><li>
            <span class="s1">o<span class="Apple-tab-span"> </span></span>Data cannot be recovered if los​t</li></ul></li></ul>
<strong style="line-height&#58;1.6;">Read access geo-redundant storage (RA-GRS).</strong><span style="line-height&#58;1.6;">&#160;</span>
<ul class="ul1"><li class="li1">Replicates your data to a secondary geographic location (same as GRS)</li><li class="li1">P<b></b>rovides read access to your data in the secondary location</li><li class="li1">Allows you to access your data from either the primary or the secondary location, in the event that one location becomes unavailable.</li><li class="li1">Use when&#58;​
   <ul><li class="li1"> 
      <span class="s1">o<span class="Apple-tab-span"> </span></span>Data is critical, and access is required to both the primary and the secondary regions</li></ul></li></ul>​<span style="color&#58;#cc4141;font-family&#58;'segoe ui', 'trebuchet ms', tahoma, arial, verdana, sans-serif;font-size&#58;18px;line-height&#58;32px;">More reading</span><ul><li> 
      <a href="https&#58;//msdn.microsoft.com/en-us/library/azure/dn727290.aspx" target="_blank">Azure Storage Redundancy Option&#160;​</a></li></ul>


