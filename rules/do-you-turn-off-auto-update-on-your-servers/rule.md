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


It is not a good idea to have Windows Update automatically updating your servers.&#160; There are a few reasons. 
<br><br>
<br><excerpt class='endintro'></excerpt><br>

  
<ol>
    <li>The hotfix could bring down a production environment. (This issue previously happened)<br></li>
    <li>In fact, even in a development environment this could be hours of lost work as the development team struggles to understand why only <strong>some</strong> of the developers' servers&#160;<strong>magically and mysteriously </strong>broke overnight.<br></li>
    <li>Windows Update could restart your server, or put your server in a state where it requires restarting - preventing any urgent MSI installs without bringing down the server.</li>
</ol>
<p>Windows Update remains the best thing for end-users to protect their systems.&#160; But in a server, especially a production server environment - Windows Update patches are just like any new versions of the software that's built internally.&#160; It should be tested and then deployed in a controlled manner.<br>
<br>So recommendations&#58;</p>
<ol>
    <li>Windows Updates may be critical and should be kept relatively up to date.</li>
    <li>Have a plan where your awesome Network Admins schedule time to keep the servers up to date - including testing that the servers still perform its functions.<br></li>
    <li>Turn off Automatic Windows Update on Windows Servers<br></li>
</ol>



