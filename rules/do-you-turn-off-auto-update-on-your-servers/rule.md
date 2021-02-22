---
type: rule
archivedreason: 
title: Do you turn off auto-update on your servers?
guid: 3f57b030-795a-4b41-90cf-8bc352e2b7fd
uri: do-you-turn-off-auto-update-on-your-servers
created: 2010-06-24T01:43:02.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


It is not a good idea to have Windows Update automatically updating your servers.  There are a few reasons. 
<br><br>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>The hotfix could bring down a production environment. (This issue previously happened)<br></li><li>In fact, even in a development environment, this could be hours of lost work as the development team struggles to understand why only 
      <strong>some</strong> of the developers' servers <strong>magically and mysteriously </strong>broke overnight.<br></li><li>Windows Update could restart your server, or put your server in a state where it requires restarting - preventing any urgent MSI installs without bringing down the server.</li></ol><p>Windows Update remains the best thing for end-users to protect their systems.  But in a server, especially a production server environment - Windows Update patches are just like any new versions of the software that's built internally.  It should be tested and then deployed in a controlled manner.<br> 
   <br>So recommendations for managing updates are as follows:</p><ol><li>Use WSUS to approve/deny updates for your servers.<br></li><li>Update Staging/Development servers first to see if any issues arise from the updates.<br></li><li>Roll these updates out to Production once confident there are no issues​.<br></li><li>Windows Updates may be critical and should be kept relatively up to date.</li><li>Do all of this on a schedule - have an email sent to your SysAdmins to remind them to review and reboot needed machines:</li></ol><dl class="goodImage"><dt><img src="WSUSReport.png" alt="WSUSReport.png" style="width:750px;" />
   </dt><dd>Good Example: Scheduled email showing clear action points and WSUS stats<br></dd>
</dl>

<h3> ​​Related Rules<br></h3><ul><li>
      <a href=/do-you-disable-automatic-windows-update-installations>​Do you enable automatic Windows Update Installations?​</a> [for PCs] ​<br></li><li>
      <a href=/do-you-use-group-policy-to-manage-your-windows-update-policy>Do you use Group Policy to manage your Windows Update Policy?​</a> [for both PCs and Servers]​<br></li></ul>


