---
type: rule
archivedreason: 
title: Do you know the best way to give the best customer support?
guid: 09255b34-91b3-4404-b7f4-6fff46392c87
uri: do-you-know-the-best-way-to-give-the-best-customer-support
created: 2009-03-04T06:49:46.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


There are a few methods to control a client's machine remotely, all of them have the same functionality, but different usage, and different pros and cons. 

<br><excerpt class='endintro'></excerpt><br>

  <p>
    <strong>Servers</strong> </p>
<p>For server machines, we recommend using either Windows' built-in Remote Desktop (also knows as &quot;Terminal Services&quot; ) or a VNC-based tool. Remote Desktop provides each authenticated user a Windows logon session that is not shared.&#160;If your client lives in a place where the time zone is different, Remote Desktop should be your first choice as it doesn't need the client's interaction once Remote Desktop is enabled (typically it should have been enabled for a server for the ease for remote maintenance and monitoring). </p>
<img class="ms-rteCustom-ImageArea" alt=" " src="/Management/RulesToSuccessfulProjects/PublishingImages/RemoteDesktop.gif" border="0" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Enabled Remote Desktop </span>
<p>Remote Desktop works for workstations, but it's not recommended due to a security risk if Remote Support isn't disabled. Also, because of the End User License Agreement (EULA), only allows 1 user at a time, if you logon to client's Windows machine, the client will be logged off. </p>
<p>Of course the second option is a VNC-based remote tool, one of the main difference of a&#160;VNC-based remote tool is it shares the same logon session with the user who is currently logged on the machine. The server administrator doesn't need to give the user&#160;Windows' username and password, nor create a temporary user account. And because of both parties will share the same logon session, we see what the clients see, and so do they. Some clients may prefer this as they know what's happening exactly, which is important for a server. <br>
The VNC tools we prefer&#58; <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Redirect/tightvnc.htm" class="newWindow" target="_blank">TightVNC</a> and <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Redirect/ultravnc.htm" class="newWindow" target="_blank">UltraVNC</a>. </p>
<p><strong>Desktop support</strong></p>
<p>For supporting end users' workstation machines remotely, here is the order you should try with the end users&#58;</p><ul>
    <li><a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaTeamViewer.aspx">TeamViewer</a>&#160;It’s easy, simple and works in most environments.&#160;</li><li><a href="http&#58;//www.skype.com/">Skype​</a>&#160;</li><li><a href="http&#58;//products.office.com/en/lync/lync">Lync</a></li><li><a href="https&#58;//www.mikogo.com/">Mikogo (Free)</a></li><li><a href="https&#58;//www.join.me/">JoinMe</a> (Free)</li>
    <li><a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaUltraVNC.aspx">UltraVNC</a>&#160;(Free)</li>
    <li><a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaCopilot.aspx">Copilot</a>&#160;The final option is to try Copilot - there is no screwing with firewalls at both sides. (Not free)​</li>
</ul>
<p><a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportSampleScript.aspx">SSW Remote Support Standard</a> </p>
<p>See useful tools <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/networkTools.aspx#TeamViewer">The Best 3rd Party Network Tools - TeamViewer</a>.</p>



