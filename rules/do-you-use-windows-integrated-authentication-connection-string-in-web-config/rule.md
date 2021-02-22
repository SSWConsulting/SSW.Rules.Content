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
<!--endintro-->

We recommend you use the Windows NT authentication by default, because Windows security services operate by default with the Microsoft Active Directory?directory service, it is a derivative best practice to authenticate users against Active Directory. Although you could use other types of identity stores in certain scenarios, for example Active Directory Application Mode (ADAM) or Microsoft SQL Server? these are not recommended in general because they offer less flexibility in how you can perform user authentication.

If not, then add a comment confirming the reason.




```
<connectionStrings>
   <add name="ConnectionString" connectionString="Server=(local);
    Database=NorthWind;Integrated Security=SSPI;" />
</connectionStrings>
```

          Bad example - not use Windows Integrated Authentication connection string without comment.   





```
<connectionStrings>
    <add name="ConnectionString" connectionString="Server=(local);
     Database=NorthWind;Integrated Security=SSPI;" />
</connectionStrings>
```

          Good example - use Windows Integrated Authentication connection string by default.   





```
<connectionStrings>
                    <add name="ConnectionString" 
                     connectionString="Server=(local);
                     Database=NorthWind;uid=sa;pwd=sa;" />
                    <!--It can't use the Windows Integrated because they are 
                     using Novell -->                
</connectionStrings>
```

          Good example - not use Windows Integrated Authentication connection string with comment.
