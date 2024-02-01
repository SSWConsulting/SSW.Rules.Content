---
type: rule
archivedreason: Duplicate of [https://www.ssw.com.au/rules/write-a-good-pull-request/](/rules/write-a-good-pull-request/)
title: Do you include a useful description of your changes?
uri: useful-information-on-changes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - write-a-good-pull-request
  - github-content-changes
  - meaningful-pbi-titles
created: 2023-02-08T19:59:31.616Z
guid: e126fb1b-8b28-4712-b928-6ba400274015

---

When creating a Pull Request with your changes, it is important to have a good description that will help the reviewer to understand what was done.

Leaving the description blank is common and not helpful. There are also cases where people overexplain. **You should try to include just the right amount of information.**

<!--endintro-->

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:**  
:::
::: bad
Figure: Bad example - Cannot tell what was done here
:::

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:** Changes made:

1. Added missing video figure to embedded YouTube video
2. Fixed typo:  
From:  
Use emojis. See our rule on emojis in Scrum).  
To:  
Use emojis. See our rule on emojis in Scrum
:::
::: ok
Figure: OK example - What was done is clear, but both editor and reviewer may spend too much time on the description of such simple changes
:::

Try to make generic comments that objectively summarize your changes. This way the reviewer will know what to expect and confirm the changes by looking at the file diffs.

::: greybox
**PR title:** Update Rule “meaningful-pbi-titles/rule”

**PR description:** Added missing video caption + removed unnecessary brackets
:::
::: good
Figure: Clear and concise description
:::

### Many small changes

You should summarize by saying: _“Improved readability”_ OR _“Fixed typos and grammar”_

### Big and complex changes

You should include a demonstration of the change. E.g. A [screenshot](/screenshots-avoid-walls-of-text) to show text/UI changes, or a [Done video](/record-a-quick-and-dirty-done-video) to demo functionality changes.
