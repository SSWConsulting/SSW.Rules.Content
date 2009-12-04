---
type: rule
title: Do you hard code your ConnectionString?
uri: do-you-hard-code-your-connectionstring
created: 2009-04-29T05:36:44.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <pre class="brush&#58;c-sharp">connection.ConnectionString = &quot;
Provider=SQLOLEDB;
Data Source=server_name_or_address; Initial Catalog=database_name;
User ID=username; Password=password; &quot;;

   connection.Open();
</pre>
<span class="ms-rteCustom-FigureBad">Bad code - use the lengthy connection string.</span>
<pre class="brush&#58;c-sharp">connection.ConnectionString = ConfigurationManager.Items[&quot;ConnectionString&quot;];

 connection.Open();
</pre>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Code - Use ConfigurationManager to handle the connection string.</span>
<table id="table30" class="clsSSWProductTable" cellspacing="2" summary="Code Auditor" cellpadding="2">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> to check for this rule. </td>
        </tr>
    </tbody>
</table>



