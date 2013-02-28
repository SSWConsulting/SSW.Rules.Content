---
type: rule
archivedreason: 
title: Do you use TFS 2012 instead of TFS 2010?
guid: 26028e7b-a84b-4a43-b65d-42a66a050c7c
uri: do-you-use-tfs-2012-instead-of-tfs-2010
created: 2009-11-05T06:35:33.0000000Z
authors:
- title: Lei Xu
  url: https://ssw.com.au/people/lei-xu
related: []
redirects: []

---


<p>With the release of TFS 2012, you should always use TFS 2012 instead of TFS 2010. <br>
<br>
<strong>Async checkout</strong><br>There is a new TFS 2012 feature so that VS 2012 will do checkouts in the background for server workspaces.&#160; That eliminates the pause when you start typing and VS checks out the file.&#160; Turning it on turns off checkout locks, but you can still use checkin locks.&#160; </p><p><strong>Merge on Unshelve</strong> <br>Shelvesets can now be unshelved into a workspace even if there are local changes on files in the shelveset.&#160; Conflicts will be created for any items modified both locally and in the shelveset, and you will resolve them as you would any other conflict. </p><p><strong>Local workspaces </strong><br>Local workspaces allow many operations to be done offline (add, edit, rename, delete, undo, diff) and are recommended only for workspaces with fewer 50,000 files.&#160; Local workspaces are now the default with TFS 2012, but you can control that if you want server workspaces to be the default.</p>
<br><excerpt class='endintro'></excerpt><br>



