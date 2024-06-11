---
seoDescription: Defining a new build in TFS requires checking workspaces to ensure only relevant files are included.
type: rule
archivedreason:
title: Do you check your Workspaces when defining a new build?
guid: a8c4e7bc-555d-4420-80a5-29b0d2924d94
uri: do-you-check-your-workspaces-when-defining-a-new-build
created: 2012-03-28T05:38:50.0000000Z
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Daragh Bannigan
    url: https://twitter.com/dbannigan
    noimage: true
related: []
redirects: []
---

When defining a build, you should always check the Workspace tab. Only the workspace relevant to your build should be included.

<!--endintro-->

If you have a number of Team Projects open from the same TFS Project Collection, all of their workspaces will be included by default. You should remove those workspaces that aren’t being used otherwise the build server will get the source for every workspace in this list before starting a build.

::: bad
![Figure: Bad example – Several workspaces from other team projects are included by default](bad_workspace.png)
:::

::: good
![Figure: Good example – Only the relevant workspace has been included in this build definition](good_workspace.png)
:::
