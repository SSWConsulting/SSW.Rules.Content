---
type: rule
title: Controls - Do you include '-All-' option in your ComboBoxes?
uri: controls---do-you-include--all--option-in-your-comboboxes
created: 2012-11-27T08:38:56.0000000Z
authors: []

---



<span class='intro'> <div>ComboBoxes are often used for filtering data. It is best to have an '-All-' option to give your user chances to select all data.</div><div><br></div>
<div>It is important to understand the idea of <strong>visual text</strong>. In a list you could see either&#58;</div>
<ul><li>-None- or<br></li>
<li>No activity assigned</li></ul>
<div>They both have the same meaning, but the first one is immediately visible whereas the second one must be read.</div> </span>

<div><br></div>If the ID column in your database is a string data type, it&#160;​is useful to add a constraint to limit the types of characters that it&#160;can contain. Adding a constraint can make it simpler to build your front-end, as you won't need to worry about encoding or escaping to handle special characters.<div><br></div><div>In SQL Server, you can add a check constraint that limits your column to alphanumeric characters, a&#160;hyphen, or&#160;underscore&#160;using the following T-SQL&#58;<div><div><div><p class="ssw15-rteElement-CodeArea">ALTER TABLE [TableName]&#160;ADD CONSTRAINT CK_String_Identifier​<br>&#160; &#160; CHECK&#160;<span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#eeeeee;">([StringIdColumn]&#160;NOT LIKE'%[^a-</span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#eeeeee;">zA-Z0-9_\-]%')​</span></p><div><br></div><div><br><div><img alt="ComboBox without All" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/Combo-ALL-1.jpg" /><div><dl class="badImage">
<dd>Figure&#58; Bad Example - No '-All-' option so the user cannot select all data</dd></dl>
<dl class="goodImage"><dt><img alt="ComboBox without All" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/Combo-ALL-2.jpg" /></dt>
<dd>Figure&#58; Good Example - Having an '-All-' option gives a user a chance to select all data</dd></dl>
<div>Also, keep it simple!</div>
<dl class="badImage"><dt><img alt="All Stores" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SelectAllBad.jpg" /></dt>
<dd>Figure&#58; Bad Example - '-All Stores-' isn't needed</dd></dl>
<dl class="goodImage"><dt><img alt="All" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SelectAllGood.jpg" /></dt>
<dd>Figure&#58; Good Example - Keep it as a simple '-All-'</dd></dl>
<dl class="goodImage"><dt><img alt="All" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SelectAllVGood.png" /></dt>
<dd>Figure&#58; Good Example - Keeping it simple makes it easy to spot (that there is no filter) when you have multiple fields.</dd></dl>
<div>Read our rule on <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterBusinessIntelligence.aspx#AllDimensionsTag">Always make sure the dimensions All Captions = All</a>.</div>
</div></div></div></div></div></div></div>


