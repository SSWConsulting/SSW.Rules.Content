---
type: rule
archivedreason: 
title: Do you use Hot Reload?
guid: e8523286-b3e3-49a1-8a9c-c01b43bc7390
uri: do-you-use-hot-reload
created: 2020-10-07T23:15:56.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 97
  title: Matt Goldman
related: []

---

Developing mobile apps presents unique challenges compared to web or desktop development. One of the problems is that when using MVVM or using dynamic data on a page, you need to run your app to populate the data and see what your UI will actually look like.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="hot-reload-bad.png" alt="hot-reload-bad.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Bad Example - rebuilding your app every time to see small UI changes</dd></dl>
This problem is partially solved by Design Time Data (see rule: [Do you use design time data?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=bc86f3f0-e79d-44a6-bf7c-0196afd45235)), but this still doesn't show you how things change as you interact with them.

To get around this problem use Hot Reload. This lets you make changes to your XAML while debugging your app - as soon as you save your UI will update, without having to stop and rebuild your app.
<dl class="goodImage">&lt;dt&gt;<img src="hot-reload-good.png" alt="hot-reload-good.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Good example - hot reload enable screenshot Windows</dd></dl>
**Tip:** This works on the iOS simulator, the Android emulator, and physical iOS and Android devices.
