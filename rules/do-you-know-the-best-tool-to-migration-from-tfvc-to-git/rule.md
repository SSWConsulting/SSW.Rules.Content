---
type: rule
archivedreason: 
title: Do you know the best tool to migration from TFVC to Git?
guid: 1e33e748-ca14-40fe-bd9e-36f992f9d2c2
uri: do-you-know-the-best-tool-to-migration-from-tfvc-to-git
created: 2017-04-03T23:23:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related:
- do-you-use-version-control-with-power-bi
redirects: []

---

Git has become the defacto standard for version control systems. It's distributed and decentralized and promotes working disconnected as default. It also takes away the pain of branching and merging and has a built in code review system with pull requests. Everybody should be using Git, and if you're not, you should be migrating the Git using one of the below tools.


* VisualStudio.com - Import Repository
* Git-Tf
* Git-Tfs (recommended)



<!--endintro-->

### VisualStudio.com - Import Repository


VisualStudio.com gives you the ability to import from a TFVC repository into a new Git repository.

![](03_29_08.png)


::: bad
Bad Example - Built in tool has several limitations

:::

If you don't care about source control history, then this inbuilt tool is the easiest to use. It has the limitations of:


* 180 days of history
* No branches



::: greybox
 **TIP -** Use this if you don't care about source control history

:::
 

### Git -Tf 

[Git-Tf](https://www.microsoft.com/en-us/download/details.aspx?id=30474) is an open source command line tool  that works cross platform and use the Java TFS SDK. This tool is useful for migration if you're not on a Windows environment. This tool is not maintained and has issues with migrating branches. 



To see how to use this to migrate see ["Migrate an existing project from TFS to Git with changeset history intact" from Chris Kirby](https://chriskirby.net/blog/migrate-an-existing-project-from-tfs-to-github-with-changeset-history-intact)



::: greybox
 **TIP -** Use Git-Tf if you don't have a Windows environment

:::


### Git-Tfs ( Recommended)



[Git-Tfs](https://github.com/git-tfs/git-tfs) is an open source command line tool that uses the .NET TFS SDK to interface between Git and TFVC. It has the following advantages over the other tools:



* Actively maintained
* Good support for branches
* Author mapping
* Migrates all history


Follow the [migration guide](https://github.com/git-tfs/git-tfs/blob/master/doc/usecases/migrate_tfs_to_git.md) to import from TFVC to Git and then proceed with [the after migration steps](/do-you-know-what-to-do-after-migrating-from-tfvc-to-git).
To help you do a smoother migration, you can refer to this [tool](/tfs-master-do-you-have-a-report-to-see-who-has-not-checked-in).
