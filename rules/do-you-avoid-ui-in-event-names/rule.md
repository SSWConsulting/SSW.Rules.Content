---
type: rule
title: Do you avoid "UI" in event names?
uri: do-you-avoid-ui-in-event-names
created: 2018-04-30T21:07:59.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> No &quot;UI&quot; in event names, the event raiser should be unaware of the UI in MVVM and user controls<br>The handler of the event should then do something on the UI. <br> </span>

<p class="ssw15-rteElement-CodeArea">  private void RaiseUIUpdateBidButtonsRed()<br>&#123;<br>if (UIUpdateBidButtonsRed != null)<br>&#123;<br>UIUpdateBidButtonsRed();<br>&#125;<br>&#125;</p><dd class="ssw15-rteElement-FigureBad"> Bad Code&#58; Avoid &quot;UI&quot; in event names, an event is UI un-aware</dd><p>​​<br></p><p class="ssw15-rteElement-CodeArea"> private void RaiseSelectedLotUpdated()<br>&#123;<br>if (SelectedLotUpdated != null)<br>&#123;<br>SelectedLotUpdated();<br>&#125;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood"> Good Code&#58; We received an update on the currently selected item, change the UI correspondingly (or even better&#58; use MVVM and data binding)</dd><p>​<br></p>


