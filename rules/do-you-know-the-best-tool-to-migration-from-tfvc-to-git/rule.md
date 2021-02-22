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


Git has become the defacto standard for version control systems. It's distributed and decentralized and promotes working disconnected as default. It also takes away the pain of branching and merging and has a built in code review system with pull requests. Everybody should be using Git, and if you're not, you should be migrating the Git using one of the below tools.<br><div><ul><li>VisualStudio.com - Import Repository<br></li><li>Git-Tf<br></li><li>Git-Tfs (recommended)<br></li></ul></div>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">VisualStudio.com - Import Repository<br></h3><p>VisualStudio.com gives you the ability to import from a TFVC repository into a new Git repository. <br></p><p><img src="03_29_08.png" alt="03_29_08.png" style="margin:5px;" /><br></p><dd class="ssw15-rteElement-FigureBad">Bad Example - Built in tool has several limitations<br></dd><div>If you don't care about source control history, then this inbuilt tool is the easiest to use. It has the limitations of:</div><div><ul><li>180 days of history<br></li><li>No branches<br></li></ul><p class="ssw15-rteElement-GreyBox"><strong>TIP - </strong>Use this if you don't care about source control history<br></p> </div><h3 class="ssw15-rteElement-H3">Git -Tf <br></h3><a href="https://gittf.codeplex.com/">Git-Tf</a> is an open source command line tool  that works cross platform and use the Java TFS SDK. This tool is useful for migration if you're not on a Windows environment. This tool is not maintained and has issues with migrating branches. <div><br></div><div>To see how to use this to migrate see <a href="https://chriskirby.net/blog/migrate-an-existing-project-from-tfs-to-github-with-changeset-history-intact">"Migrate an existing project from TFS to Git with changeset history intact" from Chris Kirby </a><br></div><p class="ssw15-rteElement-GreyBox"><strong>TIP - </strong> Use Git-Tf if you don't have a Windows environment<br></p><div><h3 class="ssw15-rteElement-H3">Git-Tfs ( Recommended)<br></h3></div><div><a href="https://github.com/git-tfs/git-tfs">Git-Tfs</a> is an open source command line tool that uses the .NET TFS SDK to interface between Git and TFVC. It has the following advantages over the other tools:<br></div><div><ul><li>Actively maintained<br></li><li>Good support for branches<br></li><li>Author mapping<br></li><li>Migrates all history <br></li></ul><div>Follow the <a href="https://github.com/git-tfs/git-tfs/blob/master/doc/usecases/migrate_tfs_to_git.md">migration guide</a> to import from TFVC to Git and then proceed with <a href=/do-you-know-what-to-do-after-migrating-from-tfvc-to-git>the after migration steps </a>.<br>To help you do a smoother migration, you can refer to this <a href=/tfs-master-do-you-have-a-report-to-see-who-has-not-checked-in>tool </a>. <br></div></div><div><br></div>


