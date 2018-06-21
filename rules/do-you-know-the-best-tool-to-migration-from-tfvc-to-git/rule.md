---
type: rule
title: Do you know the best tool to migration from TFVC to Git?
uri: do-you-know-the-best-tool-to-migration-from-tfvc-to-git
created: 2017-04-03T23:23:08.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
- id: 46
  title: Danijel Malik

---



<span class='intro'> Git has become the defacto standard for version control systems. It's distributed and decentralized and promotes working disconnected&#160;as default. It also takes away the pain of branching and merging and has a built in code review system with pull requests. Everybody should be using Git, and&#160;if you're not, you should be migrating the Git using one of the below tools.<br><div><ul><li>VisualStudio.com - Import Repository<br></li><li>Git-Tf<br></li><li>Git-Tfs (recommended)<br></li></ul></div> </span>

<h3 class="ssw15-rteElement-H3">VisualStudio.com - Import Repository<br></h3><p>VisualStudio.com gives you the ability to import from a TFVC repository into a new Git repository.&#160;<br></p><p><img src="/SiteAssets/do-you-know-the-best-tool-to-migration-from-tfvc-to-git/03_29_08.png" alt="03_29_08.png" style="margin&#58;5px;" /><br></p><dd class="ssw15-rteElement-FigureBad">Bad Example - Built in tool has several limitations<br></dd><div>If you don't care about source control history, then this inbuilt tool is the easiest to use. It has the limitations of&#58;</div><div><ul><li>180 days of history<br></li><li>No branches<br></li></ul><p class="ssw15-rteElement-GreyBox"><strong>TIP - </strong>Use this if you don't care about source control history<br></p> </div><h3 class="ssw15-rteElement-H3">Git -Tf&#160;<br></h3><a href="https&#58;//gittf.codeplex.com/">Git-Tf</a> is an open source command line tool&#160; that works cross platform and use the&#160;Java TFS SDK. This tool is useful for migration if you're not on a Windows environment. This tool is not maintained and has issues with migrating branches.&#160;<div><br></div><div>To see how to use this to migrate see&#160;<a href="https&#58;//chriskirby.net/blog/migrate-an-existing-project-from-tfs-to-github-with-changeset-history-intact">&quot;Migrate an existing project from TFS to Git with changeset history intact&quot; from Chris Kirby </a><br></div><p class="ssw15-rteElement-GreyBox"><strong>TIP - </strong> Use Git-Tf if you don't have a Windows environment<br></p><div><h3 class="ssw15-rteElement-H3">Git-Tfs ( Recommended)<br></h3></div><div><a href="https&#58;//github.com/git-tfs/git-tfs">Git-Tfs</a> is an open source command line tool that uses the .NET TFS SDK to interface between Git and TFVC. It has the following advantages over the other tools&#58;<br></div><div><ul><li>Actively maintained<br></li><li>Good support for branches<br></li><li>Author mapping<br></li><li>Migrates all history <br></li></ul><div>Follow the <a href="https&#58;//github.com/git-tfs/git-tfs/blob/master/doc/usecases/migrate_tfs_to_git.md">migration guide</a> to import from TFVC to Git and then&#160;proceed with <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d9e40f73-f7e8-4ff3-aedf-800df2941564">the after migration steps </a>.<br>To help you do a smoother migration, you can refer to this <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d754182b-a385-4d9e-9c99-c0f83204e6a4">tool </a>.&#160;<br></div></div><div><br></div>


