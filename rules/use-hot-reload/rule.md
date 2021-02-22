---
type: rule
archivedreason: 
title: Do you use Hot Reload?
guid: e8523286-b3e3-49a1-8a9c-c01b43bc7390
uri: use-hot-reload
created: 2020-10-07T23:15:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- do-you-use-hot-reload

---


Developing mobile apps presents unique challenges compared to web or desktop development. One of the problems is that when using MVVM or using dynamic data on a page, you need to run your app to populate the data and see what your UI will actually look like.<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>​<img src="hot-reload-bad.png" alt="hot-reload-bad.png" style="width:750px;" /></dt><dd>Figure: Bad Example - rebuilding your app every time to see small UI changes</dd></dl><p>This problem is partially solved by Design Time Data (see rule: <a href=/use-design-time-data>Do you use design time data?</a>), but this still doesn't show you how things change as you interact with them. </p><p>​To get around this problem use Hot Reload. This lets you make changes to your XAML while debugging your app - as soon as you save your UI will update, without having to stop and rebuild your app.</p><dl class="goodImage"><dt><img src="hot-reload-good.png" alt="hot-reload-good.png" style="width:750px;" /></dt><dd>Figure: Good example - hot reload enable screenshot Windows</dd></dl><p><b>Tip: </b>This works on the iOS simulator, the Android emulator, and physical iOS and Android devices.</p>


