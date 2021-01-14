---
type: rule
archivedreason: 
title: Do you use a helper extension method to raise events?
guid: 30ea0a57-c66d-44f4-87b6-61ae5ee8972a
uri: do-you-use-a-helper-extension-method-to-raise-events
created: 2018-04-30T21:21:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- use-a-helper-extension-method-to-raise-events

---

Enter Intro Text

<!--endintro-->

Instead of:



```
private void RaiseUpdateOnExistingLotReceived()
{
if (ExistingLotUpdated != null)
{
ExistingLotUpdated();
}
}
```



...use this event extension method:



```
public static void Raise<t>(this EventHandler<t> @event,
object sender, T args) where T : EventArgs
{
var temp = @event;
if (temp != null)
{
temp(sender, args);
}
}
public static void Raise(this Action @event)
{
var temp = @event;
if (temp != null)
{
temp();
}
}
```



That means that instead of calling:



```
RaiseExistingLotUpdated();
```



...you can do:



```
ExistingLotUpdated.Raise();
```



Less code = less code to maintain = less code to be blamed for ;)
