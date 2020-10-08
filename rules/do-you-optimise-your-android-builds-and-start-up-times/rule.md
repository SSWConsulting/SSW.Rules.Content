---
type: rule
archivedreason: 
title: Do you optimise your Android builds and start-up times?
guid: fa142c74-97bb-4150-be0d-abb997ea9d30
uri: do-you-optimise-your-android-builds-and-start-up-times
created: 2020-10-08T23:04:23.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 97
  title: Matt Goldman
related: []

---


<p class="ssw15-rteElement-P">​Whereas iOS enforces AOT (ahead of time) compilation, Android supports (and uses by default) JIT (just in time) compilation, but AOT can be enabled on Android to improve performance.​​​</p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">Xamarin also provides several other options for optimizing Android builds and improving performance. Additionally, you can use Android's new bundle format (rather than apk) so that smaller builds can be targeted to individual hardware specifications.​<br></p><dl class="image"><dt><img src="/PublishingImages/android-startup.png" alt="android-startup.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Using the d8 compiler and r8 code shrinker can improve your Android app performance, and enabling startup tracing can help you identify performance issues</dd></dl>

<p>For more information, see&#58;&#160;<a href="https&#58;//devblogs.microsoft.com/xamarin/optimize-xamarin-android-builds/">https&#58;//devblogs.microsoft.com/xamarin/optimize-xamarin-android-builds/</a><br></p>


