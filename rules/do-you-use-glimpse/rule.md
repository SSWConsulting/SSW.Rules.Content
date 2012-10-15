---
type: rule
title: Do you use Glimpse?
uri: do-you-use-glimpse
created: 2012-04-02T15:08:43.0000000Z
authors:
- id: 3
  title: Eric Phan

---



<span class='intro'> Glimpse allow you to easily perform diagnostics on your MVC application at runtime. </span>

<p>You can find useful information like&#58;</p>
<ul>
<li>Routing information</li>
<li>Profiling</li>
<li>Request information</li>
<li>Parameters passed into actions</li>
<li>Model inspector</li>
</ul>
<p>Glimpse is available on NuGet, so it’s a simple matter to get it up and running on your application. You can find out more from <a href="http&#58;//getglimpse.com/" target="_blank">their website</a>.</p>
<img class="ms-rteCustom-ImageArea" alt="glimpse.png" src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/glimpse.png" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Glimpse in action - We can see which routes were chosen for this page, and the parameters used by the controller</span><span class="ms-rteCustom-FigureNormal"></span>
<h2>Securing Glimpse for production use</h2>
<p>Glimpse is very powerful but there are some considerations to be addressed before using it on Production.
</p>
<ul><li>1. Security&#58; Enabling Glimpse can reveal many details about your server – including full database connection details. Glimpse also publishes a full list of all the actions your MVC site can perform so you should thoroughly test the security on all restricted actions before you consider enabling Glimpse.
</li>
<li>2. Performance&#58; Running Glimpse involves sending debug data with every request. This can impact site performance.
</li></ul>

<p>Even with these considerations, Glimpse can provide some unique insights into production server performance so it’s worth spending the time to correctly configure Glimpse for production use.</p>

<h4>Glimpse on Production Level 1&#58; Developers Only</h4>
<p>Install Glimpse on production so that only internal developers can enable it.This is achieved by&#58;
</p>
<ul><li>Limiting access to an ip address range.
<br>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">glimpse</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">enabled</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">true</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">ipAddresses</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">add</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">address</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">127.0.0.1</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> /&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">add</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">addressRange</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">192.168.1.1/24</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> /&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">add</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">address</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#58;&#58;1</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> /&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160; &lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">ipAddresses</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160; &lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">glimpse</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;<br><span style="color&#58;rgb(0, 0, 0);font-family&#58;'calibri','sans-serif';font-size&#58;11pt;"><strong>Figure&#58; Glimpse is
now limited to localhost and the 192.168.1.x network</strong></span></span><span style="font-family&#58;'calibri','sans-serif';font-size&#58;11pt;"><br>
<br>
</span></li>
<li>Using role-based authentication.<br>If your site has role-based authentication, you can secure Glimpse usage by editing web.config to control access to the Glimpse.axd location.<br>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">location</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">path</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">glimpse.axd</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;text-indent&#58;36pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">system.web</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160;&#160; &#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">authorization</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">allow</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">roles</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">Developers</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> /&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">deny</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">users</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">*</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">
/&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160; &#160;&#160; &#160;&#160;&lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">authorization</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;text-indent&#58;36pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">system.web</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">location</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">

<div style="margin&#58;0cm 0cm 0pt;color&#58;rgb(0, 0, 0);"><b><font face="Calibri">Figure&#58; Glimpse is restricted to the Developers group</font></b></div>

</span></div>

</li></ul>
<p>&#160;</p>

<h4>Glimpse on Production Level 2&#58; Public by invitation only</h4>
<p>If an end-user reports a problem on your website it can be useful to temporarily enable Glimpse for that user. Glimpse also has remote features allowing developers to see the user’s Glimpse data.
</p>
<ul><li>Create a new authentication role such as &quot;PublicGlimpseUsers&quot;</li>
<li>Edit web.config to control access to Glimpse.axd<br>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">location</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">path</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">glimpse.axd</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;text-indent&#58;36pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">system.web</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160;&#160; &#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">authorization</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">allow</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">roles</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">Developers, PublicGlimpseUsers</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> /&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160;
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">deny</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">users</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">*</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">
/&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160; &#160;&#160; &#160;&#160;&lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">authorization</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;text-indent&#58;36pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">system.web</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;rgb(0, 0, 0);font-family&#58;consolas;font-size&#58;9.5pt;">&lt;/</span><span style="background&#58;white;color&#58;rgb(0, 0, 0);font-family&#58;consolas;font-size&#58;9.5pt;">location</span><span style="background&#58;white;color&#58;rgb(0, 0, 0);font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"><span style="color&#58;rgb(0, 0, 0);">

</span><div style="margin&#58;0cm 0cm 0pt;"><b><font face="Calibri"><span style="color&#58;rgb(0, 0, 0);">Figure&#58; Glimpse.axd is now restricted to Developers&#160;
and PublicGlimpseUsers </span><br></font></b></div>

</span></div>

</li>
<li>Disable the “config” section of Glimpse so that site connection strings are not published. <br>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">pluginBlacklist</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&#160;&#160;&#160;&#160;&#160; &lt;</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">add</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> </span><span style="background&#58;white;color&#58;red;font-family&#58;consolas;font-size&#58;9.5pt;">plugin</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">=</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">Glimpse.Core.Plugin.Config</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;">&quot;</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"> /&gt;</span><span style="background&#58;white;color&#58;black;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

<div style="margin&#58;0cm 0cm 0pt;"><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&lt;/</span><span style="background&#58;white;font-family&#58;consolas;font-size&#58;9.5pt;">pluginBlacklist</span><span style="background&#58;white;color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;">&gt;<br><b style="color&#58;rgb(0, 0, 0);"><font face="Calibri">Figure&#58; How to disable the Config tab </font></b>

</span><span style="color&#58;blue;font-family&#58;consolas;font-size&#58;9.5pt;"></span></div>

</li>
<p>&#160;</p></ul>


