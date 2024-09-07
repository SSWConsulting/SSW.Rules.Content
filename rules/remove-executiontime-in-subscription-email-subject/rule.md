---
type: rule
archivedreason:
title: Admin - Do you remove @ExecutionTime in subject of subscription email?
guid: 69500811-c6f2-4e36-9d12-4086244631ad
uri: remove-executiontime-in-subscription-email-subject
created: 2024-08-02T14:47:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

In subscription settings, @ExecutionTime should be removed from subject, because it ruins conversation threading in Outlook - You cannot sort them by subject.

<!--endintro-->

::: bad  
![Figure: Bad example - Keep @ExecutionTime in subject](RSRulesRemoveTimeOld.gif)  
:::

So we always make subject of subscription exactly same as report name.

::: good  
![Figure: Good example - Subject same as report name](RSRulesRemoveTimeNew.gif)
:::
