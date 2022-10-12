---
type: rule
archivedreason: 
title: Do you use LINQ instead of CAML?
guid: ceb1e790-eafc-44f3-91b9-c718c7bba67e
uri: do-you-use-linq-instead-of-caml
created: 2009-12-09T04:22:07.0000000Z
authors:
- title: Andy Taslim
  url: https://ssw.com.au/people/andy-taslim
related: []
redirects: []

---

In SharePoint development, it is always a good practice to use LINQ, instead of CAML.

<!--endintro-->

Why CAML is bad? 
* New language skills required for .NET developers
* No IntelliSense or strongly typed objects

Why LINQ is good?

* No new language skills required
* Easier to read and write
* SPMetal is awesome for generating entity classes
* In the backend, LINQ provider translates as much as it can to CAML first

``` ocaml
SPQueryquery = newSPQuery(); 

query.Query= String.Format(“

<Where>

<And>

<Contains><FieldRefName=‘Tags’ /><ValueType=‘Text’>{0}</Value></Contains>

<IsNotNull><FieldRefName=‘URL’ /></IsNotNull>

</And>

</Where>

<OrderBy>

<FieldRefName=‘PostedOn’ Ascending=‘TRUE’ />

</OrderBy>”, _filter);

SPListItemCollectionlistItemsColl= resourceList.GetItems(query);
```
::: bad
Figure: Bad example – using CAML  
:::


``` cs
Var resourceListItems =

From SPListItem item in resourceList.Items

Where item.Tags.ToString().ToLower().Contains(_filter)

&& item.URL.ToString().Length> 0

OrderBy item.PostedOn Ascending
```
::: good
Figure: Good example – using LINQ  
:::
