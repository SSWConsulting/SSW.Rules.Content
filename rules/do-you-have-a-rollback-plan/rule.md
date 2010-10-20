---
type: rule
title: Do you have a rollback plan?
uri: do-you-have-a-rollback-plan
created: 2009-11-02T22:38:45.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan

---



<span class='intro'> 
  <p>Always <a shape="rect" href="http&#58;//www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#assumeCatastrophic">plan for a catastrophic disaster</a>, in the event of errors when testing&#58;</p>
<ol>
    <li>Take the&#160;TFS2010 server offline </li>
    <li>Bring the TFS2008 server online </li>
    <li>Change the DNS entries for tfs.northwind.com from the IP for the TFS2010 server to the IP for the TFS2008 server
    <ol>
        <li>Internal DNS Server </li>
        <li>External DNS Server </li>
    </ol>
    </li>
</ol>
<p><img alt="TFS In DNS" src="/PublishingImages/TFSDNS.png" /><br>
Figure&#58; DNS Pointer for&#160;TFS can be easily changed</p>
 </span>




