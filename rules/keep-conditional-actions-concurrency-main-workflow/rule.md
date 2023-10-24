---
type: rule
title: Do you keep conditional actions and concurrency to the main workflow?
uri: keep-conditional-actions-concurrency-main-workflow
authors:
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy/
created: 2023-10-19T00:39:49.331Z
guid: c725ced3-e675-40f7-b43d-d5db1501b844
---

When designing CI/CD workflows, it's essential to maintain clarity and simplicity. This ensures that your pipelines are easy to understand, modify, and troubleshoot.

<!--endintro-->

Scattering conditional actions and concurrency controls across multiple sub-pipelines or jobs can lead to confusion. Tracking the flow becomes challenging, and potential bottlenecks or errors might be overlooked.

::: bad
![Figure: Bad example - Conditionals and concurrency in main workflow](github-concurrency-main-pipeline.png)
:::

Adding further conditionals or concurrency controls to the workflows adds no value. The workflow still only runs in the "dev" environment and operates within its own concurrency group. However, when changes are made to the more visible workflow (CICD.yaml), it's less obvious that changes are needed in the called workflow.

::: bad
![Figure: Bad example - Conditionals and concurrency in called workflow](github-concurrency-calledworkflow.png)
:::

Centralize all conditional actions and concurrency controls in the main pipeline. This approach provides a clear overview of the workflow, making it easier to manage and optimize the pipeline's performance.

::: good
![Figure: Good example - Only the main workflow has conditional and concurrency](github-concurrency-main-pipeline.png)
:::

::: good
![Figure: Good example - Called workflow doesn't contain conditionals or concurrency groups](github-concurrency-calledworkflow-good.png)
:::

Of course, there are occasional circumstances where a called workflow must contain a conditional. However, these instances should be limited and documented thoroughly to ensure clarity and maintainability.

By adhering to this rule, you ensure that your CI/CD workflows remain streamlined, efficient, and easy to manage.
