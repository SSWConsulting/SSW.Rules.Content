---
type: rule
archivedreason: 
title: Do you know the quickest way to get your Windows 10 SOE up and running?
guid: 434aba3a-381a-474c-b8d3-357d10fc55bf
uri: do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running
created: 2016-06-20T04:57:19.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects: []

---


​Your developers should be using Windows 10 for a <a href="http&#58;//au.pcmag.com/windows-10-preview-release-date-news-features/35511/feature/10-reasons-to-upgrade-to-windows-10"> number of reasons</a>, the primary one being it is faster than Windows 8.<div>The next step is to get the Standard Operating Environment (SOE) installed. You have a few choices&#58;<div><ul><li>Manually - it can take over a day to install your favorite 20 or so apps</li><li>Windows Image - there is an overhead of maintaining the .WIM file as software changes - RECOMMENDED FOR LARGE COMPANIES 100+ NON TECHNICAL STAFF<br></li><li>Use a package manager (eg. chocolatey/Winget​) - RECOMMENDED FOR SMALLER COMPANIES {ltHTMLChar}100<br></li></ul></div></div>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Use a package manager (<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=c4c72062-a59d-44fc-8101-8ee008f3ca05">Chocolatey</a>)&#160; 
   <br></h3><p class="ssw15-rteElement-P">Assuming that Windows 10 is already installed, then get your SOE installed fast by following these steps&#58;</p><ol style="list-style-type&#58;decimal;"><li>Logon and configure Windows 10<br></li><li>Install Windows Updates</li><li>Join&#160;laptop to&#160;the Domain (or run a Logon-Script.bat to get printers, Word templates, etc. Contact SysAdmin to join laptop to the domain)<br></li><li>Install and run&#160;a Chocolatey script&#160;to get most of the software<br> 
      <p class="ssw15-rteElement-SSW-Only"> 
         <a href="file&#58;///fileserver/SetupFiles/SetupNotMS/ChocolateySSWPackages">Chocolatey script</a>&#160;for SSW<br></p></li><li>Install all rest of the&#160;standard Software&#160;that does not&#160;support Chocolatey [SSW Only] &#160; 
      <p class="ssw15-rteElement-SSW-Only"> 
         <a href="https&#58;//intranet.ssw.com.au/SysAdmin/Lists/WinImageInstalledSoftware/AllItems.aspx">Standard Software</a> for SSW​<br></p></li><li>In case you lose your laptop, it is a good idea to stick a business card to the bottom</li><li>For branding reasons, stick your company sticker to the laptop 
      <dl class="image"><dt>
            <img alt="LoginScript.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/LoginScript.jpg" style="width&#58;750px;height&#58;381px;" /> 
         </dt><dd>Figure&#58; SSWLoginScript.bat<br></dd></dl><dl class="image"><dt>
            <img alt="ChocolateyScript.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/ChocolateyScript.jpg" style="width&#58;750px;height&#58;397px;" />
         </dt><dd>Figure&#58; SSWPackages.ps1 which runs Chocolatey command to install SOE&#160;software</dd></dl><dl class="image"><dt>
            <img alt="NonChocolateySoftware.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/NonChocolateyApp.jpg" style="width&#58;750px;height&#58;198px;" />
         </dt><dd>Figure&#58; SOE Software that is not supported by&#160;Chocolatey</dd></dl><dl class="image"><dt>
            <img alt="SSWLaptopBranding.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/SSWLaptopBranding.jpg" />
         </dt><dd>Figure&#58; Company&#160;branding on&#160;laptop​<br></dd></dl></li><li>If you are preparing the machine for someone else or migrating an old PC, you could send an email based on the template below. Don't forget to change the names where necessary&#58;
      <div class="greyBox">Hey Ana,&#160;<br>&#160;<br>Your new computer is ready.&#160;⭐️ &#160;<br>
         <ul><li>Machine name is&#160;COBRA&#160;</li><li>Model&#58; ThinkPad X1 Carbon Gen8&#160;&#160;<br></li><li>Operating System&#58; Windows 10 Enterprise installed and activated.&#160;</li></ul><b>Done</b> - I have followed an SSW Rule&#58;&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=69373d34-e0f7-4a0e-ab58-c438d77af2ce">https&#58;//rules.ssw.com.au/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running</a>&#160;and this included&#58;&#160;<br> 
         <ul><li>Data - I have copied the data files from your old PC (MountainGoat) to your new C&#58; drive&#160;</li><li>Branding - A SSW sticker has been added&#160;</li><li>Power adapter - I labeled it for easy recognition&#160;</li><li>Underneath - I stuck your business card in case it gets stolen<br></li></ul><b>Done</b> - then I followed&#160;a SugarLearning Item&#58;&#160;<a href="https&#58;//my.sugarlearning.com/SSW/items/8159/pc-install-and-configure-your-laptop">https&#58;//my.sugarlearning.com/SSW/items/8159/pc-install-and-configure-your-laptop</a>&#160;and this included&#58;&#160;<br> 
         <ul><li>Software - Installed all your software via Chocolatey&#160;</li><li>Printer - Added the main office printers<br></li></ul><b>Done</b> - then I followed a SysAdmin SugarLearning Item&#58;&#160;<a href="https&#58;//my.sugarlearning.com/SSW/items/13220/snipe-it-asset-management">https&#58;//my.sugarlearning.com/SSW/items/13220/snipe-it-asset-management</a> and this included&#58;<br> 
         <ul><li>Asset - Added the asset to our asset management tool, Snipe-IT&#58; <a href="https&#58;//snipe.ssw.com.au/hardware/593">https&#58;//snipe.ssw.com.au/hardware/593</a></li><li>Underneath - I added a QR Asset Tag (look here if you ever need to know your computer name)&#160;<br></li></ul>Now I need you to do (we can do this together if you are stuck, just give me a call &#128378;)&#160;<br> 
         <ol><li>Now login and check Microsoft - Teams App, Outlook&#160;&#160;</li><li>Now login and check Google - Chrome will bring back your bookmarks</li><li>Plugin external monitors - Configure your screens</li></ol></div></li></ol>​​<br>


