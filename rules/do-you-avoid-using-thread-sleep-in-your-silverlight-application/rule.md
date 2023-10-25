---
type: rule
archivedreason: Deprecated - Silverlight is no longer installable and has been deprecated for 10 years.
title: Do you avoid using Thread.Sleep in your Silverlight application?
guid: 5ed4ab0e-4bac-4eba-ac0e-fc087efcd865
uri: do-you-avoid-using-thread-sleep-in-your-silverlight-application
created: 2011-05-20T07:34:58.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Calling Thread.Sleep on your Silverlight application causes the UI thread to sleep. That means the application is not responsive.

If you want to delay something, you can use a [storyboard](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.animation.storyboard?view=windowsdesktop-7.0&redirectedfrom=MSDN).   
 
<!--endintro-->

```cs
Thread.Sleep(5000); 

this.Dispatcher.BeginInvoke(new Action(() => 
  { 
    // Try to reconnect in the background 
    Connect.Execute(null); 
  }));
```

::: bad  
Code: Bad example - Using Thread.Sleep() causes your Silverlight application to freeze 
:::
  
```cs
Storyboard sb = new Storyboard() { Duration = TimeSpan.FromSeconds(5) }; 
sb.Completed += (ds, de) => this.Dispatcher.BeginInvoke(new Action(() => 
  {
    // Try to reconnect in the background 
    Connect.Execute(null);
  }));
sb.Begin();
```

::: good  
Code: Good example - Use a Storyboard with a duration of the delay and once the Storyboard is finished running  
:::
