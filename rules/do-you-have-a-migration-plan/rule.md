---
type: rule
title: Do you have a migration plan
uri: do-you-have-a-migration-plan
created: 2016-05-20T02:01:48.0000000Z
authors:
- id: 15
  title: Mark Liu
- id: 9
  title: William Yin

---



<span class='intro'> <span style="line-height&#58;20.8px;">​At a high level, the plan is&#58;</span> </span>

<p></p><p></p><ul><li><span style="line-height&#58;1.6;"><strong>Install </strong></span><span style="line-height&#58;1.6;"><strong>SharePoint&#160;​</strong></span><br></li></ul><ol><li><span style="line-height&#58;1.6;background-color&#58;initial;">I</span><span style="line-height&#58;1.6;background-color&#58;initial;">nstall with topology of your choice in SharePoint 2016 (or use <a href="https&#58;//autospinstaller.codeplex.com/">AutoSPInstaller</a>)</span><br></li><li><span style="line-height&#58;1.6;background-color&#58;initial;">Configure Application services</span><br></li></ol><p></p><p></p><blockquote style="margin&#58;0px 0px 0px 40px;border&#58;none;padding&#58;0px;"><ul><li>Run the wizard (or use script. the community script wasn't ready when Thiago and I was migrating intranet)​</li><li><span style="line-height&#58;1.5em;">Configure user profile and its permission configuration (see <a href="https&#58;//technet.microsoft.com/en-us/library/ee721052.aspx">msdn</a>​)​</span></li></ul></blockquote><div><div><ul><li><span style="line-height&#58;1.5em;"><strong>Test Migration</strong></span><br></li></ul></div><ol><li><span style="line-height&#58;1.6;">Install required WSP packages in 2016</span><br></li><li><span style="line-height&#58;1.6;">Migrate content database from old to new</span><br></li><li><span style="line-height&#58;1.6;">(</span><span style="line-height&#58;1.6;">Optional) Migrate services database&#160;(depends on which service applications do you use)</span><br></li></ol><ul><li><span style="line-height&#58;1.6;"><strong>Post migration setup</strong></span><br></li></ul><ol><li><span style="line-height&#58;1.6;">Configure search (TODO&#58; create a rule)</span><br></li><li><span style="line-height&#58;1.6;">Configure metadata (optional)</span><br></li></ol><ul><li><span style="line-height&#58;1.6;"><strong>Test test </strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong>tes</strong></span><span style="line-height&#58;1.6;"><strong>t</strong></span><br></li><li><span style="line-height&#58;1.6;"><strong>Go-live migration</strong></span><br></li></ul><ol><li><span style="line-height&#58;1.6;">Put old SharePoint into read-only</span><br></li><li><span style="line-height&#58;1.6;">Refresh content &amp; service database from SP 2013 to 2016</span><br></li><li><span style="line-height&#58;1.6;">Update DNS</span><br></li><li><span style="line-height&#58;1.5em;">Decomission old SharePoint server and</span><span style="line-height&#58;1.5em;"> database (after 2 weeks when you're confident with the new environment)</span></li></ol><br><p><br></p></div>


