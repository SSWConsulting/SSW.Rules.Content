---
type: rule
archivedreason: 
title: Do you turn off auto-update on your servers?
guid: 3f57b030-795a-4b41-90cf-8bc352e2b7fd
uri: do-you-turn-off-auto-update-on-your-servers
created: 2010-06-24T01:43:02.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan
related: []

---


It is not a good idea to have Windows Update automatically updating your servers.&#160; There are a few reasons. 
<br><br>
<br><excerpt class='endintro'></excerpt><br>

  
<ol>
    <li>The hotfix could bring down a production environment. (This issue previously happened)<br></li>
    <li>In fact, even in a development environment this could be hours of lost work as the development team struggles to understand why only <strong>some</strong> of the developers' servers&#160;<strong>magically and mysteriously </strong>broke overnight.<br></li>
    <li>Windows Update could restart your server, or put your server in a state where it requires restarting - preventing any urgent MSI installs without bringing down the server.</li>
</ol>
<p>Windows Update remains the best thing for end-users to protect their systems.&#160; But in a server, especially a production server environment - Windows Update patches are just like any new versions of the software that's built internally.&#160; It should be tested and then deployed in a controlled manner.<br>
<br>So recommendations for managing updates are as follows&#58;</p>
<ol>
    <li>Use WSUS to approve/deny updates for your servers.<br></li><li>Update Staging/Development servers first to see if any issues arise from the updates.<br></li><li>Roll these updates out to Production once confident there are no issues​.<br></li><li>Windows Updates may be critical and should be kept relatively up to date.</li><li>Do all of this on a schedule - have an email sent to your SysAdmins to remind them to review and reboot needed machines&#58;</li></ol><div><img src="/SiteAssets/do-you-turn-off-auto-update-on-your-servers/WSUSReport.png" alt="WSUSReport.png" style="margin&#58;5px;width&#58;808px;" /><dd class="ssw15-rteElement-FigureGood">Good Example&#58; Scheduled email showing clear action points and WSUS stats<br></dd></div><ol>
</ol>



