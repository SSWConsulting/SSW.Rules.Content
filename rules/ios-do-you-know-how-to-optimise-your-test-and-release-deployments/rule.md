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

A common approach is to submit your app to Testflight, wait for user feedback, then submit for App Store release. The problem with this approach is that your release cycle can be significantly impacted by Apple's review schedule. App Store and Testflight reviews can be very quick, but can also take up to 3 weeks!




<!--endintro-->

A better process is to submit your build for Testflight and Release simultaneously.

### Steps:


1. Upload your build to App Store Connect.
2. When automated processing is completed (scanning of the assemblies usually takes less than an hour), you will receive an email confirmation, open Testflight and submit for approval.
3. Immediately, prepare your app for submission to the App Store (by completing the appropriate metadata, e.g. new features or fixes in this version).
 **Important** : Set to Manual Release so that your app does not get automatically released untested.
4. If you are using external or public users, your build must be approved by Apple for testing.
 **Note:** If you are using internal testers only (App Store Connect users), they can begin testing immediately.
5. Once both your App Store and Testflight builds have been approved, get a Test Pass via the Test Please process - see [Rules to Successful Projects: Do you conduct a "test please" internally and then with the client?](/do-you-conduct-a-test-please-internally-and-then-with-the-client)

 **Tip for Mid-Sprint Releases** : If its an internal app, you can accelarate the Test Please process by asking someone with an iPhone to test straight away via Testflight.
 **Tip for End of Sprint Releases:** Get the Testflight and Release submissions approved in preparation for your Sprint Review. You can then demo your release to the Product Owner and be ready to release your Product Increment after the Sprint Review.
6. You can now release your app as soon as you are ready. In App Store Connect click Release to make your latest build publicly available in the App Store.

![](bad-example-new.png)



::: bad
Figure: Bad Example - v1.7 is "Waiting for Review" in Testflight but only v1.6 is submitted to the App Store. This can introduce delays of 3 weeks.

:::



![](good-example-new.png)


::: good
Figure: Good Example - v1.7 has been submitted to Testflight and App Store at the same time - also "Waiting for Review", but your build will be ready to release as soon as testing has passed


:::
