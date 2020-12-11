---
type: rule
archivedreason: 
title: Controls - Do you use Text Boxes for displaying data?
guid: ae3ac9f6-c2cf-44af-95ec-aa16c3538083
uri: controls---do-you-use-text-boxes-for-displaying-data
created: 2012-11-27T09:21:17.0000000Z
authors: []
related: []

---


<p>Use Label controls to display static text of the application. Eg. "Customer ID:"<br>Use Text Box controls to display data (results of calculations, information, records from a database, etc.).</p>
<br><excerpt class='endintro'></excerpt><br>
​<div>The reasons are:</div>
<ul><li>users know it is data, not a label of the application</li>
<li>users can copy and paste from the field</li></ul>
<div>PS: One reason web UI's are nice, is that the information is always selectable/copyable.</div>
<dl class="badImage"><dt><img alt="Long string cut off when you are using label" src="../../assets/BetterInterface_LabelCutOff.jpg" /></dt>
<dd>Figure: Bad Example - Not only is the data cut off when you are using label, but you can't copy and paste the value</dd></dl>
<dl class="goodImage"><dt><img alt="Using Textbox is better practice" src="../../assets/GoodTextbox.gif" /></dt>
<dd>Figure: Good Example - Using Textbox controls makes the data obvious to users</dd></dl>
<div>As you can see you'll barely know the difference, so start using Textboxes for displaying data, that's good practice.</div>
<h4>More Information</h4>
<div>When using TextBox controls in Windows Forms, set them up like this:</div>
<dl class="image"><dt><img alt="Using Textbox is better practice" src="../../assets/BorderStyle_1.gif" /></dt>
<dd>Figure: Having the 'BorderStyle' Property set to Fixed3D is the best choice visually</dd></dl>
<dl class="image"><dt><img alt="Using Textbox is better practice" src="../../assets/ReadOnly_1.gif" /></dt>
<dd>Figure: Make the text box Read-Only (users copying data is OK, changing is silly)</dd></dl>



