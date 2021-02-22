---
type: rule
archivedreason: 
title: Do you swarm to fix the build?
guid: f51b4c00-7b7d-4b6a-a35e-096cdf1c9e39
uri: do-you-swarm-to-fix-the-build
created: 2015-11-03T08:46:16.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related: []
redirects: []

---


If you or someone on your team has broken the build, the whole team should swarm to fix the problem immediately.
<br><excerpt class='endintro'></excerpt><br>
<p>​</p><p></p><p>It is PERFECTLY ok to have the CI build go red, that is what is there for, but when the build goes red the team should go immediately into corrective action mode and make sure the build goes green again.</p><p>Two things should be done:</p><ol><li><span style="line-height:1.6;">Get it Green </span><br></li><li><span style="line-height:1.6;">Find out WHY it went green locally but red on build server. This may indicate something is brittle in the application structure, and that is the </span><span style="line-height:1.6;">underlying cause – and should of course also be fixed.</span><br></li></ol><div><span style="line-height:20.8px;"><br></span></div><div><span style="line-height:20.8px;"><img src="broken builds.png" alt="broken builds.png" style="margin:5px;width:808px;" /><br></span></div><dd class="ssw15-rteElement-FigureBad">Bad Example: Too many broken builds in a row.</dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-P">​​<img src="good builds.png" alt="good builds.png" style="margin:5px;width:808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Good Example: Broken build was fixed immediately.</dd><p class="ssw15-rteElement-P">​<br></p>


