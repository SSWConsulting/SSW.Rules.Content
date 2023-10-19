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

<--intro --/>

## **Bad Example**:
Scattering conditional actions and concurrency controls across multiple sub-pipelines or jobs can lead to confusion. It becomes challenging to track the flow, and potential bottlenecks or errors might be overlooked.

![Bad Example Image Placeholder](path_to_bad_example_image.png)

## **Good Example**:
Keep all conditional actions and concurrency controls centralized in the main pipeline. This provides a clear overview of the workflow and makes it easier to manage and optimize the pipeline's performance.

![Good Example Image Placeholder](path_to_good_example_image.png)

By adhering to this rule, you ensure that your CI/CD workflows remain streamlined, efficient, and easy to manage.