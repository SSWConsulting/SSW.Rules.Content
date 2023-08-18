---
type: rule
title: Do you use Configuration over Key Vault?
uri: config-over-keyvault
authors:
  - title: Andrew Harris
    url: https://ssw.com.au/people/andrew-harris
created: 2023-08-08T23:45:18.798Z
guid: d104022e-2cce-4771-a54a-42e6dfbdaf09
---

We all know that we should [Store Secrets Securely](/store-your-secrets-securely) using Key Vault, but did you know that rather than have developers having to deal with a combination of Key Vault and Configuration, you can abstract Key Vault out of your application code and leave developers to only have to deal with Configuration?

<!--endintro-->

::: bad
![Figure: Bad example - Having to wire up Key Vault unnecessarily](badkeyvault.png "Wiring up both KeyVault and Configure")
:::

A feature of Azure AppService is the ability to [use secrets from Key Vault as Configuration values](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references). This allows you to setup a link between your AppService and a Key Vault and have Configuration values point to a Key Vault Entry.

So now rather than developers having to think about if a value is a secret or configurations, it's always configuration. It just might have its value stored securely in Key Vault.

::: good
![Figure: Good Example - Developers don't need to know anything about Key Vault](goodkeyvault.png)
:::
