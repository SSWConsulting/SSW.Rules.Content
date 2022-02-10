---
type: rule
title: Do you change message size restrictions in Exchange Online?
uri: change-message-size-restrictions-exchange-online
authors:
  - title: Chris Schultz
related:
  - do-you-avoid-huge-images-or-attachments-in-your-email
created: 2022-02-09T23:16:53.094Z
guid: 867eba1d-ddf7-452c-bf13-1735a5a3b123
---
The default message size limit in Exchange Online is 25MB. Even though email attachments are not the best way to share a large file, sometimes it is the only option - and these days, 25MB is quite small. This default limit should be increased; it is easy to do so from the Exchange admin center, or with PowerShell.

<!--endintro-->

It is important to remember that the maximum email attachment size will also depend on the person receiving the email - their email service will need to accept the larger size. For example, Gmail's default limit is also 25MB.

### Changing the default in Exchange admin center

1. Go to **Exchange admin center | Recipients | Mailboxes | Set default message size restrictions**