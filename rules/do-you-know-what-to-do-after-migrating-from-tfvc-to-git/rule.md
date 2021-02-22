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


​After you <a href="/Pages/Do-you-know-the-best-tool-to-migration-from-TFVC-to-Git.aspx">use the right tool to migrate from TFVC to Git</a>, there's a few more things you need to do to clean things up for a new user joining the project. By default, if there is a TFVC repository, that will become the default in the UI.<br><div><br></div><div>Unfortunately, you can't kill the TFVC repository and make Git the default one, so there's a few steps you need to follow.<br></div><div><br>​<br><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p>​<img src="2017-04-05_10-02-58.png" alt="2017-04-05_10-02-58.png" style="margin:5px;" /></p><dd class="ssw15-rteElement-FigureBad">​Figure: Bad Example - Can't delete the now deprecated​ TFVC repository​​<br></dd><h3 class="ssw15-rteElement-H3">Delete files from TFVC<br></h3><p>Go into the repository, delete any existing files. Add a new document saying "_Migrated_to_Git.md". This will stop people from getting the wrong code.<br></p><p><img src="2017-04-05_10-24-52.png" alt="2017-04-05_10-24-52.png" style="margin:5px;width:808px;" /><br></p><dd class="ssw15-rteElement-FigureNormal">​​​​Figure: Clean up TFVC so developers can't accidentally get the wrong source code<br></dd><dd class="ssw15-rteElement-FigureNormal"><br></dd><p class="ssw15-rteElement-InfoBox"><strong>Note</strong>: All the source code is still there, it's just flagged as being deleted.<br></p><h3 class="ssw15-rteElement-H3">Lock down TFVC<br></h3><p>In the TFVC repository, click Security<br></p><p>​<img src="2017-04-05_10-43-51.png" alt="2017-04-05_10-43-51.png" style="margin:5px;" /></p><dd class="ssw15-rteElement-FigureNormal">Figure: Con​​figure the security of the TFVC repository<br></dd><p class="ssw15-rteElement-P">​​Then deny check-ins to <strong>Contributors</strong>, P<strong>roject Administrators</strong> and <strong>Project Collection Administrators</strong>. This should stop anyone from committing new code to the repository.<br></p><h3 class="ssw15-rteElement-H3">Update the Dashboard<br></h3><p>​Next step is to update the dashboard to let new developers know.<br></p><p class="ssw15-rteElement-P"><img src="2017-04-05_10-30-43.png" alt="2017-04-05_10-30-43.png" style="margin:5px;width:808px;" />​​<br></p><dd class="ssw15-rteElement-FigureGood">​​Figure: Good example - Let new users know that the source control is now on Git<br></dd><p>​​<br></p><h3 class="ssw15-rteElement-H3">​Suggestions for the VSTS team<br></h3><ol><li>​​Give us the ability to hide a repository<br></li><li>Give us the ability to set a repository as the default for all users<br></li><li>Give us the ability to delete a TFVC repository<br></li></ol><br><div>Having any of these suggestions will avoid the confusion on this screen<br></div><div><img src="2017-04-05_10-06-12.png" alt="2017-04-05_10-06-12.png" style="margin:5px;" /><br></div><dd class="ssw15-rteElement-FigureBad">​​Figure: Bad Exmaple - This is confusing for a new dev<br></dd><div><br></div>


