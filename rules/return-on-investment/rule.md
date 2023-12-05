---
type: rule
title: Do you understand why Return on Investment (ROI) should affect decision making?
uri: return-on-investment
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
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

`youtube: https://www.youtube.com/embed/GEYDtxmX_8I`

An important part of communication is to improve the Product Owner's understanding of ROI and help them make good decisions. When you are actioning a task, it's crucial to value your time and think about how much manual time it may consume over a longer period, say a year. You can then go the extra step and quantify this $ cost.

<!--endintro-->

If you find out that another solution would be better, then you should clearly communicate that to the Product Owner.

In the software world to calculate ROI we take a PBI and do [Business Value ÷ Effort](/do-you-estimate-business-value)

If the Product Owner still disagrees with you then it may be a good idea to [send a 'For the record' email](/send-a-for-the-record-email-when-you-disagree).

::: email-template
|          |     |
| -------- | --- |
| From:    | Piers |
| To:      | Bob Northwind |
| Subject: | Email signature - not working |
::: email-content  

### Hi Bob

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

### Hi Bob

Done - I have fixed the email signature by changing the file server's HTML and it took me 1 hour.

**ROI Consideration -** As per our conversation, **I have to make these changes every month for 12 users**. Therefore, for future changes to email signatures, let's wait until I implement the new 3rd party solution I am working on. This will give better ROI because I won't need to do any further wasted work.

Thanks!

Piers
:::
:::
::: good
Figure: OK Example - ROI is mentioned
:::

::: email-template
|          |     |
| -------- | --- |
| From:    | Piers |
| To:      | Bob Northwind |
| Subject: | Email signature - not working |
::: email-content

### Hi Bob

Done - I have fixed the email signature by changing the file server's HTML and it took me 1 hour.

...**but I will have to do it for each of our 12 users once a month**.

The choices:

**Option A** - Continue manually adding each email signature, every month.

* Maintenance: SysAdmin x 12 hours x $200/hr = $2,400 per month
* Total cost = $28,800 per year

**Option B (recommended)** - Purchase and configure an email signature system.

* Configure: SysAdmin x 16 hours x $200/hr = $3,200 flat fee
* License: 1 License fee x $2,000 = $2,000 flat fee
* Total cost = $5,200 flat fee

Thanks!

Piers
:::
:::
::: good
Figure: Good Example - ROI is mentioned and quantified
:::

**Note:** If fixing the email signatures had been a huge task then it would have been better for Piers to have a conversation with Bob before he implemented the fix.
