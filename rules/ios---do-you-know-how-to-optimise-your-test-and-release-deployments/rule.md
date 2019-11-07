---
type: rule
title: iOS - Do you know how to optimise your test and release deployments?
uri: ios---do-you-know-how-to-optimise-your-test-and-release-deployments
created: 2019-11-05T00:01:25.0000000Z
authors:
- id: 97
  title: Matt Goldman

---



<span class='intro'> ​A common approach is to submit your app to Testflight, wait for user feedback, then submit for App Store release. The problem with this approach is that your release cycle can be significantly impacted by Apple's review schedule.&#160;App Store and Testflight reviews can be very quick, but can also take up to three weeks under some circumstances.<br><div><br></div> </span>

<p>A better process&#160;is to submit your build for&#160;Testflight and&#160;Release simultaneously.<br></p><h3 class="ssw15-rteElement-H3">​​Steps&#58;<br></h3><ol><li>Upload your build to App Store Connect.</li><li>When automated processing is completed (usually less than an hour), submit for approval to test in Testflight.</li><li>Immediately, prepare your app for submission to the App Store.&#160;<strong>Important</strong>&#58; set to Manual Release so that your app does not get automatically released untested.<br></li><li>If you are using internal testers only (App Store Connect users), they can begin testing immediately.</li><li>If you are using external or public users, your build must be approved by Apple for testing.</li><li>Once both your App Store and Testflight builds have been approved, get a test pass (if its an internal app, walk up to a stakeholder in your office who has an iPhone and get them to test via Testflight).<br></li><li>Immediately upon receiving a test pass, in App Store Connect click Release.<br></li></ol><div><font color="#333333"><br></font></div><div><font color="#333333">BONUS&#58; Get the Testflight and Release submissions approved in preparation for your Sprint Review. You are then ready to release your latest version at the end of your sprint as a Product Increment.&#160;<br>​<br></font></div><div><font color="#333333"><br></font></div><img src="/SiteAssets/ios-do-you-know-how-to-optimise-your-test-and-release-deployments/Screen%20Shot%202019-11-05%20at%2011.11.06%20am.png" alt="" style="margin&#58;5px;" /><br><dd class="ssw15-rteElement-FigureBad">​​Figure&#58; Bad Example - you can see &quot;Waiting for Review&quot;-&#160;if you wait for&#160;Testflight to complete before submitting for release you can introduce delays<br></dd><p class="ssw15-rteElement-P">​​​​<br></p><p class="ssw15-rteElement-P"><img src="/SiteAssets/ios-do-you-know-how-to-optimise-your-test-and-release-deployments/Screen%20Shot%202019-11-05%20at%2011.14.13%20am.png" alt="Screen Shot 2019-11-05 at 11.14.13 am.png" style="margin&#58;5px;" /><br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good Example - App Store release submitted at the same time - also &quot;Waiting for Reivew&quot;, but your release build will be ready to go as soon as testing has passed<br><br><br></dd><p class="ssw15-rteElement-P"><br></p>


