---
type: rule
title: Do you disable connections?
uri: do-you-disable-connections
created: 2015-08-12T15:42:01.0000000Z
authors: []

---



<span class='intro'> <p>It is important that while you're upgrading, nobody can check in.&#160; Any check-ins after you backup your database will be lost.</p><p>To make sure that nobody can change anything during the upgrade, follow these steps.</p> </span>

<p>a.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Send out an email notifying everyone TFS will be unavailable for the upgrade period<br> Follow&#160;<a href="http&#58;//www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart">Rules to better Networks</a>&#160; </p><p>b.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Make sure nobody can check in files&#58;</p><p>&#160;.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Open the TFS Administration Console on the server.</p><p>a.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Navigate to Application Tier / Team Project Collections.</p><p>b.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; For each Team Project Collection, select it, and click &quot;Stop Collection&quot;. Enter a useful message (this will be displayed to users trying to connect from Visual Studio) and click &quot;Stop&quot;&#58;</p><p><img src="/SiteAssets/do-you-disable-connections-1/stop%20each%20term.png" alt="stop each term.png" style="margin&#58;5px;width&#58;650px;" /><br></p><p><strong>Figure&#58; Stop each Team Project Collection</strong></p><p>&#160;</p><p><img src="/SiteAssets/do-you-disable-connections-1/all%20team%20project.png" alt="all team project.png" style="margin&#58;5px;width&#58;650px;" /><br></p><p><strong>Figure&#58; All Team Project Collections are stopped</strong></p><p>c.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; In Visual Studio, confirm you can no longer connect to TFS</p><p><br></p><p><img src="/SiteAssets/do-you-disable-connections-1/visual%20studio.png" alt="visual studio.png" style="margin&#58;5px;" /><br></p><p><strong>Figure&#58; Visual Studio shows the message that you entered when you stopped the Team Project Collection</strong><br> <br></p>


