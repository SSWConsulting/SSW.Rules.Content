---
type: rule
title: Do you avoid using duplicate connection string in web.config?
uri: do-you-avoid-using-duplicate-connection-string-in-web-config
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects: []
created: 2009-05-11T06:55:57.000Z
archivedreason: null
guid: 0bf7e11b-1185-406d-96bd-63304f056ccb
---

Since we have many ways to use Connection String in .NET 2.0, it is probably that we are using duplicate connection string in web.config.   

<!--endintro-->

```xml
<connectionStrings>
    <add 
        name="ConnectionString" 
        connectionString="Server=(local);
        Database=NorthWind;" 
    />
</connectionStrings>

<appSettings>
    <add key="ConnectionString" value="Server=(local);Database=NorthWind;"/>
</appSettings>
```
::: bad
Bad example - Using duplicate connection string in web.config
:::

