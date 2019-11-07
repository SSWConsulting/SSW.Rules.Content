---
type: rule
archivedreason: 
title: iOS - Do you know how to optimise your test and release deployments?
guid: 528b9ccf-cb3e-4cf4-880b-1906c0c6694d
uri: ios-do-you-know-how-to-optimise-your-test-and-release-deployments
created: 2019-11-05T00:01:25.0000000Z
authors:
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects: []

---


​A common approach is to submit your app to Testflight, wait for user feedback, then submit for App Store release. The problem with this approach is that your release cycle can be significantly impacted by Apple's review schedule.&#160;App Store and Testflight reviews can be very quick, but can also take up to 3&#160;weeks!<br><div><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p>A better process&#160;is to submit your build for&#160;Testflight and&#160;Release simultaneously.<br></p><h3 class="ssw15-rteElement-H3">​​Steps&#58;<br></h3><ol><li>Upload your build to App Store Connect.</li><li>When automated processing is completed (scanning of the assemblies&#160;usually takes less than an hour), you will&#160;receive an&#160;email confirmation, open Testflight and&#160;submit for approval.<br></li><li>Immediately, prepare your app for submission to the App Store (by completing the appropriate metadata, e.g. new features or fixes in this version).<br><strong>&#160; &#160; Important</strong>&#58; Set to Manual Release so that your app does not get automatically released untested.<br></li><li>If you are using external or public users, your build must be approved by Apple for testing.<br><strong>&#160; &#160;&#160;Note&#58;</strong>&#160;If you are using internal testers only (App Store Connect users), they can begin testing immediately.​<br></li><li>Once both your App Store and Testflight builds have been approved, get a Test Pass via the Test Please process - see&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=b9ec5dbc-7379-47ea-9cc2-59bd3769cd18">Rules to Successful Projects&#58; Do you conduct a &quot;test please&quot; internally and then with the client?​</a><br>​<br><strong>&#160; &#160; Tip for&#160;Mid-Sprint Releases</strong>&#58; If its an internal app, you can accelarate&#160;the Test Please process by asking someone&#160;with an iPhone&#160;to test straight away&#160;via Testflight.<br><strong>&#160; &#160; Tip for End of Sprint Releases&#58; </strong>Get the Testflight and Release submissions approved in preparation for your Sprint Review. You can then demo your release to the Product Owner and be&#160;ready to release your Product Increment after the Sprint Review.<br><br></li><li>You can now release your app as soon as you are ready.&#160;In App Store Connect click Release to make your latest build publicly available in the App Store.<br><br><img src="/SiteAssets/ios-do-you-know-how-to-optimise-your-test-and-release-deployments/bad-example-new.png" alt="bad-example-new.png" style="margin&#58;5px;width&#58;808px;" /><br><br></li></ol><dd class="ssw15-rteElement-FigureBad">​​Figure&#58; Bad Example - v1.7 is&#160;&quot;Waiting for Review&quot; in Testflight but only v1.6 is submitted to the App Store. This can introduce delays of 3 weeks.<br></dd><p class="ssw15-rteElement-P">​​​​<br></p><p class="ssw15-rteElement-P"><img src="/SiteAssets/ios-do-you-know-how-to-optimise-your-test-and-release-deployments/good-example-new.png" alt="good-example-new.png" style="margin&#58;5px;width&#58;808px;" /><br><br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good Example - v1.7 has been submitted to Testflight and&#160;App Store at the same time - also &quot;Waiting for Review&quot;, but your&#160;build will be ready to release&#160;as soon as testing has passed<br><br></dd><p class="ssw15-rteElement-P"><br></p>


