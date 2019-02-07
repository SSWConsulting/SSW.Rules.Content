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
<h3 class="ssw15-rteElement-H3">Desktop support<br></h3><p>For supporting end users' workstation machines remotely, here is the order you should try with the end users&#58;</p><ul><li>
      <a href="https&#58;//products.office.com/en-AU/microsoft-teams/group-chat-software">Microsoft Teams </a> - (recommended) 
      <dl class="image"><dt>
            <img src="/PublishingImages/Teams-give-control.png" alt="Teams-give-control.png" style="width&#58;760px;" />
         </dt><dd>Figure&#58; Teams allow you to give remote control, making it the best option for giving support 
            <br></dd></dl></li><li>
      <a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaTeamViewer.aspx" shape="rect">TeamViewer</a>&#160;&#160;</li><li>
      <a href="http&#58;//www.skype.com/">Skype</a>&#160;- via screen&#160;share&#160;</li><li>
      <a href="https&#58;//www.skype.com/en/business/skype-for-business/">Skype for Business (previously Lync)</a><br></li><li><a href="https&#58;//www.aeroadmin.com/en/">Aeroadmin​</a>&#160;<br></li><li>
      <a href="https&#58;//www.mikogo.com/">Mikogo</a>&#160;(Free)</li><li>
      <a href="https&#58;//www.join.me/">JoinMe</a>&#160;(Free)</li><li>
      <a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportViaUltraVNC.aspx" shape="rect">UltraVNC</a>&#160;(Free)<br></li></ul><h3 class="ssw15-rteElement-H3">Servers<br></h3><p>For server machines, we recommend using either Windows' built-in Remote Desktop (also knows as &quot;Terminal Services&quot;) or a VNC-based tool. Remote Desktop provides each authenticated user a Windows login session that is not shared.&#160;If your client lives in a place where the time zone is different, Remote Desktop should be your first choice as it doesn't need the client's interaction once Remote Desktop is enabled (typically it should have been enabled for a server for the ease for remote maintenance and monitoring). For servers, Remote Desktop is usually enabled via a group policy (AD GPO), although it can also be enabled through Windows System Properties.<br></p><dl class="image"><dt>
      <img alt="remote connection" src="/PublishingImages/remoteconnection.png" border="0" />
   </dt><dd>Figure&#58; Enable Remote Desktop </dd></dl><p>Remote Desktop works for workstations, but it's not recommended due to a security risk if Remote Support isn't disabled. Also, because of the End User License Agreement (EULA), only allows 1 user at a time, if you log in to client's Windows machine, the client will be logged off.</p><p>If you can't use TeamViewer, Skype,&#160;or Remote Desktop, you can try VNC.&#160;There are a number of VNC servers and clients available.&#160;VNC-based sessions typically behave as if you're physically using the computer. This means that it shares the same login session with the user who is currently logged on the machine. VNC software allows you to configure a specific username and password for remote access, which means that you don't have to share Windows usernames&#160;and passwords or create a temporary Windows user account.&#160;Some clients may also prefer this as they can sit in and watch what is happening.<br></p><p>The VNC tools we prefer&#58; ​​<a href="http&#58;//www.ssw.com.au/ssw/Redirect/tightvnc.htm">TightVNC</a> and​ <a href="http&#58;//www.ssw.com.au/ssw/Redirect/ultravnc.htm" target="_blank" shape="rect">Ultra VNC</a>.</p><p>Read <a href="http&#58;//www.ssw.com.au/ssw/Standards/Support/RemoteSupportSampleScript.aspx" shape="rect" style="line-height&#58;1.6;">SSW Remote Support Standard</a>.</p>


