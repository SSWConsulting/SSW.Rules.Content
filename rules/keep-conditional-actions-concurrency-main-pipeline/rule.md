---
type: rule
title: Do you keep conditional actions and concurrency to the main pipeline?
uri: keep-conditional-actions-concurrency-main-pipeline
authors:
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy/
created: 2023-10-19T00:39:49.331Z
guid: c725ced3-e675-40f7-b43d-d5db1501b844
---
When designing CI/CD workflows, it's essential to maintain clarity and simplicity. This ensures that your pipelines are easy to understand, modify, and troubleshoot.

<!--endintro-->

Scattering conditional actions and concurrency controls across multiple sub-pipelines or jobs can lead to confusion. It becomes challenging to track the flow, and potential bottlenecks or errors might be overlooked.

::: bad

![Bad Example - Conditionals and concurrency in main workflow](github-concurrency-main-pipeline.png)

![Bad Example - Conditionals and concurrency in called workflow](github-concurrency-calledworkflow.png)
:::

Keep all conditional actions and concurrency controls centralized in the main pipeline. This provides a clear overview of the workflow and makes it easier to manage and optimize the pipeline's performance.

![Good Example - Only the main workflow has a conditional](github-concurrency-main-pipeline.png)

By adhering to this rule, you ensure that your CI/CD workflows remain streamlined, efficient, and easy to manage.