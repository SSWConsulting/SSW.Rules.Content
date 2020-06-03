---
type: rule
title: Do you know how to fix people's display name in SharePoint ?
uri: do-you-know-how-to-fix-peoples-display-name-in-sharepoint-
created: 2011-05-20T01:51:03.0000000Z
authors:
- id: 8
  title: John Liu

---



<span class='intro'> When SharePoint encounters a new person, it takes people's display name and account name from Active Directory, but sometimes
 </span>


  <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/MixUpNames.jpg" />&#160;<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Mixed up names - some are good Display Name, some are essentially just the Account Name</font> (More here) <br>
<ol>The easiest way to fix this requires someone with central administration access&#58;
    <li>Go to&#58; SharePoint Central Administration | Application Management | Service Applications | Manage Service applications <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/ServiceApplication.jpg" /></li>
    <li>Go to User Profile Service Application<br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/UserProfileServiceApplication.jpg" /> </li>
    <li>Go to Manage User Profiles <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/ManageUserProfiles.jpg" /> </li>
    <li>Find the user profile that you want to update <br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/FindUserProfile.jpg" /></li>
    <li>Fix the Name field (Display name)<br>
    <img alt="" class="ms-rteCustom-ImageArea" src="/PublishingImages/FixNameField.jpg" />&#160;</li>
    <li>Save</li>
</ol>
<p>Better way<br>
The better way is to set up User Profile Synchronization and have SharePoint communicate with Active Directory on a schedule and keep user's profile information up to date. Unfortunately, it can be tricky to set this up in SharePoint 2010. </p>
<p>Technical<br>
When a user is entered (or using) a SharePoint site, the site will first check with Central Admin (the farm) to enquire about this user's profile details. The farm grabs the account name and display name from Active Directory, but does not keep this synchronized. </p>
<p>Unless configured otherwise, end users in SharePoint do not have the ability to modify their own display name. And the best place to update this is to either&#58;</p>
<ol>
    <li>Modify the farm user information list cache (via steps above), or </li>
    <li>Set up User Profile Synchronization </li>
</ol>



