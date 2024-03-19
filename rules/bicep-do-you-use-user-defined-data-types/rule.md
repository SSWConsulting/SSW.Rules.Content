---
type: rule
archivedreason:
title: Bicep - Do you use User-defined Data Types?
guid: 2a3ba816-ba40-4cfe-8193-7e151e038ac5
uri: bicep-user-defined-data-types
created: 2024-03-19T19:19:19.1919191Z
authors:
- title: Rick Su
  url: https://ssw.com.au/people/rick-su
related: []
redirects: []

---

[User-defined data types in Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/user-defined-data-types) allow you to create custom data structures for better code organization and type safety. They enhance reusability, abstraction, and maintainability within projects .

<!--endintro-->

## Get Started

[Bicep CLI version 0.12.X or higher](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install) is required to use this feature.

## Pain

When creating a cloud resource, numerous parameters are typically required for configuration and customization. Organizing and naming these parameters effectively is increasingly important.

``` bicep
@allowed(['Basic', 'Standard'])
param skuName string = 'Basic'
@allowed([5, 10, 20, 50, 100])
param skuCapacity int = 5
param skuSizeInGB int = 2
```

:::bad
Bad example - Relying on parameter prefixes and order leads to unclear code, high complexity, and increased maintenance effort.
:::

``` bicep
// User-defined data type
type skuConfig = {
  name: 'Basic' | 'Standard'
  capacity: 5 | 10 | 20 | 50 | 100
  sizeInGB: int
}

param sku skuConfig = {
  name: 'Basic'
  capacity: 5
  sizeInGB: 2
}
```

:::good
Good example - User-defined data type provides type safety, enhanced readability and making maintenance easier.
:::
