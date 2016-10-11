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
<br>
<br><excerpt class='endintro'></excerpt><br>

  <p><strong style="line-height&#58;1.6;"><br>Desktop support</strong><br></p><p>For supporting end users' workstation machines remotely, here is the order you should try with the end users&#58;</p><ul><li><a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaTeamViewer.aspx" shape="rect">TeamViewer</a>&#160;It’s easy, simple and works in most environments.&#160;</li><li><a href="http&#58;//www.skype.com/">Skype​</a>&#160;- via screen&#160;share&#160;</li><li><a href="http&#58;//products.office.com/en/lync/lync">Skype for Business (previously Lync)</a></li><li><a href="https&#58;//www.mikogo.com/">Mikogo</a>&#160;(Free)</li><li><a href="https&#58;//www.join.me/">JoinMe</a>&#160;(Free)</li><li><a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaUltraVNC.aspx" shape="rect">UltraVNC</a>&#160;(Free)</li><li><a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaCopilot.aspx" shape="rect">Copilot</a>.&#160;This is a last option, and does not require changes to firewalls at either end (not free)​​.</li></ul><p><strong style="line-height&#58;1.6;">Servers</strong><br></p>
<p>For server machines, we recommend using either Windows' built-in Remote Desktop (also knows as &quot;Terminal Services&quot;) or a VNC-based tool. Remote Desktop provides each authenticated user a Windows logon session that is not shared.&#160;If your client lives in a place where the time zone is different, Remote Desktop should be your first choice as it doesn't need the client's interaction once Remote Desktop is enabled (typically it should have been enabled for a server for the ease for remote maintenance and monitoring). For servers, Remote Desktop is usually enabled via a group policy (AD GPO), although it can also be enabled through Windows System Properties.<br></p>
<img class="ms-rteCustom-ImageArea" alt=" " src="/PublishingImages/remoteconnection.png" border="0" style="width&#58;426px;" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Enabled Remote Desktop </span>
<p>Remote Desktop works for workstations, but it's not recommended due to a security risk if Remote Support isn't disabled. Also, because of the End User License Agreement (EULA), only allows 1 user at a time, if you logon to client's Windows machine, the client will be logged off. </p>
<p>If you can't use TeamViewer, Skype,&#160;or Remote Desktop, you can try VNC.&#160;There are a number of VNC servers and clients available.&#160;VNC-based sessions typically behave as if you're physically​ using the computer. This means that it shares the same logon session with the user who is currently logged on the machine. VNC software allows you to configure a specific username and password for remote access, which means that you don't have to share Windows usernames and passwords, or create a temporary Windows user account.&#160;Some clients may also prefer this as they can sit in and watch what is happening.<br>
The VNC tools we prefer&#58; <a class="newWindow" href="http&#58;//www.ssw.com.au/ssw/Redirect/tightvnc.htm" target="_blank" shape="rect">TightVNC</a> and <a class="newWindow" href="http&#58;//www.ssw.com.au/ssw/Redirect/ultravnc.htm" target="_blank" shape="rect">UltraVNC</a>.<br><span style="line-height&#58;1.6;"><br>Do you know t</span><span style="line-height&#58;1.6;">he best way to handle a support call?</span><span style="line-height&#58;1.6;"> -&#160;​</span><a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportSampleScript.aspx" shape="rect" style="line-height&#58;1.6;">SSW Remote Support Standard</a></p>
<p>See useful tools <a href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/networkTools.aspx#TeamViewer" shape="rect">The Best 3rd Party Network Tools - TeamViewer</a>.</p>



