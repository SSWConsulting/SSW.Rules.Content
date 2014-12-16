---
type: rule
archivedreason: 
title: Do you have a label tag for the fields associated with your input?
guid: 8fb2c2cb-b780-4ac3-bd5a-2a7b58d15459
uri: do-you-have-a-label-tag-for-the-fields-associated-with-your-input
created: 2014-12-16T18:47:45.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


<p>
                    When adding input boxes to collect data, please always have a {ltHTMLChar}label{gtHTMLChar} tag
                    associated with your {ltHTMLChar}input{gtHTMLChar} tag to link the labels with their respective
                    edit controls. This improves accessibility and gives nice focusing stuff (when you
                    click the label).</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="code"><dt><pre>{ltHTMLChar}p{gtHTMLChar}
    {ltHTMLChar}label for=&quot;EmailAddress&quot;{gtHTMLChar}Email&#160;Address{ltHTMLChar}/label{gtHTMLChar}
    {ltHTMLChar}input id=&quot;EmailAddress&quot;&#160;type=&quot;text&quot;/{gtHTMLChar}
{ltHTMLChar}/p{gtHTMLChar}</pre></dt></dl><p>
                    <b>Tip&#58; </b>To do this in ASP.NET use the AssociatedControlID parameter on your {ltHTMLChar}asp&#58;Label&#160;/{gtHTMLChar}
                    controls.</p><dl class="code"><dt><pre>{ltHTMLChar}p{gtHTMLChar}
    {ltHTMLChar}asp&#58;Label ID=&quot;EmailLabel&quot; runat=&quot;server&quot; Text=&quot;Email&#160;Address&quot; AssociatedControlID=&quot;EmailAddress&quot;/{gtHTMLChar}
    {ltHTMLChar}asp&#58;TextBox ID=&quot;EmailAddress&quot; runat=&quot;server&quot;/{gtHTMLChar}
{ltHTMLChar}/p{gtHTMLChar}</pre></dt></dl>


