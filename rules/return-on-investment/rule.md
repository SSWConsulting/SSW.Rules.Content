---
type: rule
title: Do you understand how Return on Investment (ROI) can affect decision making?
uri: return-on-investment
authors:
  - title: Josh Bandsma
    url: https://www.ssw.com.au/people/josh-bandsma
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - send-a-for-the-record-email-when-you-disagree
  - do-you-manage-up
  - do-you-estimate-business-value
created: 2021-08-18T06:46:14.461Z
guid: f994dab2-2982-45fa-afb1-72610bdd780a
---
When you are assigned a task, or come up with one yourself you might not consider all the factors that contribute to ROI. It is important to carefully consider the task and whether another solution providers better ROI. 

<!--endintro-->

If you find out that another solution would be better, then you should clearly communicate that to the Product Owner.

In the software world to calculate ROI we take a PBI and do [Business Value ÷ Effort](https://www.ssw.com.au/rules/do-you-estimate-business-value)

If the Product Owner still disagrees with you then it may be a good idea to [send a 'For the record' email](/send-a-for-the-record-email-when-you-disagree).

::: email-template
|          |     |
| -------- | --- |
| From:    | Piers |
| To:      | Bob Northwind |
| Subject: | Email signature - not working |  
::: email-content  

### Hi Bob,

Done - I have fixed the email signature by changing the file server's HTML and it took me 1 hour. 

Thanks!

Piers
:::
:::
::: bad
Figure: Bad Example - ROI was not mentioned
:::

::: email-template
|          |     |
| -------- | --- |
| From:    | Piers |
| To:      | Bob Northwind |
| Subject: | Email signature - not working |  
::: email-content 

### Hi Bob,

Done - I have fixed the email signature by changing the file server's HTML and it took me 1 hour. 

**ROI Consideration -** As per our conversation, for future changes to email signatures, let's wait until I implement the new 3rd party solution I am working on. This will give better ROI because I won't need to do any further wasted work.

Thanks!

Piers
:::
:::
::: good
Figure: Okay Example - ROI is mentioned
:::


::: email-template
|          |     |
| -------- | --- |
| From:    | Piers |
| To:      | Bob Northwind |
| Subject: | Email signature - not working |  
::: email-content 

### Hi Bob,

Done - I have fixed the email signature by changing the file server's HTML and it took me 1 hour, but I will have to do it for every user once a month. This adds up to 12 hours a month, at a cost of $200/hr, that's $2,400/month. Over a year that's $28,000.

Option B (recommended) Buy this email signature system for $2,000, I spend 2 days configuring it ($3,200), that's a total of $5,200 - so you save $24,800k and also get the results you want with zero effort or issues in the future.

Thanks!

Piers
:::
:::
::: good
Figure: Good Example - ROI is mentioned and quantified
:::

**Note:** If fixing the email signatures had been a huge task then it would have been better for Piers to have a conversation with Bob before he implemented the fix.