---
type: rule
archivedreason: 
title: Do you use a helper extension method to raise events?
guid: 30ea0a57-c66d-44f4-87b6-61ae5ee8972a
uri: use-a-helper-extension-method-to-raise-events
created: 2018-04-30T21:21:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-a-helper-extension-method-to-raise-events

---


Enter Intro Text<br>
<br><excerpt class='endintro'></excerpt><br>
<p>Instead of&#58;</p><p class="ssw15-rteElement-CodeArea"> private void RaiseUpdateOnExistingLotReceived()<br>&#123;<br>if (ExistingLotUpdated != null)<br>&#123;<br>ExistingLotUpdated();<br>&#125;<br>&#125;<span style="background-color&#58;#ffffff;font-size&#58;13px;">​</span></p><p>...use this event extension method&#58;</p><p class="ssw15-rteElement-CodeArea"> public static void Raise&lt;t&gt;(this EventHandler&lt;t&gt; @event,<br>object sender, T args) where T &#58; EventArgs<br>&#123;<br>var temp = @event;<br>if (temp != null)<br>&#123;<br>temp(sender, args);<br>&#125;<br>&#125;<br>public static void Raise(this Action @event)<br>&#123;<br>var temp = @event;<br>if (temp != null)<br>&#123;<br>temp();<br>&#125;<br>&#125;<br></p><p>That means that instead of calling&#58;<br></p><p class="ssw15-rteElement-CodeArea">RaiseExistingLotUpdated(); <br></p><p>...you can do&#58;<br></p><p class="ssw15-rteElement-CodeArea">ExistingLotUpdated.Raise();</p><p>Less code = less code to maintain = less code to be blamed for ;)​<br></p>


