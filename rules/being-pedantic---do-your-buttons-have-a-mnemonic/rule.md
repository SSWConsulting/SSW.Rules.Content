---
type: rule
archivedreason: 
title: Being Pedantic - Do your buttons have a mnemonic?
guid: 5efb94c3-e91f-4a8c-87ba-b1bc76edf533
uri: being-pedantic---do-your-buttons-have-a-mnemonic
created: 2012-11-27T09:25:36.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>A mnemonic for a button is the letter which has an underscore, and the user can press the button using Alt-&lt;char&gt;.</p>
<br><excerpt class='endintro'></excerpt><br>
​<dl class="badImage"><dt><img alt="Browse Button" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BadMem.gif" /></dt>
<dd>Figure&#58; Bad Example - All buttons without Mnemonic</dd></dl>
<dl class="goodImage"><dt><img alt="Browse Button" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/GoodMem.gif" /></dt>
<dd>Figure&#58; Good Example - All buttons with Mnemonic - user can easily choose which button they want without a click</dd></dl>
<div>In Windows Applications, it is quite easy to assign a mnemonic to a button with the &quot;&amp;&quot; character.</div>
<div>So for the case above, the text would be&#58;</div>
<dl class="code"><dt><pre>btnAbout.Text = &quot;&amp;About&quot;</pre></dt></dl>
<div>Tip&#58; In Windows XP the mnemonic display effects can be hidden by Default and then shown every time the user presses the Alt key.</div>



