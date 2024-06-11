---
seoDescription: Do you have templates for your PBIs and Bugs? Learn how to ensure clean and detailed steps to reproduce a bug in Azure DevOps by setting up custom work item templates.
type: rule
title: Do you have templates for your PBIs and Bugs?
uri: do-you-have-templates-for-your-pbis-and-bugs
authors:
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects: []
created: 2019-07-26T05:34:05.000Z
archivedreason: null
guid: 6b0c6510-ccec-4f8c-9476-d934d12cf60c
---

Bugs are often hard enough to resolve but when they don't detail how to reproduce the bug, or what the expected behaviour is, it wastes a lot of time and gets frustrating for the developers. Detail in a bug report is key to your teams effectiveness and success. This is not limited to bug reports, for example PBIs can be missing Acceptance Criteria.

<!--endintro-->

In Azure DevOps, a great way to ensure you capture all the information required is through templates for your work items. Templates allow you to guide users through all the required info in a clear and concise manner, ensuring you will always have clean and detailed steps to reproduce a bug.

::: bad
![Bad example – This new bug template doesn’t make it obvious how the team likes their steps to repro](templates for pbis and bugs - bad example.png)
:::

::: good
![Good example – This new bug template guides the user to fill in the steps to repro in an ordered list and even prompts them to fill in what they expected to happen (and what actually happened)](templates for pbis and bugs - good example.png "Good example of a bug template")
:::

Setting this up is pretty easy:

1. First you need to customize the template for a work item type
   ![Figure: Customizing a bug work item](templates for pbis and bugs - customise.png)

2. Choose the form control to edit
   ![Figure: Set the default value for the Repro Steps field (Tip: use HTML)](templates for pbis and bugs - customise default value.png)

3. Save Template

### Sample code template

```md
<!-- These comments automatically delete -->
<!-- **Tip:** Delete parts that are not relevant -->
<!-- Next to Cc:, @ mention users who should be in the loop -->

Cc:

<!-- add intended user next to **Hi** -->

Hi

### Describe the Bug

<!-- A clear and concise description of what the bug is. -->

### To Reproduce

Steps to reproduce the behavior:

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

### Expected Behavior

<!-- A clear and concise description of what you expected to happen. -->

### Tasks

- [ ] Investigate
- [ ] Fix

### More Information

<!-- Add any other context about the problem here. -->

### Environment

- Device: [e.g. iPhone 12]
- Browser: [e.g. chrome, safari]
- OS: [e.g. iOS]

### Screenshots

<!-- If applicable, add screenshots to help explain your problem. -->

Thanks!
```
