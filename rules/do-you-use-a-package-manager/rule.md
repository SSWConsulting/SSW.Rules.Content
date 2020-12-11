---
type: rule
archivedreason: 
title: Do you use a package manager?
guid: 761d75b9-55e6-48bc-bc80-2e02149508a0
uri: do-you-use-a-package-manager
created: 2016-06-17T06:29:18.0000000Z
authors:
- id: 47
  title: Stanley Sidik
related: []

---


A package manager is a collection of software tools that automate the process of installing, upgrading, configuring, and uninstalling computer programs in a consistent manner. <a href="https://chocolatey.org/">Chocolatey</a> is a great package manager, easy to use way to manage software on Windows. <br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt> <img alt="chocolatey.png" src="chocolatey.png" /> <br>
   </dt></dl><p>To get started with Chocolatey open up Command Prompt in Administrative mode, type in: <br></p><pre class="cmd" style="box-sizing:border-box;font-size:0.95em;color:#ffffff;margin-top:0.6em;margin-bottom:0.6em;border-radius:5px;vertical-align:middle;padding:0.5em 0.7em;overflow:auto;line-height:28.8px;background:#000000;">@powershell -NoProfile -ExecutionPolicy Bypass -Com​mand "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin</pre><p>Alternatively, <a href="https://chocolatey.org/install">install Chocolatey via their website</a>.<br></p><p class="ssw15-rteElement-SSW-Only">To find a list of software that we use, along with a PowerShell script to run, check out our <a href="https://intranet.ssw.com.au/SysAdmin/Lists/WinImageInstalledSoftware/AllItems.aspx"> Intranet</a> page. ​</p><div><p class="ssw15-rteElement-P">​​​Alternatives: Homebrew on a Mac​<br></p></div>


