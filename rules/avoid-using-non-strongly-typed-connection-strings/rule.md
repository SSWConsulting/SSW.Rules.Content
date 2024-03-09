---
type: rule
title: Do you avoid using non strongly typed connection strings?
uri: avoid-using-non-strongly-typed-connection-strings
authors:
  - title: Igor Goldobin
    url: https://ssw.com.au/people/alumni/igor-goldobin/
created: 2024-03-09T06:15:30.110Z
archivedreason: "In light of the evolving best practices in software
  development, it's worth noting an update to the rule regarding the management
  of connection strings. While the use of Application Settings in Visual Studio
  was a solid approach for managing connection strings at one time, modern
  development practices recommend a more contemporary method. Now, we advise to
  utilize the IOptions pattern from Microsoft. This approach aligns with current
  standards for robust and flexible configuration management, especially in .NET
  Core applications. The IOptions pattern offers enhanced capabilities for
  handling configurations in a way that's more aligned with the latest .NET
  development paradigms. For a comprehensive understanding and guidance on
  implementing this pattern, refer to the official Microsoft documentation:
  IOptions pattern in .NET. This resource provides valuable insights into
  effectively using the IOptions pattern for managing application settings,
  including connection strings."
guid: 27abe1ac-b34a-4ea7-94e5-a3cd5ba5e10b
---
Using non strongly typed connection strings means that you have to hard code at some point in your code. Once you change the name of your connection strings, you have to change the code that references them too.

Visual Studio provides a convenient tool, called Application Settings, that allows you to manage all of your connection strings from only one location. You can use its wizard to compose connection strings quickly and correctly. Also, it provides a management class to read and write all of your connection strings.

<!--endintro-->

```cs
var connString = System.Configuration.ConfigurationManager.ConnectionStrings["MyProj.Properties.Settings.ConnectString"].ToString();
var conn = new SqlConnection(ConnString);
var cmd = new SqlCommand(strSql, conn);
conn.Open();
cmd.ExecuteNonQuery();
conn.Close();
```

::: bad
Bad Example - Using non strongly typed connection strings, the highlighted text is hard code actually
:::

::: good
![Figure: Good example - Using Application Settings to configure connection strings](conn.gif)
:::
