---
type: rule
archivedreason: 
title: Do you know what to do after migrating from TFVC to Git?
guid: 07aa6cb8-2115-4648-b308-56a110218a09
uri: do-you-know-what-to-do-after-migrating-from-tfvc-to-git
created: 2017-04-05T00:34:51.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---

After you [use the right tool to migrate from TFVC to Git](/Pages/Do-you-know-the-best-tool-to-migration-from-TFVC-to-Git.aspx), there's a few more things you need to do to clean things up for a new user joining the project. By default, if there is a TFVC repository, that will become the default in the UI.




Unfortunately, you can't kill the TFVC repository and make Git the default one, so there's a few steps you need to follow.







<!--endintro-->

![](2017-04-05_10-02-58.png)


::: bad
Figure: Bad Example - Can't delete the now deprecated TFVC repository

:::

### Delete files from TFVC


Go into the repository, delete any existing files. Add a new document saying "\_Migrated\_to\_Git.md". This will stop people from getting the wrong code.

![](2017-04-05_10-24-52.png)
 **Figure: Clean up TFVC so developers can't accidentally get the wrong source code
** **
** 
**Note** : All the source code is still there, it's just flagged as being deleted.

### Lock down TFVC


In the TFVC repository, click Security

![](2017-04-05_10-43-51.png)
 **Figure: Configure the security of the TFVC repository
** 
Then deny check-ins to  **Contributors** , P **roject Administrators** and  **Project Collection Administrators** . This should stop anyone from committing new code to the repository.

### Update the Dashboard


Next step is to update the dashboard to let new developers know.

![](2017-04-05_10-30-43.png)


::: good
Figure: Good example - Let new users know that the source control is now on Git

:::



### Suggestions for the VSTS team


1. Give us the ability to hide a repository
2. Give us the ability to set a repository as the default for all users
3. Give us the ability to delete a TFVC repository



Having any of these suggestions will avoid the confusion on this screen


![](2017-04-05_10-06-12.png)



::: bad
Figure: Bad Exmaple - This is confusing for a new dev

:::
