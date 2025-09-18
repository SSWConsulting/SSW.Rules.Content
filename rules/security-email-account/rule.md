---
type: rule
title: Do you have a security@ email account?
seoDescription: Learn why every company should have a security@ email address to
  handle vulnerability reports, prevent public exploits, and build trust with
  ethical hackers. Includes best practices, response tips, and a warning about
  common bug bounty scams.
uri: security-email-account
authors:
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects: []
created: 2025-03-25T00:01:20.896Z
guid: 58523891-7aa2-4f5c-ae34-376d002f0a14
---
When hackers or security researchers find a vulnerability in your system, they need a way to tell you. If you don’t have a security@yourcompany.com email, they might give up or go public.

Your `security@` inbox is your first line of defense.

<!--endintro-->

It helps with:

* Responsible disclosure from ethical hackers
* Bug bounty submissions
* Early warnings before public leaks

You don’t need a full bug bounty program to start. Just set up the email, publish it (e.g. in your [security.txt](https://securitytxt.org)), and monitor it.

Make sure it’s:

* Monitored by trusted staff (not just one person)
* Responded to quickly (aim for &lt; 48h)
* Part of your incident response process


::: bad  
Bad example: No security@ exists. The researcher tweets the exploit. The company finds out via media. Damage is done.
:::

::: good  
Good example: A security researcher finds a critical bug and emails security@. The team replies in 1 day, verifies the issue, patches it in a week, and thanks the reporter.
:::

::: info
Be aware of ["beg bounties"](https://www.troyhunt.com/beg-bounties/) – people who send low-risk reports and demand money. You can politely thank them or ignore if it’s not a real issue.
:::

::: info
Want ethical hackers to help you? Add a [security.txt](https://securitytxt.org) file with your security contact information. Check out how we setup ours - https://github.com/SSWConsulting/securitytxt
:::
