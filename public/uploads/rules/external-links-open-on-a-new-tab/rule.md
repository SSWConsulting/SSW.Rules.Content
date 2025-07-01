---
seoDescription: Open external links on a new tab to avoid "Back-Button Fatigue", maintain user flow and track analytics effectively.
type: rule
archivedreason:
title: Do you make external links open on a new tab?
guid: 92984462-7d50-4817-82b9-2db9685fa720
uri: external-links-open-on-a-new-tab
created: 2016-08-22T21:22:08.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - do-you-make-external-links-clear
redirects:
  - do-you-make-external-links-open-on-a-new-tab
---

External links should **open in a new tab** (by using HTML's **target="\_blank"**). Since browsers implemented tabs (replacing new window), it's considered a good practice to open external links in a different tab.

<!--endintro-->

Main reasons are:

- Avoiding 'Back-Button Fatigue';
- Keeping 'User Flow';
- Keeping a good track of Analytics

```html
<a href="http://support.microsoft.com/support">Support</a>
```

::: bad
Figure: Bad example - External link opening on the same tab
:::

```html
<a href="http://support.microsoft.com/support" target="_blank">Support</a>
```

::: good
Figure: Good example - External link opening in a new tab 
:::
