---
type: rule
title: Do you always prefix SQL stored procedure names with the owner in ADO.NET code?
uri: do-you-always-prefix-sql-stored-procedure-names-with-the-owner-in-adonet-code
created: 2009-05-13T06:49:36.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <dl class="badCode">
    <dt style="width&#58;92.63%;height&#58;76px;">
    <pre>SqlCommand sqlcmd = new SqlCommand(); sqlcmd.CommandText = &quot;<span style="background-color&#58;#ff0000;">
                    proc_InsertCustomer</span>&quot; sqlcmd.CommandType
                    = CommandType.StoredProcedure; sqlcmd.Connection = sqlcon;</pre>
    </dt>
    <dd>Bad Example </dd>
</dl>
<dl class="goodCode">
    <dt style="width&#58;93.1%;height&#58;80px;">
    <pre>SqlCommand sqlcmd = new SqlCommand(); sqlcmd.CommandText = &quot;
                     <span style="background-color&#58;#00ff00;">dbo.proc_InsertCustomer</span>&quot;; sqlcmd.CommandType
                     = CommandType.StoredProcedure; sqlcmd.Connection = sqlcon;</pre>
    </dt>
    <dd>Good Example </dd>
</dl>
<table id="table4" class="clsSSWProductTable" cellspacing="2" summary="Code Auditor" cellpadding="2">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> to check for this rule.</td>
        </tr>
    </tbody>
</table>



