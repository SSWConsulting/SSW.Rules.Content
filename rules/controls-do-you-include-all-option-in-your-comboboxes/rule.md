---
seoDescription: Controls - Include '-All-' option in your ComboBoxes to give users a chance to select all data.
type: rule
archivedreason:
title: Controls - Do you include '-All-' option in your ComboBoxes?
guid: 8e68dce9-43f5-4397-a422-09cecd3c830c
uri: controls-do-you-include-all-option-in-your-comboboxes
created: 2012-11-27T08:38:56.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

ComboBoxes are often used for filtering data. It is best to have an '-All-' option to give your user chances to select all data.

It is important to understand the idea of **visual text** . In a list you could see either:

- -None- or
- No activity assigned

They both have the same meaning, but the first one is immediately visible whereas the second one must be read.

<!--endintro-->

If the ID column in your database is a string data type, it is useful to add a constraint to limit the types of characters that it can contain. Adding a constraint can make it simpler to build your front-end, as you won't need to worry about encoding or escaping to handle special characters.

In SQL Server, you can add a check constraint that limits your column to alphanumeric characters, a hyphen, or underscore using the following T-SQL:

```sql
ALTER TABLE [TableName] ADD CONSTRAINT CK_String_Identifier
    CHECK ([StringIdColumn] NOT LIKE'%[^a-zA-Z0-9_\-]%')
```

::: bad
![Figure: Bad example - No '-All-' option so the user cannot select all data](../../assets/Combo-ALL-1.jpg)
:::

::: good  
![Figure: Good example - Having an '-All-' option gives a user a chance to select all data](../../assets/Combo-ALL-2.jpg)  
:::

Also, keep it simple!

::: bad  
![Figure: Bad example - '-All Stores-' isn't needed](../../assets/SelectAllBad.jpg)  
:::

::: good  
![Figure: Good example - Keep it as a simple '-All-'](../../assets/SelectAllGood.jpg)  
:::

::: good  
![Figure: Good example - Keeping it simple makes it easy to spot (that there is no filter) when you have multiple fields.](../../assets/SelectAllVGood.gif)
:::

Read our rule on [Always make sure the dimensions All Captions = All](http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterBusinessIntelligence.aspx#AllDimensionsTag).
