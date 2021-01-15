---
type: rule
archivedreason: 
title: Do you remove ‘My Site’ and ‘My Profile’ if you are not using them?
guid: c3c61ed0-5a66-4783-9b24-4844e1d2c62a
uri: do-you-remove-my-site-and-my-profile-if-you-are-not-using-them
created: 2010-10-15T08:33:09.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-remove-my-site’-and-my-profile’-if-you-are-not-using-them

---

<font> <strong>My Site</strong> and  <strong>My Profile</strong> are great but if you are not using them, it makes sense to remove them:<font>

</font></font>![](LinksNeedToBeRemove.png)**Figure: Links need to be hidden** 

<!--endintro-->

<font>You can follow below steps to hide “My Site” and “My Profile”,

There are a few options, based on what you need to do:
</font>
<font></font>
<font>    <li> <strong>Delete the association</strong> (not recommended)
    <blockquote dir="ltr" style="margin-right:0px;">
    <p>
    a.<span style="font:7pt 'times new roman';"> </span>Go to  <strong>Central Admin</strong> |  <strong>Application Management</strong> |  <strong>Service Applications</strong> |  <strong>Configure service application associations</strong> , 

    Choose “default” link:
    

    <img alt="" height="384" width="569" class="ms-rteCustom-ImageArea" src="RemoveAssociation.png">
::: bad
Figure: Choose “default” link  
:::
</p>
    <p>
    b.Uncheck the “ <strong>User Profile Service Application</strong> ”  in the
    opened page, then click “ <strong>OK</strong> ”:<span lang="EN-US">
    <img alt="" height="453" width="570" class="ms-rteCustom-ImageArea" src="RemoveAssociation2.png">

    </span>
    
::: bad
Figure: uncheck the association for user
    profile service  
:::
</p>
    </blockquote>
    </li>
    <li> <strong>Customize permissions for only some people to have access to create personal site</strong> <blockquote dir="ltr" style="margin-right:0px;">
    <p>
    You can remove it for most people - but leave it for only some users.
    </p>
    <p>
    <span lang="EN-US">a.<span style="font:7pt 'times new roman';">   
    </span>Go to  <strong>Central Admin</strong> |  <strong>Application Management</strong> |  <strong>Service Applications</strong> |  <strong>Manage service applications</strong> ,

    Click the link of “User Profile Service Application”, navigate to its manage
    page:</span> <strong><span lang="EN-US"><img alt="" height="241" width="573" class="ms-rteCustom-ImageArea" src="UserProfileServiceManagePage.png">

    </span></strong> 
::: good
Figure: “User Profile
    Service Application” manage page  
:::
</p>
    <p>
    b.<span style="font:7pt 'times new roman';">    </span>Click
     <strong>People</strong> |  <strong>Manage User Permissions</strong> , you can
    customize the user profile permission for specific users: <strong><span lang="EN-US"><img alt="" height="431" width="498" class="ms-rteCustom-ImageArea" src="CustomUserProfileServicePermission.png"></span>
</strong> <span class="ms-rteCustom-FigureGood">Figure: Better - customize User profile
    permission</span></p>
    <p></p>
    </blockquote>
    </li>
    <li> <strong>Delete the service</strong> (recommended if you don't need the service at all in your farm)
    <blockquote dir="ltr" style="margin-right:0px;">
    <p>
     <strong>Note</strong> : You can always create it later if you need it in the
    future.

    

    Go to  <strong>Central Admin</strong> |  <strong>Application Management</strong> |
     <strong>Service Applications</strong> |  <strong>Manage service applications</strong> ,
    </p>
    <p>
    <span lang="EN-US">Select “User Profile Service Application”, then click the
    “Delete” button on the ribbon:</span> <strong><span lang="EN-US"><img alt="" height="201" width="572" class="ms-rteCustom-ImageArea" src="DeleteUserProfileService.png">

    </span></strong> <strong> <strong><span class="ms-rteCustom-FigureGood">Figure: Best - delete user profile
    service</span></strong> </strong> </p>
    </blockquote>
    </li>
    </font>
<font>        </font>
<font>             <strong><span lang="EN-US"><font>Note</font></span></strong> <span lang="EN-US"><font>:
    Later on if you want to get My Site working read these 2 links… unless Microsoft
    creates a services that fixes User Profile Synchronization service…. thanks to
    Mark Rhodes for these tips…

    </font><a href="http://www.harbar.net/articles/sp2010ups2.aspx">
    <font color="#0000ff">http://www.harbar.net/articles/sp2010ups2.aspx</font></a><font>
    and </font><a href="http://www.harbar.net/articles/sp2010ups.aspx"><font>
    http://www.harbar.net/articles/sp2010ups.aspx </font></a></span></font>
<font></font>
[<font>

    </font>](http://www.harbar.net/articles/sp2010ups.aspx)
