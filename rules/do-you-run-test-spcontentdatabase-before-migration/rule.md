---
type: rule
title: Do you run Test-SPContentDatabase before migration
uri: do-you-run-test-spcontentdatabase-before-migration
created: 2016-05-19T08:05:06.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> <p><span style="line-height&#58;20.8px;">&#160;<strong>​​Assumpation&#58;</strong></span></p><ol><li><span style="line-height&#58;20.8px;">You have already installed the customized wsp package you know.</span><br></li><li><span style="line-height&#58;20.8px;">You have restored the content database to SQL server</span><br></li><li><span style="line-height&#58;20.8px;">You haven't attach the content database yet.</span><br></li></ol><p><span style="line-height&#58;20.8px;"><span style="line-height&#58;20.8px;">It&#160;</span><span style="line-height&#58;20.8px;">is strongly recommend to run&#160;</span><span style="line-height&#58;20.8px;">a pre-migration check on the&#160;content&#160;</span><span style="line-height&#58;20.8px;">database</span><span style="line-height&#58;20.8px;">&#160;before attaching it to trigger the migration process</span><span style="line-height&#58;20.8px;">.</span><br></span></p> </span>

<div><span style="line-height&#58;20.8px;"><strong>Steps&#58;</strong></span></div><ol><li><span style="line-height&#58;1.6;">​Run&#160;SharePoint Pow</span><span style="line-height&#58;1.6;">erShell Console as&#160;admini​strator</span><br></li><li><span style="line-height&#58;1.6;">​Run the command below</span><span style="line-height&#58;1.6;">​​</span><span style="line-height&#58;1.6;">​​</span><div><p class="ssw15-rteElement-CodeArea" style="width&#58;770.031px;">​​​​<span></span><strong>Test-SPContentDatabase</strong> <strong>-</strong><strong>name </strong>WSS_Content_DB <strong>-</strong><strong>webapplication </strong>http&#58;//sitename​<span></span></p></div></li><li><span style="line-height&#58;1.6;">Check the output log, ensure there isn't any errors.</span></li></ol>


