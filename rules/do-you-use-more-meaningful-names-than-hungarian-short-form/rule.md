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



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


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
<table cellspacing="2" cellpadding="2" summary="Code Auditor" class="clsSSWProductTable" id="table30">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> to check for this rule</td>
        </tr>
    </tbody>
</table>



