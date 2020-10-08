---
type: rule
archivedreason: 
title: Do you use know how to consistently style your app?
guid: 15901500-e40b-41c1-991d-59c70c892b4c
uri: do-you-use-know-how-to-consistently-style-your-app
created: 2020-10-08T22:50:48.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 97
  title: Matt Goldman
related: []

---


Branding is important in any product, and especially a mobile app. Xamarin offers several ways to define and ensure consistent styling throughout your app&#58;<br><br>
<br><excerpt class='endintro'></excerpt><br>
<p></p><ul><li>​Resource Dictionaries</li><li>CSS</li><li>Visual</li></ul><dl class="badImage"><dt><img src="/PublishingImages/xamarin-style-bad.png" alt="xamarin-style-bad.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Bad Example - same styling defined and repeated multiple times​<br></dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/xamarin-style-good.png" alt="xamarin-style-good.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Good Example - Styles defined once in resource dictionary and applied to controls</dd></dl><p>Resource Dictionaries and CSS provide similar capabilities, but Resource Dictionaries are the best way to style your Xamarin applications. CSS in Xamarin is not full, web-standards compliant CSS, but rather an alternative way to write Xamarin styles than Resource Dictionaries. CSS in Xamarin does not currently support the full range of properties available, but it may be more comfortable for those familiar with web development.</p><p>Visual offers a much more granular level control over the look and feel of your application. However, this increase in granularity comes with a proportionally increased level of complexity. Rather than providing a style, you need to define a custom renderer for every control you want to define the look of.</p><p>Visual is suitable for large teams with a design heavy focus, where branding is of paramount importance. The advantage of Visual is that you can specify it at individual control level, at page level, or at whole of app-level to ensure your entire app is consistent.
</p>


