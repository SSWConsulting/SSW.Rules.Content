---
type: rule
archivedreason: 
title: Do you prioritize performance optimization for maximum business value?
guid: b23385cd-e321-44bb-90b2-90075875e97c
uri: prioritize-performance-optimization-for-maximum-business-value
created: 2019-08-29T17:51:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- do-you-prioritize-performance-optimization-for-maximum-business-value

---

Like any development, performance optimization requires development time and should therefore be prioritized for business value.

Include the following considerations:

* What is the preferred performance for this feature?
* What represents an acceptable performance metric?
* How many users are expected to use this feature within a timeframe?
* What is the business impact of poor performance for this feature?
* Are we planning to significantly change this feature in the near future?


<!--endintro-->


::: greybox
Hi Adam,

As per our conversation, we have identified 2 slow queries:

Query 1: On the “Edit Item” screen (admin only) we have identified 4 separate SQL queries that can be rewritten as one. We estimate that this will reduce the response time by 1.5 seconds. Only a few admin users will be affected
Query 2: On the Home page is a query that currently takes 1 second that we can reduce to ½ a second. This affects all users.

We optimized the "Edit Item" page because that had the biggest measurable improvement.  
:::


::: bad
Bad example: although the admin page has a bigger potential saving, the home page affects all users and therefore probably has a higher business value. Business value should be determined by the Product Owner, not the developer


:::


::: greybox
Hi Adam,

As per our conversation, we have identified a query in the "Save Timesheet" endpoint that often takes more than 2 seconds to complete – well beyond the project’s 800ms target.
However, this entire feature is scheduled to be migrated from MVC to Angular in the next Sprint.

Recommended actions:
- We won't optimize the existing implementation
- Raise the priority of the Angular migration PBI
- Ensure that performance metrics are included in the acceptance criteria of the migration PBI

1.	Please “reply all” with changes or your acceptance.   
:::


::: good
Good example: there is little business value in optimizing code that will soon be replaced – but the final decision on business value is left to the Product Owner

:::

### Related Rules


* [Do you know where your goal posts are?](/where-your-goal-posts-are)
* [Do you avoid reviewing performance without metrics?](/do-you-avoid-reviewing-performance-without-metrics)
