---
seoDescription: Avoid using non-strongly-typed connection strings to improve code maintainability and reduce errors.
type: rule
title: Do you avoid using non strongly typed connection strings?
uri: avoid-using-non-strongly-typed-connection-strings
authors:
  - title: Igor Goldobin
    url: https://ssw.com.au/people/alumni/igor-goldobin/
created: 2024-03-09T06:15:30.110Z
archivedreason: Update connection string management - favor IOptions pattern over Visual Studio's Application Settings. Offers robust, flexible config in .NET Core, aligning with modern development practices. Refer to Microsoft's IOptions pattern in .NET documentation for implementation guidance.
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
Bad example - Using non strongly typed connection strings, the highlighted text is hard code actually
:::

::: good
![Figure: Good example - Using Application Settings to configure connection strings](conn.gif)
:::
