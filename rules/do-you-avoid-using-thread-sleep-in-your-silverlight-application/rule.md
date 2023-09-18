---
type: rule
archivedreason: Deprecating as Silverlight is no longer installable and has been deprecated for 10 years.
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
 If you want to delay something, you can use a [storyboard](http&#58;//msdn.microsoft.com/en-us/library/system.windows.media.animation.storyboard.aspx).   
<!--endintro-->



```cs
Thread.Sleep(5000); 

this.Dispatcher.BeginInvoke(new Action(() => 

                            { 

                         //Try to reconnect in the background 

                               Connect.Execute(null); 

                             })); 

Bad: Using Thread.Sleep() causes your Silverlight application to freeze 

 

  

Storyboard sb = new Storyboard() { Duration = TimeSpan.FromSeconds(5) }; 

  

sb.Completed += (ds, de) => this.Dispatcher.BeginInvoke(new Action(() => 

                                                                       { 

                                                                          //Try to reconnect in the background 

                                                                         Connect.Execute(null); 

                                                                       })); 

sb.Begin();
```




::: good
GOOD: Use a Storyboard with a duration of the delay and once the Storyboard is finished running  
:::
