---
type: rule
archivedreason: 
title: Do you avoid "UI" in event names?
guid: 8ed33cf7-5f1c-460c-84d9-609d121649a0
uri: do-you-avoid-ui-in-event-names
created: 2018-04-30T21:07:59.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- avoid-ui-in-event-names

---

No "UI" in event names, the event raiser should be unaware of the UI in MVVM and user controls
The handler of the event should then do something on the UI. 

<!--endintro-->



```
private void RaiseUIUpdateBidButtonsRed()
{
if (UIUpdateBidButtonsRed != null)
{
UIUpdateBidButtonsRed();
}
}
```



::: bad
Bad Code: Avoid "UI" in event names, an event is UI un-aware  
:::





```
private void RaiseSelectedLotUpdated()
{
if (SelectedLotUpdated != null)
{
SelectedLotUpdated();
}
}
```



::: good
Good Code: We received an update on the currently selected item, change the UI correspondingly (or even better: use MVVM and data binding)  
:::
