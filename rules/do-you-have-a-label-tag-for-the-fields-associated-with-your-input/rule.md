---
type: rule
archivedreason: 
title: Do you have a label tag for the fields associated with your input?
guid: 8fb2c2cb-b780-4ac3-bd5a-2a7b58d15459
uri: do-you-have-a-label-tag-for-the-fields-associated-with-your-input
created: 2014-12-16T18:47:45.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>
                    When adding input boxes to collect data, please always have a &lt;label&gt; tag
                    associated with your &lt;input&gt; tag to link the labels with their respective
                    edit controls. This improves accessibility and gives nice focusing stuff (when you
                    click the label).</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="code"><dt><pre>&lt;p&gt;
    &lt;label for=&quot;EmailAddress&quot;&gt;Email&#160;Address&lt;/label&gt;
    &lt;input id=&quot;EmailAddress&quot;&#160;type=&quot;text&quot;/&gt;
&lt;/p&gt;</pre></dt></dl><p>
                    <b>Tip&#58; </b>To do this in ASP.NET use the AssociatedControlID parameter on your &lt;asp&#58;Label&#160;/&gt;
                    controls.</p><dl class="code"><dt><pre>&lt;p&gt;
    &lt;asp&#58;Label ID=&quot;EmailLabel&quot; runat=&quot;server&quot; Text=&quot;Email&#160;Address&quot; AssociatedControlID=&quot;EmailAddress&quot;/&gt;
    &lt;asp&#58;TextBox ID=&quot;EmailAddress&quot; runat=&quot;server&quot;/&gt;
&lt;/p&gt;</pre></dt></dl>


