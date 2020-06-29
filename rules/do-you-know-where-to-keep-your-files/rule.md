---
type: rule
title: Do you know where to keep your files?
uri: do-you-know-where-to-keep-your-files
created: 2011-08-29T19:18:47.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo
- id: 66
  title: Liam Elliott

---



<span class='intro'> ​Each client project should have a nice place to keep files. In the old days, things were simple but limited, we simply used Windows Explorer and file shares. Today there are so many places that teams can store documents e.g. Dropbox, OneDrive, SharePoint, TFS, and even Microsoft Teams.<br> </span>

<h3 class="ssw15-rteElement-H3">Which is the best corporate solution?<br></h3><p>The solution that allows the best collaboration with Developers, Project Managers, and other stakeholders is SharePoint and Microsoft Teams. It is super easy to create, upload and share&#160;documents with others.<br></p><h3 class="ssw15-rteElement-H3">What stuff do you need to store?​<br></h3><p>For most projects you need to quickly store and locate important details and documents such as&#58;<br></p><ul><li>Server details (Dev, Test, Production)<br></li><li>Change-log documents<br></li><li>Upcoming features (most often in Word or OneNote)<br></li><li>General documents e.g. Requirements/Specifications (Note&#58; it is possible to share documents from Microsoft Teams externally, but not from Teams directly... just open it in&#160;​Office Online or a specific Office app first)​<br></li></ul><p></p><dl class="badImage"><dt> 
      <img alt="Keep Files Bad Example" src="Dont-keep-files.jpg" /> 
   </dt><dd>Figure&#58; Bad example – It might be easy to use File Shares, your Local C&#58; or emails – but don’t. They don’t work in a team environment as they aren’t easy for others to access</dd></dl><dl class="badImage"><dt> 
      <img alt="Keep Files Bad Example" src="keep-files-TFS.jpg" /> 
   </dt><dd>Figure&#58; Bad example – SharePoint&#160;integrated into TFS is not supported via Visual Studio anymore</dd></dl><dl class="badImage"><dt> 
      <img alt="Keep Files Bad Example" src="keep-files-SP.jpg" /> 
   </dt><dd>Figure&#58; Bad example – even though this is using SharePoint - this is using a Team Site with a Document Library - it is better to use Microsoft Teams which uses SharePoint under the covers</dd></dl><dl class="goodImage"><dt> 
      <img alt="Keep Files Good Example" src="keep-files-sp-teams.jpg" /> 
   </dt><dd>Good example&#58; Use Microsoft Teams and it will automatically create a Site for the Team (and that includes a document library which you can connect to with&#160;OneDrive)</dd></dl><h3 class="ssw15-rteElement-H3">What does not get stored in Microsoft Teams?&#160;<br></h3><p>1.	For developers, <br></p><blockquote style="margin&#58;0px 0px 0px 40px;border&#58;none;padding&#58;0px;"><p>​A&#58; code obviously belongs in github, azure, devops, etc.</p><p>B&#58; Also&#160;the&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=951ffbf9-4066-42f3-a9b7-e0d8603e728b">6 important documents</a>&#160;should be stored in Azure DevOps (was TFS/VSTS).​​.. or instead <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=846474eb-27a1-4645-90ee-10a349fef714">use Markdown with the Wiki</a></p></blockquote><p>2.	For designers with large files, OneDrive is a better choice. See&#58;&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=2df3378d-f923-4f3f-8c86-ec1074f7f98b">Do you know the best Source Control for Designers?</a><br></p><h3>What about usernames and pas​swords?<br></h3><p>Documents with user names and passwords should not be stored in Microsoft Teams. Security is very important for everyone and every company. Use Azure KeyVault or&#160;<a href="http&#58;//keepass.info/" target="_blank">KeePass</a> to store usernames and passwords. KeePass keeps all passwords in one database locked by a master key, which should be accessible only by the few people you trust.<br></p>


