---
type: rule
title: Do you update your packages regularly?
uri: do-you-update-your-packages-regularly
authors:
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []
created: 2014-11-27T18:18:39.000Z
archivedreason: null
guid: eed63bcd-bdd8-47ed-baf2-8200f9f99547
---
NuGet makes it easy to find and apply package updates – but this still must be performed manually.

<!--endintro-->

Each package update should contain improvements but also involves a small amount of risk in the form of breaking changes or regressions.

Updating often can help mitigate this risk by ensuring that each individual update is smaller.

Recommended practice is to apply package updates at the start of a Sprint so that there is time to find and resolve issues introduced by the update.

![Figure: NuGet package updates](update-nuget.png)

Visual Studio will give you a count of how many outdated packages are present in your solution.

![Figure: Visual Studio displays a badge with the amount of outdated packages (2 in this example)](screenshot-2024-01-16-at-3.02.19 pm.png)