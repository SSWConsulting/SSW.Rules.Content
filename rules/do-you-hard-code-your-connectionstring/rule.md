---
type: rule
archivedreason: 
title: Do you hard code your ConnectionString?
guid: 601cfc39-e263-423b-b2ab-f0d3fa50fdda
uri: do-you-hard-code-your-connectionstring
created: 2009-04-29T05:36:44.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---

We don't like hard coded string inside our programme. We are using model-driven development, in which we create or reuse code, and perform changes in configuration file rather the in-code changing. [More information on implementing our configuration](/do-you-use-configuration-management-application-block).   
<!--endintro-->


```
connection.ConnectionString = "
Provider=SQLOLEDB;
Data Source=server_name_or_address; Initial Catalog=database_name;
User ID=username; Password=password; ";

   connection.Open();
```

Bad code - use the lengthy connection string.

```
connection.ConnectionString = ConfigurationManager.Items["ConnectionString"];

 connection.Open();
```

Figure: Good Code - Use ConfigurationManager to handle the connection string.

| We have a program called [SSW Code Auditor](http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule.  |
| --- |
