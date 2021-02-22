---
type: rule
archivedreason: "Requested by Brendan on \n\nRE: TFS Deployment Rule - Does anyone follow this rule"
title: Do your developers deploy manually?
guid: ae32d7b5-32e1-402d-97a3-29a57546fcdb
uri: do-your-developers-deploy-manually
created: 2012-01-30T18:42:41.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---


​We strongly believe that this process should all be automated and painless. Even the receptionist should be able to make a grammatical change on the website and be able to deploy it.<p>We use TFS gated check-ins to do the deployment for us. When a developer checks there changes into TFS they are prompted with a gated check-in screen.</p>
<img class="ms-rteCustom-ImageArea" alt="Build screen" src="deployment1.jpg" /><span class="ms-rteCustom-FigureNormal">Figure: "Build" screen</span><br><p>The developer clicks the "Build changes" button and waits for the build to complete. This process needs to take no longer than 2 minutes as it just makes cranky developers if this takes too long.<br>The code is put into a TFS shelf, compiled, had all the unit tests run against the code and then deployed to the internal webserver if successful.</p>
<p>Once this process has completed successfully, the developer will get presented with the ability to "reconcile" their local copy of the files as they have now been successfully checked-in to TFS.</p>
<img class="ms-rteCustom-ImageArea" alt="Build screen" src="deployment2.jpg" /><span class="ms-rteCustom-FigureNormal">Figure: Click on the "Reconcile" button to update your local files</span><br><p>If the developer does not have Build notifications on there local computer then this step can also be easily performed via the Build Explorer in Visual Studio.</p>
<img class="ms-rteCustom-ImageArea" alt="Build screen" src="deployment3.jpg" /><span class="ms-rteCustom-FigureNormal">Figure: Right click on your last successful build and choose "Reconcile Workspace"</span><br><p>The <a href="http://www.ssw.com.au/">www.ssw.com.au</a> website also queues a build process that deploys the changes to our Australian staging server. A developer can then use <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=580a6735-c102-48c2-bf22-91ff3cc9ead5">Octopus deploy​</a> to push it live to our Australian and US production sites.<br></p>
<p>The process that syncs to our external servers is very quick. Only the changes in TFS since the last deployment are sent. This typically takes under 10 seconds to complete.<br></p>
<p>​If the build fails then no changes would get pushed to staging and developers should <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=aea8bbdc-6efd-413a-b988-1c348dd77eb4">swarm to fix the build</a>.<br></p><p><img src="2017-04-11_10-13-08.png" alt="2017-04-11_10-13-08.png" style="margin:5px;width:808px;" /><br></p><dd class="ssw15-rteElement-FigureNormal">​​Figure: See the build failing and who requested it<br></dd><p><br><br></p>
<br><excerpt class='endintro'></excerpt><br>
<p><br></p>




