---
type: rule
archivedreason:
title: Do you share your developer secrets securely?
guid: 6165deaa-a3b0-40b1-8659-482a34faf7c4
uri: share-your-developer-secrets-securely
created: 2023-08-14T00:00:00.0000000Z
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
related: 
  - store-your-secrets-securely
redirects: []
---

Most systems will have variables that need to be stored securely; OpenId shared secret keys, connection strings, and API tokens to name a few.

These secrets **must not** be stored in source control. It is insecure and means they are sitting out in the open, wherever code has been downloaded, for anyone to see.

[Do you store your secrets securely?](https://www.ssw.com.au/rules/store-your-secrets-securely/) shows different ways to store your secrets securely. When you use .NET User Secrets, you can store your secrets in a JSON file on your local machine. This is great for development, but how do you share those secrets securely with other developers in your organization?

<!--endintro-->

### Bad Examples

::: greybox

#### Do not store secrets in appsettings.Development.json

The `appsettings.Development.json` file is meant for storing development settings. It is not meant for storing secrets. This is a bad practice because it means that the secrets are stored in source control, which is insecure.

![](development-json.jpg)

:::
::: bad
Figure: Bad practice - Overall rating: 1/10
:::

#### Sharing secrets via email/teams

Sending secrets over teams is a terrible idea, the messages can land up in logs, but they are also stored in the chat history. Developers can delete the messages once copied out, although this extra admin adds friction to the process and is often forgotten.

**Note:** Sending the secrets in email, adds even more admin for deleting the message and is probably the least secure way of transferring secrets.

![](using-teams-for-secrets.jpg)

:::
::: bad
Figure: Bad practice - Overall rating: 3/10
:::

### Good Practices

For development purposes once you are using .NET User Secrets you will still need to share them with other developers on the project.

![User Secrets are stored outside the development folder](user-secrets.jpg)

As a way of giving a heads up to other developers on the project, you can add a step in your `_docs\Instructions-Compile.md` file ([Do you make awesome documentation?](https://www.ssw.com.au/rules/awesome-documentation/)) to inform developers to get a copy of the user secrets. You can also add a placeholder to the `appsettings.Development.json` file to remind developers to add the secrets.

::: good
![Figure: Good Example - Remind developers where the secrets are for this project](development-json-with-placeholder.jpg)
:::


::: greybox

#### Use 1ty.me to share secrets securely

Using a site like [1ty.me](https://1ty.me/) allows you to share secrets securely with other developers on the project. 

Pros:

* Simple to share secrets
* Free

Cons:

* Requires a developer to have a copy of the `secrets.json` file already
* Developers need to remember to add placeholders for developer specific secrets before sharing
* Access Control - Although the link is single use, there's no absolute guarantee that the person opening the link is authorized to do so

![](1ty-me.jpg)

:::
::: good
Figure: Good Practice - Overall rating 8/10
:::


::: greybox

#### Use Enterprise Secret Management Tool – Keeper/ 1Password/ LastPass/ Hashicorp Vault/ etc..

Enterprise Secret Management tools have are great for storing secrets for various systems across the whole organization. This includes developer secrets

Pros:

* Developers don't need to call other developers to get secrets
* Placeholders can be placed in the stored secrets
* Access Control - Only developers who are authorized to access the secrets can do so

Cons:

* More complex to install and administer
* Paid Service

![](developer-secrets-in-keeper.jpg)

:::
::: good
Figure: Good Practice - Overall rating 10/10
:::
