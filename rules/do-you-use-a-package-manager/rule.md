---
type: rule
title: Do you use a package manager?
uri: do-you-use-a-package-manager
created: 2016-06-17T06:29:18.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> A package manager is a collection of software tools that automate the process of installing, upgrading, configuring, and uninstalling computer programs in a consistent manner. <a href="https&#58;//chocolatey.org/">Chocolatey</a>&#160;is a great package manager, easy to use way to manage software on Windows. <br> </span>

<dl class="image"><dt> <img alt="chocolatey.png" src="/SiteAssets/do-you-use-a-package-manager/chocolatey.png" /> <br>
   </dt></dl><p>To get started with Chocolatey open up Command Prompt in Administrative mode, type in&#58;&#160;<br></p><pre class="cmd" style="box-sizing&#58;border-box;font-size&#58;0.95em;color&#58;#ffffff;margin-top&#58;0.6em;margin-bottom&#58;0.6em;border-radius&#58;5px;vertical-align&#58;middle;padding&#58;0.5em 0.7em;overflow&#58;auto;line-height&#58;28.8px;background&#58;#000000;">@powershell -NoProfile -ExecutionPolicy Bypass -Com​mand &quot;iex ((new-object net.webclient).DownloadString('https&#58;//chocolatey.org/install.ps1'))&quot; &amp;&amp; SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin</pre><p>Alternatively,&#160;<a href="https&#58;//chocolatey.org/install">install Chocolatey via their website</a>.<br></p><p class="ssw15-rteElement-SSW-Only">To find a list of software that we use, along with a PowerShell&#160;script to run,&#160;check out our <a href="https&#58;//intranet.ssw.com.au/SysAdmin/Lists/WinImageInstalledSoftware/AllItems.aspx"> Intranet</a>&#160;page. ​</p><div><p class="ssw15-rteElement-P">​​​Alternatives&#58; Homebrew on a Mac​<br></p></div>


