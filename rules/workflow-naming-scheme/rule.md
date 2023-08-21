---
type: rule
title: Do you know how to name your CI workflows?
uri: workflow-naming-scheme
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
created: 2023-08-20T02:02:31.620Z
guid: bb78bd25-79be-44a1-a2c9-fd1274bd449c
---

When working with Continuous Integration (CI) workflows like a GitHub Action or Azure DevOps Pipline, a poorly named file can lead to confusion and slow down the development process. Imagine having to dig into the code to understand what a workflow does every time you encounter it. It's like trying to read a book without a title or chapter names!

A well-named workflow file can save time and reduce confusion. By following a clear naming convention that reflects the purpose and sequence of the workflow, you can understand what's happening at a glance.

Naming your workflows in a way that reflects their purpose and sequence will improve developers experience. Stick to a clear and descriptive naming convention, and you'll never have to guess what a workflow does again.

<!--endintro-->

::: greybox
ssw-rulesgpt-prod.yml
:::
::: bad
Figure: Bad Example - It's unclear what the workflow does, the name doesn't reflect the sequence of actions.
:::


::: greybox
main-build-deploy.yml
:::
::: good
Figure: Bad Example - It's clear that changes to the main branch cause a build and deploy.
:::

It's easy to understand, even for someone new to the project.

Steps to naming a workflow:
1. Start with the trigger: What triggers the workflow? (e.g., main, pr)
2. Describe the main action: What's the primary task? (e.g., build, lint)
3. Include additional details: Any secondary actions or specific details? (e.g., and-deploy, infra-check)

Use this template to determine {{TRIGGER}}-{{ACTIONS}}-{{ADDITIONAL DETAILS}}.yml