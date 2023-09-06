---
type: rule
title: Do you use a helper extension method to raise events?
uri: use-a-helper-extension-method-to-raise-events
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-use-a-helper-extension-method-to-raise-events
created: 2018-04-30T21:21:26.000Z
archivedreason: null
guid: 30ea0a57-c66d-44f4-87b6-61ae5ee8972a
---
Enter Intro Text

<!--endintro-->

Instead of:

```csharp
private void RaiseUpdateOnExistingLotReceived() {
  if (ExistingLotUpdated != null) {
    ExistingLotUpdated();
  }
}
```

...use this event extension method:

```csharp
public static void Raise<t>(
  this EventHandler<t> @event,
  object sender, 
  T args
) where T : EventArgs {
  var temp = @event;
  
  if (temp != null) {
    temp(sender, args);
  }
}

public static void Raise(this Action @event) {
  var temp = @event;

  if (temp != null) {
    temp();
  }
}
```

That means that instead of calling:

```csharp
RaiseExistingLotUpdated();
```

...you can do:

```csharp
ExistingLotUpdated.Raise();
```

Less code = less code to maintain = less code to be blamed for ;)