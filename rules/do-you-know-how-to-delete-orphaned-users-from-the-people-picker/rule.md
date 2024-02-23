---
type: rule
archivedreason: 
title: Do you know how to delete orphaned users from the People Picker?
guid: c31997cb-b93b-42a7-8c6c-41efeea1d0db
uri: do-you-know-how-to-delete-orphaned-users-from-the-people-picker
created: 2012-02-27T15:49:49.0000000Z
authors: []
related: []
redirects: []

---

The SharePoint "People Picker" is a great tool for quickly selecting users of your SharePoint site. It allows you to quickly select users from your organization by browsing Active Directory.
<!--endintro-->
![caption](PeoplePicker.jpg)
**Figure: The People Picker**
Unfortunately, if you have added users directly to your site collection, and later deleted or disabled them from Active Directory, you will notice that these orphaned users will still appear in your People Picker. This will eventually clutter up your People Picker.
![caption](PeoplePicker-deleted.jpg)
**Figure: A user in the People Picker that was deleted from Active Directory** ![caption](PeoplePicker-searching.jpg)
**Figure: Searching in Active Directory for the user shows the user is in fact deleted**
To remove these orphaned users, as a SharePoint Administrator, you can open the following URL (where <www.northwind.com> is your SharePoint URL):

* `http://www.northwind.com/\_catalogs/users/sample.aspx`

On this page you will find a list of all the users that are members of your site collection, including the orphaned users.
![caption](PeoplePicker-found.jpg)
**Figure: We have found our orphaned user!**
To remove the user simply click on the  **Username** | Click  **Delete User from Site Collection** . This will instantly remove the user from the People Picker.
