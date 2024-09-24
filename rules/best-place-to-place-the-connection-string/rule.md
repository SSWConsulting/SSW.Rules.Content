---
seoDescription: Best place to put connection string - IOptions pattern over Web.config enables flexible and robust config in .NET.
type: rule
title: Do you know the best place to place the connection string?
uri: best-place-to-place-the-connection-string
authors:
  - title: Igor Goldobin
    url: https://ssw.com.au/people/alumni/igor-goldobin/
created: 2024-03-09T06:48:10.371Z
archivedreason: |
  Update connection string management: prefer IOptions pattern over Web.Config. Enables flexible, robust config in .NET, emphasizing dependency injection.
guid: 27abe1ac-b34a-4ea7-94e5-a3cd5ba5e10b
---

The best place to put the connection string is in the Web.Config file.That makes the code simple and easy to read. Look into the following code:

<!--endintro-->

```cs
string cnnString = "data source=(local); integrated security=SSPI; persist security info=False; pooling=False; initial catalog=Northwind2";
```

::: bad
Bad example - Using magic strings
:::

and observe the following code which is simple and easy to read:

```cs
string cnnString = LinqToNorthwind.Properties.Settings.Default.NorthwindEFConnectionString;
```

::: good
Good example - Strongly typed connection string
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
Good example - Using strongly typed connection string
:::
