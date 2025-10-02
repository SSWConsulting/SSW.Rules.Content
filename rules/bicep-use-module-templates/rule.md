---
seoDescription: Learn why using module templates in your Bicep code improves maintainability, reusability, and consistency across your infrastructure-as-code projects.
type: rule
title: Do you use module templates in your Bicep code?
uri: bicep-module-templates
authors:
  - title: Ben Neoh
    url: https://www.ssw.com.au/people/ben-neoh
  - title: Rick Su
    url: https://www.ssw.com.au/people/rick-su
created: 2025-10-02T10:00:00.000Z
guid: 8e4a02af-87ad-4a65-8e6e-bf903ff87d90
---

When teams start with Bicep, it’s tempting to keep everything in a single large `.bicep` file. While this works for small experiments, it quickly becomes unmanageable in real-world solutions. Changes become risky, duplication creeps in, and debugging is painful.  

That’s why **using Bicep modules**—small, reusable templates—is the recommended approach. Modules let you break down complex infrastructure into logical components, making your code easier to maintain, test, and share across projects.  

<!--endintro-->

## Why use module templates?

* **Reusability** – Define resources once and reuse them across environments (e.g. dev, test, prod).  
* **Maintainability** – Smaller files are easier to read and troubleshoot.  
* **Consistency** – Teams can follow the same patterns, reducing misconfiguration.  
* **Scalability** – Large deployments can be composed of well-tested building blocks.  

## Example: Without vs With Modules

```bicep
// main.bicep (all-in-one)
resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'myuniquestorage'
  location: resourceGroup().location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'myappinsights'
  location: resourceGroup().location
  kind: 'web'
  properties: {
    Application_Type: 'web'
  }
}
```

::: bad
Figure: Bad Example - Multiple resources jammed into a single main module, hard to maintain and reuse
:::

```bicep
// storageAccount.bicep (module)
param storageName string
param location string

resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: storageName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

// appInsights.bicep (module)
param appInsightsName string
param location string

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: appInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
  }
}

// main.bicep
module storage './storageAccount.bicep' = {
  name: 'storageDeployment'
  params: {
    storageName: 'myuniquestorage'
    location: resourceGroup().location
  }
}

module appInsights './appInsights.bicep' = {
  name: 'appInsightsDeployment'
  params: {
    appInsightsName: 'myappinsights'
    location: resourceGroup().location
  }
}
```

::: good
Figure: Good Example - A clean main module calling smaller reusable modules for storage and application insights
:::

## Best practices for modules

* **Keep modules small** – A module should represent a logical unit (e.g. a storage account, app service, or network).  
* **Use parameters and outputs** – Define clear inputs and outputs so modules are flexible.  
* **Version control** – Store commonly used modules in a shared repo or registry.  
* **Validate early** – Test modules in isolation before plugging them into larger deployments.  

By treating your Bicep modules like building blocks, you create a clean, reusable infrastructure-as-code foundation that grows with your projects.
