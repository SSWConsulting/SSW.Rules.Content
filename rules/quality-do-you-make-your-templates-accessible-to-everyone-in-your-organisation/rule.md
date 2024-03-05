---
type: rule
archivedreason: 
title: IP - Do you make your templates accessible to everyone in your organization?
guid: ce7cf067-10fa-402c-b915-2a69cdaea651
uri: quality-do-you-make-your-templates-accessible-to-everyone-in-your-organisation
created: 2012-09-25T18:01:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- ip-do-you-make-your-templates-accessible-to-everyone-in-your-organisation

---

A common mistake is to use code or emails that you have previously written, and stored somewhere on your computer, and change around key bits to make it relevant for the current situation.

The problem with this is that you make it impossible for anyone else in your organization to do the same task to the same quality level.

<!--endintro-->

Make sure your company has a common code base and email template store and endeavour to improve it regularly. This shares knowledge across your organization and makes sure everyone is working to the level that your company standards require.

### Create Nuget Packages for reusable code libraries

The best approach to reuse code across multiple projects is to create Nuget Packages. When you need to update that library, it is then trivial to apply that update to your client projects.

::: good
![Figure: Good example - when reusing code across multiple projects for a single client, hosting your own Nuget Server provides an excellent way to manage shared private dependencies](BCE_Nuget_Server.png)
:::

For details on creating your own internal Nuget repository, read [Do you create a private repository for reusable internal code?](/do-you-create-a-private-repository-for-reusable-internal-code)

::: good
![Figure: Good example - If your library has potential outside of your current requirement, consider publishing to the world on Nuget.  Often the work involved to make a library more generic and re-usable results in better-quality code](SSW_nuget.png)
:::

See a [selection of Nuget packages published by SSW](https://www.nuget.org/profiles/SSW).
