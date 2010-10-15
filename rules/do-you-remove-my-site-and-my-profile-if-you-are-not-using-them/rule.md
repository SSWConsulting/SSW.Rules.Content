---
type: rule
title: Do you remove ‘My Site’ and ‘My Profile’ if you are not using them?
uri: do-you-remove-my-site-and-my-profile-if-you-are-not-using-them
created: 2010-10-15T08:33:09.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 8
  title: John Liu
- id: 9
  title: William Yin

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

  <span lang="EN-US">
<font>
<font>You can follow below steps to&#160;hide “My Site” and “My Profile”,<br>
</font>
<br>
There are a few options, based on what you need to do&#58;</font> <br>
</span>
<span>
<span>
<font>1.</font>
<span style="font&#58;7pt 'times new roman';">&#160;&#160;&#160; </span>
</span>
</span>
<span lang="EN-US">
<font>Delete the association (not recommended)<br>
</font></span><span><span><font>a.</font>
<span style="font&#58;7pt 'times new roman';">&#160;&#160;&#160; </span>
</span>
</span>
<span>
<font>Go to <strong>Central Admin</strong> | <strong>Application Management</strong> | <strong>Service Applications</strong> | <strong>Configure service application associations</strong>,&#160;<br>
<font>Choose “default” link&#58;</font></font>
</span>
<font>
<br>
</font>
<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/RemoveAssociation.png" />
<br>
<font class="ms-rteCustom-FigureNormal">
Figure&#58; Choose “default” link</font>
<p>
<font>b.Uncheck the “<strong>User Profile Service Application</strong>”&#160; in the opened page, then click “<strong>OK</strong>”&#58;<span lang="EN-US">
<font><font>
<img alt="" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/RemoveAssociation2.png" /><br>
</font></font></span></font><font size="+0" class="ms-rteCustom-FigureNormal">Figure&#58; uncheck the association for user profile service</font></p>
<p><span lang="EN-US"><span><font>2.</font> </span><font>Delete the service (recommended)<br>
Recommended if you don't need the service at all in your farm.<br>
<strong>Note</strong>&#58; You can always create it later if you need it in the future.<br>
<br>
Go to <strong>Central Admin</strong> | <strong>Application Management</strong> | <strong>Service Applications</strong> | <strong>Manage service applications</strong>,<strong></strong></font></span></p>
<p><span lang="EN-US"><font>Select “User Profile Service Application”, then click the “Delete” button on the ribbon&#58;</font></span><strong><span lang="EN-US"><font><font><strong><span lang="EN-US"><font><span lang="EN-US"><font><font><img alt="" height="278" width="855" style="width&#58;830px;height&#58;252px;" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/DeleteUserProfileService.png" class="ms-rteCustom-ImageArea" /></font></font></span></font></span></strong></font><br>
</font></span></strong><font class="ms-rteCustom-FigureNormal"><span class="ms-rteCustom-FigureNormal">Figure&#58; how to delete user profile service<span lang="EN-US"><font>&#160;</font></span></span><span lang="EN-US"><font></font></span></font></p>
<p><span lang="EN-US"><span><font>3.</font><span style="font&#58;7pt 'times new roman';">&#160;&#160;&#160; </span></span></span><span lang="EN-US"><font>Customize permissions for only some people to have access to create personal site </font></span></p>
<p><font>You can remove it for most people - but leave it for only some users.</font></p>
<p><span lang="EN-US"><span><font>a.</font><span style="font&#58;7pt 'times new roman';">&#160;&#160;&#160; </span></span></span><span lang="EN-US"><font>Go to <strong>Central Admin</strong> | <strong>Application Management</strong> | <strong>Service Applications</strong> | <strong>Manage service applications</strong>,</font></span></p>
<p><span lang="EN-US"><font>Click the link of “User Profile Service Application”, navigate to its manage page&#58;</font></span><strong><span lang="EN-US"><font><font><strong><span lang="EN-US"><font><span lang="EN-US"><font><font><img alt="" height="277" width="827" class="ms-rteCustom-ImageArea" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/UserProfileServiceManagePage.png" /></font></font></span></font></span></strong></font><br>
</font></span></strong><font size="+0" class="ms-rteCustom-FigureNormal">Figure&#58; “User Profile Service Application” manage page</font></p>
<p><span><span><font>b.</font><span style="font&#58;7pt 'times new roman';">&#160;&#160;&#160; </span></span></span><font>Click <strong>People</strong> | <strong>Manage User Permissions</strong>, you can customize the user profile permission for specific users&#58;</font><strong><font><font><strong><font><span lang="EN-US"><font><font><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/CustomUserProfileServicePermission.png" class="ms-rteCustom-ImageArea" /></font></font></span></font></strong></font><br>
</font></strong><span class="ms-rteCustom-FigureNormal">Figure&#58; customize User profile permission</span></p>
<p><strong><span lang="EN-US"><font>Note</font></span></strong><span lang="EN-US"><font>&#58; Later on if you want to get My Site working read these 2 links… unless Microsoft creates a services that fixes User Profile Synchronization service…. thanks to Mark Rhodes for these tips…<br>
</font><a href="http&#58;//www.harbar.net/articles/sp2010ups2.aspx"><font color="#0000ff">http&#58;//www.harbar.net/articles/sp2010ups2.aspx</font></a><font> and </font><a href="http&#58;//www.harbar.net/articles/sp2010ups.aspx"><font>http&#58;//www.harbar.net/articles/sp2010ups.aspx</font></a></span></p>



