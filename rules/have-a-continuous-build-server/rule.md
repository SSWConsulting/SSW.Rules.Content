---
seoDescription: Implementing a Continuous Integration (CI) server reduces the risk of introducing unwanted changes by automatically building and testing software after each code update.
type: rule
title: Do you have a Continuous Integration (CI) Server?
uri: have-a-continuous-build-server
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
  - do-you-have-a-continuous-integration-ci-server
  - do-you-have-a-continuous-integration-(ci)-server
created: 2020-03-12T23:23:23.000Z
archivedreason: null
guid: 74607e42-d950-4b8a-98ce-b0e87a3f324d
---

A Continuous Integration (CI) server monitors the Source Control repository and, when something changes, it will checkout, build and test the software.

If something goes wrong, notifications are sent out immediately (e.g. via email or Teams) so that the problems can be quickly remedied.

<!--endintro-->

::: greybox

### It's all about managing the risk of change

Building and testing the software on each change made to the code helps to reduce the risk of introducing unwanted changes in its functionality without us realising.

The various levels of automated testing that may form part of the CI pipeline (e.g. unit, contract, integration, API, end-to-end) all act as change detectors, so we're alerted to unexpected changes almost as soon as the code that created them is committed to the code repository.

The small change deltas between builds in combination with continuous testing should result in a stable and "known good" state of the codebase at all times.
:::

::: info
**Tip:** Azure DevOps and GitHub both provide online build agents with a free tier to get you started.
:::
