---
type: rule
archivedreason: 
title: Help - Do you have a wiki for each page or form?
guid: 4c7f4917-33de-4e19-b061-1c697944c71e
uri: help---do-you-have-a-wiki-for-each-page-or-form
created: 2012-11-27T02:10:18.0000000Z
authors: []
related: []

---


<p>In agile development; updates, changes and bug fixes happen all the time and an issue that a user encounters today might already is fixed or have a workaround. That is why each page or form should link to a wiki page with any common problems that a user might encounter (and workarounds for them) and planned changes.</p>
<br><excerpt class='endintro'></excerpt><br>
​<div>This saves the end user from resorting to crawling the web for solutions.</div>
<dl class="bad"><dt><div><strong>From&#58;</strong> Tech Support<br><strong>Sent&#58;</strong> Wednesday, 27 January 2010 4&#58;31 PM<br><strong>To&#58;</strong> Mr Northwind<br><strong>Subject&#58;</strong> RE&#58; Issue with lab management hosts</div>
<div>Hi Mr Northwind</div>
<div>There was a bug in Beta2 (fixed in upcoming RC release) wherein even if you have no lab artifacts in a host group, it did not allow you to delete host group from a Project collection in Team Foundation Admin Console UI until you delete the host groups explicitly from all the associated team projects. </div>
<ol><li><div>Run the following commands to project level association (make sure that there are no Lab environments in this Host Group).</div>
<div><strong>TFSLabConfig.exe DeleteTeamProjectHostGroup /Collection&#58;&lt;CollectionUrl&gt; /teamProject&#58;* /name&#58;&quot;Testing Host&quot; </strong></div></li>
<li><div>Delete the host groups from Team Foundation Admin Console UI</div>
<div><strong>There was a similar issue with the Library shares also, and has been fixed now.</strong></div></li></ol>
<div>Regards<br>Tech Support</div>
<hr />
<div><strong>From&#58;</strong> Mr Northwind<br><strong>Sent&#58;</strong> 27 January 2010 10&#58;07<br><strong>To&#58;</strong> Tech Support<br><strong>Subject&#58;</strong> Issue with lab management hosts</div>
<div>I accidentally (on scvmm) created a folder called &quot;Testing&quot; under by All Hosts group. In TFSAC I added the AllHosts\Testing host. This led me to other problems so I tried to remove this host from TFS. Guess what? I can't remove any hosts from TFS at all! Even after I deleted it from SCVMM. The error I get is&#58; </div>
<div>TF259085&#58; Team Foundation Server could not delete the environment location because the following All Hosts_Testing is currently in use&#58; TeamProjectCollectionhostGroup. Delete the resources at this location, and then try the operation again. (type SoapException)</div>
<div>I have no idea what this is telling me. Anyone have any ideas?</div>
<div>Thanks!<br>Mr Northwind</div></dt>
<dd>Figure&#58; Bad Example - The user encounters an issue and has to email someone about it </dd></dl>
<dl class="goodImage"><dt><img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/InterfacesWiki.png" alt="" /></dt>
<dd>Figure&#58; Good Example - The 'Wiki...' link in the bottom left, takes the user to a wiki page with common issues and workarounds for this form (e.g. Creating a Project Portal) </dd></dl>



