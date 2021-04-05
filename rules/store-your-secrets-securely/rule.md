---
type: rule
archivedreason: 
title: Do you store your secrets securely?
guid: 57dc15ba-605a-4a71-8b0e-d9f1551b9fc0
uri: store-your-secrets-securely
created: 2016-04-28T19:19:40.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Andrew Lean
  url: https://ssw.com.au/people/andrew-lean
related: []
redirects:
- do-you-store-your-secrets-securely

---

Most systems will have variables that need to be stored securely; OpenId shared secret keys, connection strings, and API tokens to name a few.

These secrets **must not** be stored in source control in plain text – it is insecure by nature, and basically means that it is sitting.

<!--endintro-->

There are many options for managing secrets in a secure way:

### Bad Practices

::: greybox

#### Store production passwords in source control protected with the [ASP.NET IIS Registration Tool](https://docs.microsoft.com/en-us/previous-versions/zhhddkxy(v=vs.140)?redirectedfrom=MSDN)

Pros:
* Minimal change to existing process – no need for [DPAPI](https://docs.microsoft.com/en-us/previous-versions/ms995355(v=msdn.10)?redirectedfrom=MSDN) or a dedicated Release Management (RM) tool
* Simple and easy to understand

Cons:
* Need to manually give the app pool identity ability to read the default RSA key container
* Difficult to manage production and non-production config settings
* Developers can easily decrypt and access the production password
* Manual transmission of the password from the key store to the encrypted config file
:::
::: bad
Figure: Bad practice - Overall rating: 2/10
:::
    

::: greybox

#### Use Windows Identity instead of username/ password

Pros:
* Minimal change to existing process – no need for DPAPI or a dedicated RM tool
* Simple and easy to understand

Cons:
* Difficult to manage production and non-production config settings
* Not generally applicable to all secured resources
* Can hit firewall snags with Kerberos and AD ports
* Vulnerable to DOS attacks related to password lockout policies
* Has key-person reliance on network admin
:::
::: bad
Figure: Bad practice - Overall rating: 4/10  
:::
   

::: greybox

#### [Use External Configuration Files](https://docs.microsoft.com/en-us/aspnet/identity/overview/features-api/best-practices-for-deploying-passwords-and-other-sensitive-data-to-aspnet-and-azure)

Pros:
* Simple to understand and implement

Cons:
* Makes setting up projects the first time very hard
* Easy to accidentally check the external config file into source control
* Still need DPAPI to protect the external config file
* No clear way to manage the DevOps process for external config files
:::
::: bad
Figure: Bad practice - Overall rating: 1/10  
:::

### Good Practices

::: greybox

#### Use Octopus/ VSTS RM secret management, with passwords sourced from KeePass

Pros:
* Scalable and secure
* General industry best practice - great for organizations of most sizes below large corporate

Cons:
* Password reset process is still manual
* DPAPI still needed
:::
::: good
Figure: Good practice - Overall rating: 8/10  
:::

::: greybox

#### Use Enterprise Secret Management Tool – LastPass/ Hashicorp Vault/ etc..

Pros:
* Enterprise grade – supports cryptographically strong passwords, auditing of secret access and dynamic secrets
* Supports hierarchy of secrets
* API interface for interfacing with other tools
* Password transmission can be done without a human in the chain

Cons:
* More complex to install and administer
* DPAPI still needed for config files at rest
:::
::: good
Figure: Good practice -  Overall rating: 8/10
:::

::: greybox

#### Use Azure KeyVault

See the [SSW Rewards](https://www.ssw.com.au/ssw/Rewards/) mobile app repository for how SSW is using this in a production application: [https://github.com/SSWConsulting/SSW.Rewards](https://github.com/SSWConsulting/SSW.Rewards)

Pros:
* Best solution for cloud (Azure) solutions
* Enterprise grade
* Uses industry standard best encryption
* Dynamically cycles secrets
* Access granted based on Azure AD permissions - no need to 'securely' share passwords with colleagues
* Can be used to inject secrets in your CI/CD pipelines for non-cloud solutions

Cons:

* Price is per transaction - can become costly if used in high volume and not managed thoroughly (see [SSW's William Liebenberg on Azure SpendOps](https://azuregems.io/spendops-with-azure-cosmos-db/)
:::
::: good
Figure: Good Practice - Overall rating 9/10  
:::
