---
type: rule
title: Do you know the quickest way to get your Windows 10 SOE up and running?
uri: do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running
created: 2016-06-20T04:57:19.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 47
  title: Stanley Sidik

---



<span class='intro'> ​Your developers should be using Windows 10 for a <a href="http&#58;//au.pcmag.com/windows-10-preview-release-date-news-features/35511/feature/10-reasons-to-upgrade-to-windows-10"> number of reasons</a>, the primary one being it is faster than Windows 8.<div>The next step is to get the Standard Operating Environment (SOE) installed. You have a few choices&#58;<div><ul><li>Manually - it can take over a day to install your favourite 20 or so apps</li><li>Windows Image - there is overhead of maintaining the .WIM file as software changes</li><li>Use a package manager (eg. chocolatey) - RECOMMENDED</li></ul></div></div> </span>

<h3 class="ssw15-rteElement-H3">Use a package manager (<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=c4c72062-a59d-44fc-8101-8ee008f3ca05">Chocolatey </a>)&#160; <br></h3><p class="ssw15-rteElement-P">Assuming that Windows 10 in already installed, then get your SOE installed fast by following these steps&#58;</p><ol style="list-style-type&#58;decimal;"><li>Logon and configure Windows 10<br></li><li>Install Windows Updates</li><li>Join&#160;laptop to&#160;the Domain (or run a Logon-Script.bat to get printers, Word templates etc. Contact SysAdmin to join laptop to domain)<br></li><li>Install and run&#160;a <a href="file&#58;///fileserver/SetupFiles/SetupNotMS/ChocolateySSWPackages">Chocolatey script</a>&#160;to get most of the software</li><li>Install all rest of the&#160;<a href="https&#58;//intranet.ssw.com.au/SysAdmin/Lists/WinImageInstalledSoftware/AllItems.aspx">standard Software​</a>&#160;that does not&#160;support Chocolatey [SSW Only]​<br></li><li>In case you lose your laptop, it is a good idea to stick a business card to the bottom</li><li>For branding reasons, stick your company sticker to the laptop <br></li></ol><dl class="image"><dt> <img alt="LoginScript.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/LoginScript.jpg" style="width&#58;808px;" /></dt> <dd>Figure&#58; SSWLoginScript.bat <br><br></dd></dl><dl class="image"><dt> <img alt="ChocolateyScript.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/ChocolateyScript.jpg" style="width&#58;808px;height&#58;428px;" /> </dt><dd>Figure&#58; SSWPackages.ps1 which runs Chocolatey command to install SOE&#160;software</dd></dl><dl class="image"><dt> <img alt="NonChocolateySoftware.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/NonChocolateyApp.jpg" style="width&#58;882px;" /> </dt><dd>Figure&#58; SOE Software that are not supported by&#160;Chocolatey</dd></dl><dl class="image"><dt> <img alt="SSWLaptopBranding.jpg" src="/SiteAssets/do-you-know-the-quickest-way-to-get-your-windows-10-soe-up-and-running/SSWLaptopBranding.jpg" /> </dt><dd>Figure&#58; Company&#160;branding on&#160;laptop</dd> </dl>


