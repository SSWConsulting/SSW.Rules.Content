---
type: rule
title: GitHub Actions - Do you know why Job Summaries are awesome?
uri: use-job-summaries
authors:
  - title: Steven Qiang
    url: https://ssw.com.au/people/steven-qiang
related: []
redirects: []
created: 2022-07-06T02:07:35.474Z
guid: 26f7e0e7-f154-4117-85a7-77030c904adc
---
GitHub Actions are awesome but it can be really painful when you need to go digging through hundreds of lines of log output to find a problem. So, there has been a huge amount of requests for Markdown reporting analytics in GitHub Actions.

Job Summaries solves this problem by allowing you to generate and group custom Markdown content on the Actions and publish them when the action finishes. This summary is awesome because it gives you a quick visual indicator at a glance.

For example, when running a series of tests, it's so good to see all the [green ticks and crosses](/use-icons-webpages) showing which ones succeeded.

![Figure: Job Summaries with Markdown](screen-shot-2022-07-06-at-1.36.21-pm.png "Job Summaries with Markdown")

Custom Markdown content can be used for a variety of creative purposes, such as:

* Aggregating and displaying test results
* Generating reports
* Custom output independent of logs

More info: [How to create Job Summaries for GitHub Actions](https://github.blog/2022-05-09-supercharging-github-actions-with-job-summaries/)
