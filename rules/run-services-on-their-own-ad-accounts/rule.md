---
seoDescription: Run services on their own AD accounts to ensure secure and organized management of your network's identity.
type: rule
title: Do you run services on their own AD accounts?
uri: run-services-on-their-own-ad-accounts
authors:
  - title: Kaique Biancatti
    url: https://www.ssw.com.au/people/kaique-biancatti
created: 2021-09-01T00:01:28.761Z
guid: 84d15d33-025c-45a8-97b4-7c4d35907722
---

When [using service accounts](/do-you-use-service-accounts), you should have a specific AD account for each major service.

<!--endintro-->

::: bad

![Figure: Bad example - Using the default Administrator account](defaultadministrationaccount.jpeg)
:::

::: ok
![Figure: Better example - At least don't use the Administrator account, create a new account](createnewaccount.jpeg)
:::

::: good
![Figure: Best example - A specific AD account for each major server](specificadaccount.jpeg)
:::

::: bad
![Figure: Bad example - Using the network admin's name](networkadminname.jpeg)
:::

::: good
![Figure: Good example - A specific SQL Server account being used (Suggestion: Make the text box wider and link to the one in 'Services')](sqlserveraccount.jpeg)
:::
