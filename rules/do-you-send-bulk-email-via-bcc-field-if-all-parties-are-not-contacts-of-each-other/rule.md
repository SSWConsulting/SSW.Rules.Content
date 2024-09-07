---
seoDescription: Send bulk emails via Bcc field to ensure privacy and protect recipients' email addresses from being shared.
type: rule
archivedreason:
title: Do you send bulk email via 'Bcc' field if all parties are not contacts of each other?
guid: a06057b7-d957-4df3-8794-a38d2be30a45
uri: do-you-send-bulk-email-via-bcc-field-if-all-parties-are-not-contacts-of-each-other
created: 2009-03-26T02:58:23.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
related: []
redirects:
  - do-you-send-bulk-email-via-bcc-field-(if-all-parties-are-not-contacts-of-each-other)
---

To ensure privacy, and not allow parties to get hold of each others' email addresses, emails to multiple parties should be entered in the 'Bcc' field (not the 'To' field).

<!--endintro-->

::: email-template  
| | |
| -------- | --- |
| To: | alex@aaa.com, @brandon@bbb.com, charlie@ccc.com, debora@ddd.com |
| Cc: | |
| Bcc: | |
| Subject: | Thank you for coming to Sydney .NET User Group |  
:::  
::: bad
Figure: Good Example - Send bulk email via 'To' field
:::

::: email-template  
| | |
| -------- | --- |
| To: | |
| Cc: | |
| Bcc: | alex@aaa.com, @brandon@bbb.com, charlie@ccc.com, debora@ddd.com |
| Subject: | Thank you for coming to Sydney .NET User Group |  
:::  
::: good
Figure: Good Example - Send bulk email via 'Bcc' field
:::
