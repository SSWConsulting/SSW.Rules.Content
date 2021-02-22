---
type: rule
archivedreason: 
title: Do you use Windows Integrated Authentication connection string in web.config?
guid: d8967ec8-56b1-4acc-81ff-8cc5dec43fe0
uri: do-you-use-windows-integrated-authentication-connection-string-in-web-config
created: 2009-05-11T07:09:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


Both SQL Server authentication (standard security) and Windows NT authentication (integrated security) are SQL Server authentication methods that are used to access a SQL Server database from Active Server Pages (ASP). 

<br><excerpt class='endintro'></excerpt><br>

  <p>We recommend you use the Windows NT authentication by default, because Windows security services operate by default with the Microsoft Active Directory?directory service, it is a derivative best practice to authenticate users against Active Directory. Although you could use other types of identity stores in certain scenarios, for example Active Directory Application Mode (ADAM) or Microsoft SQL Server? these are not recommended in general because they offer less flexibility in how you can perform user authentication. </p>
<p>If not, then add a comment confirming the reason.</p>
<p>&#160;</p>
<dl class="badCode">
    <dt style="width&#58;92.17%;height&#58;126px;">
    <pre>&lt;connectionStrings&gt;<br>   &lt;add name=&quot;ConnectionString&quot; connectionString=&quot;Server=(local);<br>    Database=NorthWind;Integrated Security=SSPI;&quot; /&gt;<br>&lt;/connectionStrings&gt;</pre>
    </dt>
    <dd>Bad example - not use Windows Integrated Authentication connection string without comment. </dd>
</dl>
<p>&#160;</p>
<p>&#160;</p>
<dl class="goodCode">
    <dt style="width&#58;92.02%;height&#58;100px;">
    <pre>&lt;connectionStrings&gt;<br>    &lt;add name=&quot;ConnectionString&quot; connectionString=&quot;Server=(local);<br>     Database=NorthWind;Integrated Security=SSPI;&quot; /&gt;<br>&lt;/connectionStrings&gt;</pre>
    </dt>
    <dd>Good example - use Windows Integrated Authentication connection string by default. </dd>
</dl>
<p>&#160;</p>
<p>&#160;</p>
<dl class="goodCode">
    <dt style="width&#58;92.79%;height&#58;152px;">
    <pre>                &lt;connectionStrings&gt;<br>                &#160;&#160;&#160;&#160;&lt;add name=&quot;ConnectionString&quot; <br>                     connectionString=&quot;Server=(local);<br>                     Database=NorthWind;uid=sa;pwd=sa;&quot; /&gt;<br>                &#160;&#160;&#160;&#160;&lt;!--It can't use the Windows Integrated because they are <br>                     using Novell --&gt;                <br>&lt;/connectionStrings&gt;</pre>
    </dt>
    <dd>Good example - not use Windows Integrated Authentication connection string with comment.</dd>
</dl>



