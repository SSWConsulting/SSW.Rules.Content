---
seoDescription: Remove orphaned users from SharePoint and prevent permissions issues with ShareGate's easy-to-use solution.
type: rule
title: Do you remove orphaned users from SharePoint?
uri: sharepoint-removing-orphaned-users
authors:
  - title: Warwick Leahy
    url: https://www.ssw.com.au/people/warwick-leahy
created: 2021-09-06T23:16:37.291Z
guid: cbd3e21a-bcbb-408e-9e8d-b010b5ce8edc
---

Did you know that when you delete or disable a user in Active Directory or Azure Active Directory the user is still stored in SharePoint. Did you also know that SharePoint retains any permissions that the user did have in SharePoint at the time? This means that if the user returns and their account is re-enabled they will have all of the same permissions that they had before. Luckily for us ShareGate offer us an easy way to remove these 'orphaned users'.

<!--endintro-->

1. Open ShareGate Desktop

2. Click All reports | Orphaned user report
   ![Figure: Orphaned user report](step2-orphaneduser.png "Figure: Open orphaned user report")
3. Add your connection
   ![Figure: Add connection](step3-orphaneduser.png "Add your connection")

4. Add your site address, Choose your Authentication method and press Connect
   ![Figure: Connect to your environment](step4-orphaneduser.png "Connect to your enviroment")

5. Choose Navigate to choose individual sites or tick the box to choose all sites and teams folders
   ![Figure: Choose navigate or tick](step5-orphaneduser.png)

6. Under Navigate choose the individual site | Click Next
   ![Figure: Choose site](step6-orphaneduser.png)

7. Click Run now
   ![Figure: Choose Run now](step7-orphaneduser.png "Run Now")

8. Select Users | Select Clean orphaned users
   ![Figure: Clean orphaned users](step8-orphaneduser.png "Clean orphaned users")

9. Click Continue
   ![Figure: Continue](step9-orphaneduser.png "Continue")

10. View results of report
    ![Figure: Report Results](step10-orphaneduser.png)
