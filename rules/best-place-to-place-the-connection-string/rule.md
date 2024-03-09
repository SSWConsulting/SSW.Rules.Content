---
type: rule
title: Do you know the best place to place the connection string?
uri: best-place-to-place-the-connection-string
authors:
  - title: Igor Goldobin
    url: https://ssw.com.au/people/alumni/igor-goldobin/
created: 2024-03-09T06:48:10.371Z
archivedreason: As software development practices evolve, it's important to
  update our approach to managing connection strings. While the rule advocating
  for storing connection strings in the Web.Config file was effective in the
  past, modern .NET development recommends using the IOptions pattern. This
  method, detailed in Microsoft's documentation, offers a more flexible and
  robust approach to configuration management, especially in .NET Core and .NET
  environments. It moves away from traditional Web.Config or strongly typed
  settings, favoring a cleaner, scalable, and maintainable method with
  dependency injection and options classes. For a comprehensive guide on
  implementing this pattern, visit IOptions pattern in .NET.
guid: 27abe1ac-b34a-4ea7-94e5-a3cd5ba5e10b
---
The best place to put the connection string is in the Web.Config file.That makes the code simple and easy to read. Look into the following code:

<!--endintro-->

```cs
string cnnString = "data source=(local); integrated security=SSPI; persist security info=False; pooling=False; initial catalog=Northwind2";
```

::: bad
Bad Example - Using magic strings
:::

and observe the following code which is simple and easy to read:

```cs
string cnnString = LinqToNorthwind.Properties.Settings.Default.NorthwindEFConnectionString;
```

::: good
Good Example - Strongly typed connection string
:::

```cs
private void Form1_Load(object sender, System.EventArgs e)
{
    //string connString = "data source=(local); integrated security=SSPI; persist security info=False; pooling=False; initial catalog=Northwind2";
    string cnnString = LinqToNorthwind.Properties.Settings.Default.NorthwindEFConnectionString;
    cboCity.Items.Add("London");
    cboCity.Items.Add("Madrid");
    cboCity.Items.Add("Sao Paulo");
    db = new NorthwindDataContext(cnnString);
    cboCity.SelectedIndex = 0;
}
```

::: good
Good Example - Using strongly typed connection string
:::
