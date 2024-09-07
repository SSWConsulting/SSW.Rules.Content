---
seoDescription: User experience should be seamless and intuitive with a standard "Check for Updates" menu option offering clear results.
type: rule
title: Do you know what the user experience should be like?
uri: what-the-user-experience-should-be-like
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:39:00.000Z
archivedreason: outdated
guid: 24f2a833-2d72-40d7-aeb0-3acea67bfc7f
---

You should have a standard menu item "Check for Updates" in the Help menu.

<!--endintro-->

Here are a couple of examples of Check for Updates results:

::: bad
![Figure: Bad example - Skype does a good job, with a green tick and simple message. The actual version number would have made it more complete](checkforupdate_skype.png)
:::

::: bad
![Figure: Bad example - Snagit has horrible UI (red text when it is not an error and Hyperlinks without underlines), however the link to the latest features is not bad](checkforupdate_snagit.png)
:::

::: good
![Figure: Good example - SSW Code Auditor has a great UI (using the freely available component in .NET Toolkit)](codeauditorupdater.png)
:::

#### More Information

If you implement this code from the SSW Toolkit, you will get this UI:

![Figure 1: Help | Check for Updates opens the Updater form](diagnosticsupdater01.jpg)

![Figure 2: Confirmation that they already have the latest version](diagnosticsupdater02.jpg)

![Figure 3: The simple prompt to upgrade when a new version is available](diagnosticsupdater03.jpg)

![Figure 4: Showing the upgrading progress](diagnosticsupdater04.jpg)

![Figure 5: Restarting the application is required because the new version will not take affect until quit and launch the app again](diagnosticsupdater05.jpg)
