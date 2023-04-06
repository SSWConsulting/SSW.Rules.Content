---
type: rule
archivedreason: 
title: Do you avoid using duplicate connection string in web.config?
guid: 0bf7e11b-1185-406d-96bd-63304f056ccb
uri: do-you-avoid-using-duplicate-connection-string-in-web-config
created: 2009-05-11T06:55:57.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

Since we have many ways to use Connection String in .NET 2.0, it is probably that we are using duplicate connection string in web.config.   
<!--endintro-->


```
<connectionStrings>
   <add name="ConnectionString" connectionString="Server=(local);
Database=NorthWind;" />
</connectionStrings>
<appSettings>
   <add key="ConnectionString" value="Server=(local);Database=NorthWind;"/>
</appSettings>
```

          Bad example - use duplicate connection string in web.config.   

| We have a program called [SSW Code Auditor](http&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule. |
| --- |
