---
type: rule
archivedreason: 
title: Do you parameterize all input to your database?
guid: 34c49f46-1057-42b1-8436-f8c0a05af103
uri: parameterize-all-input-to-your-database
created: 2020-03-18T23:01:46.0000000Z
authors:
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- do-you-parameterize-all-input-to-your-database

---

It is important to parameterize all input to your database and it’s easy to implement.
Doing so will also reduce a lot of headaches down the track.

 ![](ParameterizeSqlInputsXKCD.png) **Figure: What can happen if you don’t parameterize your inputs
Source: [xkcd.com](https://xkcd.com/327/)
** 

<!--endintro-->

::: good
Advantages

:::

* Prevents SQL injection attacks
* Preserves types being sent to the database
* Increased performance by reducing the number of query plans
* Makes your code more readable

```sql
SELECT Id, CompanyName, ContactName, ContactTitle
FROM dbo.Customers
WHERE CompanyName = 'NorthWind';
```

::: bad
Figure: Bad Example - Using a dynamic SQL query

:::

```sql
SELECT Id, CompanyName, ContactName, ContactTitle
FROM dbo.Customers
WHERE CompanyName = @companyName;
```

::: good
Figure: Good Example - Using a parameterized query

:::

### Should I use Parameters.AddWithValue()?
Using Parameters.AddWithValue() can be a bit of a shortcut as you don’t need to specify a type. However shortcuts often have their dangers and this one certainly does.
For most cases [Parameters.AddWithValue()](https://docs.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlparametercollection.addwithvalue?view=netframework-4.8) will guess correctly, but sometimes it doesn’t which can lead to the value being misinterpreted when sent to the database. This can be avoided using [Parameters.Add()](https://docs.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlparametercollection.add?view=netframework-4.8) and specifying the [SqlDbType](https://docs.microsoft.com/en-us/dotnet/api/system.data.sqldbtype?view=netframework-4.8), this will ensure the data will reach the database in the correct form.
When using dates, strings, varchar and nvarchar it is strongly recommended to use  **Parameters.Add()** as there is a possibility of  **Parameters.AddWithValue()** to incorrectly guess the type.
Implementing parameterized queries using Parameters.Add()

```sql
cmd.Parameters.Add("@varcharValue", System.Data.SqlDbType.Varchar, 20).Value = “Text”;
```

::: good
Figure: Good Example – Using VarChar SqlDbType and specifying a max of 20 characters (-1 for MAX)

:::

```sql
cmd.Parameters.Add("@decimalValue", System.Data.SqlDbType.Decimal, 11, 4).Value = decimalValue;
```

::: good
Figure: Good Example – Using decimal(11,4) SQL Parameter

:::

```sql
cmd.Parameters.Add("@dateTimeValue", System.Data.SqlDbType.DateTime2).Value = DateTime.UtcNow;
```

::: good
Figure: Good Example - C#, VB .NET SQL DateTime Parameter

:::

```sql
$SqlCmd.Parameters.Add("@dateTimeValue", [System.Data.SqlDbType]::DateTime2).Value = $dateTime2Value
```

::: good
Figure: Good Example - PowerShell SQL DateTime Parameter

:::
