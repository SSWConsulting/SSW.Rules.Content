---
seoDescription: Simplify code by using null-conditional operators to easily check for null values when retrieving object properties.
type: rule
archivedreason:
title: Do you use null condition operators when getting values from objects
guid: af72188f-fb7d-452b-a23e-348ecaca6093
uri: use-null-condition-operators-when-getting-values-from-objects
created: 2020-01-29T05:20:27.0000000Z
authors:
  - title: Liam Elliott
    url: https://ssw.com.au/people/liam-elliott
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
  - do-you-use-null-condition-operators-when-getting-values-from-objects
---

Null-conditional operators - makes checking for null as easy as inserting a single question mark. The Null-conditional operators feature boils down all of the previously laborious clunky code into a single question mark.

<!--endintro-->

```cs
int length = customer != null && customer.name != null ? customer.name.length : 0;
```

::: bad
Figure: Bad example - Verbose and complex code checking for nulls
:::

```cs
int length = customers?.name?.length ?? 0;
```

::: good
Figure: Good example - Robust and easier to read code
:::
