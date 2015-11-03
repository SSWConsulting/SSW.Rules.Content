---
type: rule
title: Do you swarm to fix the build?
uri: do-you-swarm-to-fix-the-build
created: 2015-11-03T08:46:16.0000000Z
authors:
- id: 37
  title: Ben Cull

---



<span class='intro'> If you or someone on your team has broken the build, the whole team should swarm to fix the problem immediately. </span>

<p>​</p><p></p><p>It is PERFECTLY ok to have the CI build go red, that is what is there for, but when the build goes red&#160;the team should go immediately into corrective action mode&#160;and make sure the build goes green again.</p><p>Two things should be done&#58;</p><ol><li><span style="line-height&#58;1.6;">Get it Green&#160;</span><br></li><li><span style="line-height&#58;1.6;">Find out WHY it went&#160;green locally but&#160;red on build server.&#160;This may indicate something is brittle in the application structure, and that is the </span><span style="line-height&#58;1.6;">underlying cause – and should of course also be fixed.</span><br></li></ol><div><span style="line-height&#58;20.8px;"><br></span></div><div><span style="line-height&#58;20.8px;"><img src="/PublishingImages/broken%20builds.png" alt="broken builds.png" style="margin&#58;5px;width&#58;808px;" /><br></span></div><dd class="ssw15-rteElement-FigureBad">Bad Example&#58; Too many broken builds in a row.</dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-P">​​<img src="/PublishingImages/good%20builds.png" alt="good builds.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; Broken build was fixed immediately.</dd><p class="ssw15-rteElement-P">​<br></p>


