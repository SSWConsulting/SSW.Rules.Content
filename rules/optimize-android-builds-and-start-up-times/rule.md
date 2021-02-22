---
type: rule
archivedreason: 
title: Do you optimise your Android builds and start-up times?
guid: fa142c74-97bb-4150-be0d-abb997ea9d30
uri: optimize-android-builds-and-start-up-times
created: 2020-10-08T23:04:23.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- do-you-optimise-your-android-builds-and-start-up-times

---


<p class="ssw15-rteElement-P">​Whereas iOS enforces AOT (ahead of time) compilation, Android supports (and uses by default) JIT (just in time) compilation, but AOT can be enabled on Android to improve performance.​​​</p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">Xamarin also provides several other options for optimizing Android builds and improving performance. Additionally, you can use Android's new bundle format (rather than apk) so that smaller builds can be targeted to individual hardware specifications.​<br></p><dl class="image"><dt><img src="android-startup.png" alt="android-startup.png" style="width:750px;" /></dt><dd>Figure: Using the d8 compiler and r8 code shrinker can improve your Android app performance, and enabling startup tracing can help you identify performance issues</dd></dl>

<p>For more information, see: <a href="https://devblogs.microsoft.com/xamarin/optimize-xamarin-android-builds/">https://devblogs.microsoft.com/xamarin/optimize-xamarin-android-builds/</a><br></p>


