---
type: rule
title: Do you check your AD security with PingCastle?
uri: check-ad-security-with-pingcastle
authors:
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
created: 2022-05-04T01:17:40.642Z
guid: 4fefa162-1bc8-431d-8e8c-24033d7ec148
---
> "Active directory is quickly becoming a critical failure point in any big sized company, as it is both complex and costly to secure..." - PingCastle

[PingCastle](https://www.pingcastle.com/) is an Active Directory auditing tool. It checks your accounts, computers and configuration in AD and gives you a great report on things that should be addressed. It is a tool that should be run periodically - we do it every 3 months - to keep AD secure.

<!--endintro-->

PingCastle is easy to install and run - see [their documentation](https://www.pingcastle.com/documentation/) for more information. It is free to use in your own environment, or there are paid versions for MSPs and larger enterprises.

![Figure: PingCastle report](pingcastle.png)

Once you have run it, you get a great report on your Active Directory security health, with detailed recommendations of what you need to fix.

![Figure: Example item from PingCastle, with detailed description and solution](pingcastle2.png)