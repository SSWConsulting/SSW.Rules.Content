---
type: rule
title: Do you deploy "Controlled Lookup Data" ?
uri: do-you-deploy-controlled-lookup-data-
created: 2009-10-05T06:26:18.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Lookup data is data that you usually see in combo boxes. It may be a Customer Category, a Product Color or the Order Status. Usually this is defined by the user and the programmer does not care what or how many records they have. When the programmer relies on records being in the lookup table, it is called 'Controlled Lookup Data'. <br>
<br>
So whenever you have special data,&#160;which is referenced in code you need to tread carefully by&#58; 
 </span>


  <p style="margin&#58;0cm 0cm 0pt;">1) First understanding that although most of the time there is a clear separation between data and schema, there is an exception for Controlled Lookup Data. This is when data (aka Controlled Lookup Data) is tightly coupled to the&#160;application, meaning that you have an application that cannot function correctly without that data.</p>
<p style="margin&#58;0cm 0cm 0pt;">2) You need to deploy that 'Controlled Lookup Data'<br>
<br>
3) You then need to add a check for it so that it does not disappear. </p>
<p style="margin&#58;0cm 0cm 0pt;">Let's look at an example&#58;</p>
<dl class="image">
    <dt><img alt="" src="/PublishingImages/TimeProDropDown.png" /> </dt>
    <dd>Figure&#58; This combo looks innocent. However if it is &quot;Billable&quot; then the calendar goes yellow </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="/PublishingImages/TimeProCalendar.png" /> </dt>
    <dd>Figure&#58;&#160;Billable days are shown in yellow </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>if (drDay.NotBillableCount == 0 &amp;&amp; 
    drDay.BillableCount &gt; 0)
&#123;
    //Yellow Background
    cell.BackColor = Color.FromArgb(255, 255, 140);
    cell.BackColor2 = Color.FromArgb(255, 255, 140);
&#125;
else if (drDay.BillableCount &gt; 0)
&#123;
    cell.BackColor = Color.FromArgb(255, 255, 140);
    cell.BackColor2 = Color.LightGray;
&#125;
else
&#123;
    cell.BackColor = Color.LightGray;
    cell.BackColor2 = Color.LightGray;
&#125;
</pre>
    </font></dt>
    <dd>Figure&#58; I think we have &quot;Controlled Lookup Data&quot; here, because if the &quot;BillableCount&quot; is greater than 0, the color shown will be yellow </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>INSERT INTO dbo.[EmpTimeBillable] 
    ([CategoryID], [CategoryName], [DateCreated], 
    [DateUpdated], [EmpUpdated], [Note], [rowguid], 
    [Colour]) 
VALUES 
    ('ALL', '', '09/13/2009 00&#58;00&#58;00', 
    '09/13/2009 00&#58;00&#58;00', 
    'SSW-AdamCogan', 
    'Used for reports - 
     Excluded in Timesheets and Tasklist data entry', 
    '&#123;A9A009A9-4E19-4FD3-B86A-B9260067D0EF&#125;', 
    'White')
GO
INSERT INTO dbo.[EmpTimeBillable] 
    ([CategoryID], [CategoryName], [DateCreated], 
    [DateUpdated],[EmpUpdated], [Note], [rowguid], 
    [Colour]) 
VALUES 
    ('B', 'Billable', '07/01/2009 00&#58;00&#58;00', 
    '07/01/2009 00&#58;00&#58;00', 
    'SSW-AdamCogan', 
    'DON’T CHANGE - These are hard coded', 
    '&#123;F410C25D-1F1A-4340-B7A4-7A4AAE037708&#125;', 
    'Yellow')
GO
INSERT INTO dbo.[EmpTimeBillable] 
    ([CategoryID], [CategoryName], [DateCreated], 
    [DateUpdated], [EmpUpdated], [Note], [rowguid], 
    [Colour]) 
VALUES 
    ('BPP', 'Prepaid Billable', '02/28/2009 15&#58;30&#58;19', 
    '02/28/2009 00&#58;00&#58;00', 
    'SSW-AdamCogan', 
    'DON’T CHANGE - These are hard coded', 
    '&#123;608AA6FF-B3C5-47BE-AC9A-29553E89643D&#125;', 
    'LightYellow')
GO
INSERT INTO dbo.[EmpTimeBillable] 
    ([CategoryID], [CategoryName], [DateCreated], 
    [DateUpdated], [EmpUpdated], [Note], [rowguid], 
    [Colour]) 
VALUES 
    ('U', 'Unknown', '07/01/2009 00&#58;00&#58;00', 
    '07/01/2009 00&#58;00&#58;00', 
    'SSW-AdamCogan', 
    'DON’T CHANGE - These are hard coded', 
    '&#123;74937D60-D2B2-4A4D-96AD-7F5B1941B244&#125;', 
    'White')
GO
INSERT INTO dbo.[EmpTimeBillable] 
    ([CategoryID], [CategoryName], [DateCreated], 
    [DateUpdated], [EmpUpdated], [Note], [rowguid], 
    [Colour]) 
VALUES 
    ('W', 'W/Off', '07/01/2009 00&#58;00&#58;00', 
    '07/01/2009 00&#58;00&#58;00', 
    'SSW-AdamCogan', 
    'DON’T CHANGE - These are hard coded', 
    '&#123;D51513CE-8A1D-41E4-93C4-3E827FF7522B&#125;', 
    'LavenderBlue')
GO
</pre>
    </font></dt>
    <dd>Figure&#58; This data must be deployed, just like we deploy schema </dd>
</dl>
Now you need&#160;to add a&#160;procValidate, see <a href="/Pages/DoYouCheckYourLookupDataAkaReferenceDataIsStillThereWithProcValidate.aspx">Do you check your &quot;Controlled Lookup Data&quot; (aka Reference Data) is still there with procValidate?&#160;</a> 



