---
type: rule
title: Do you use more meaningful names than Hungarian short form?
uri: do-you-use-more-meaningful-names-than-hungarian-short-form
created: 2009-05-05T07:29:18.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> Hungarian notation is used in VB6. In .NET, there are over 35,000 classes, so&#160;we can't just call them with three letter short form. We would suggest the developer use the full class name as&#160; in example below. As a result, the code will be much easier to read and follow up. 
 </span>


  <dl class="badCode">
    <dt style="width&#58;92.04%;height&#58;206px;">
    <pre>                          //Bad Code<br><br>
                          DateTime dt = new DateTime.Now();
<br>
                          DataSet ds = new DataSet();
<br>
                          // It could be confused with Date time.
<br>
                          DataTable dt = ds.Tables[0];</pre>
    </dt>
    <dd>Bad code - Without meaningful name. </dd>
</dl>
<dl class="goodCode">
    <dt style="width&#58;92.33%;height&#58;170px;">
    <pre>                     //Good Code<br><br>
                     DateTime currentDateTime = new DateTime.Now();
<br>
                     DataSet employmentDataSet = new DataSet();
<br>
                     DataTable ContactDetailsDataTable = ds.Tables[0];</pre>
    </dt>
    <dd>Good code - With meaningful name. </dd>
</dl>
<p><a href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperDotNet/DotNetStandard_ObjectNaming.aspx">More information on naming convention</a>. </p>
<p>&#160;</p>
<table id="table30" class="clsSSWProductTable" cellspacing="2" summary="Code Auditor" cellpadding="2">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> to check for this rule</td>
        </tr>
    </tbody>
</table>



