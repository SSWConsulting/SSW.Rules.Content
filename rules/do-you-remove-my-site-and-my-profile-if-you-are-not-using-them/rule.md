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

**My Site** and **My Profile<** are great but if you are not using them, it makes sense to remove them:

<!--endintro-->

![Figure: Links need to be hidden](LinksNeedToBeRemove.png) 

You can follow below steps to hide “My Site” and “My Profile”. There are a few options, based on what you need to do:

### Delete the association (not recommended)

1. Going to **Central Admin | Application Management | Service Applications | Configure service application associations**, and choose “default” link:
  
::: bad    
![Figure: Bad example - Choose “default” link](RemoveAssociation.png) 
:::

2. Uncheck the “User Profile Service Application”  in the opened page, then click “OK”:
    
::: bad
![Figure: Bad example - Uncheck the association for "User Profile Service"](RemoveAssociation2.png) 
:::


### Customize permissions for only some people to have access to create personal site

You can remove it for most people - but leave it for only some users.

1. Go to **Central Admin | Application Management | Service Applications | Manage service applications**, and click the link of “User Profile Service Application”, navigate to its manage page:
  
::: ok
![Figure: OK example - “User Profile Service Application” manage page](UserProfileServiceManagePage.png) 
:::

2. Click **People | Manage User Permissions**, you can customize the user profile permission for specific users: 

::: ok
![Figure: OK example - Customize "User Profile Permissions"](CustomUserProfileServicePermission.png) 
:::
  
### Delete the service (recommended if you don't need the service at all in your farm)

**Note:** You can always create it later if you need it in the future.

1. Go to **Central Admin | Application Management | Service Applications | Manage service applications**, and select “User Profile Service Application”, then click the “Delete” button on the ribbon:

::: good
![Figure: Good example - Delete "User Profile Service"](DeleteUserProfileService.png) 
:::

::: greybox
**Note:** Later on if you want to get My Site working read these 2 links... unless Microsoft creates a services that fixes User Profile Synchronization service. Thanks to Mark Rhodes for these tips:

- [“Stuck on Starting”: Common Issues with SharePoint Server 2010 User Profile Synchronization](http://www.harbar.net/articles/sp2010ups2.aspx)
- [Rational Guide to implementing SharePoint Server 2010 User Profile Synchronization](http://www.harbar.net/articles/sp2010ups.aspx)
:::
