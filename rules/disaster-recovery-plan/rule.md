---
type: rule
title: Do you have a disaster recovery plan?
uri: disaster-recovery-plan
authors:
  - title: Warwick Leahy
    url: https://www.ssw.com.au/people/warwick-leahy
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kiki

created: 2021-10-11T00:20:18.145Z
guid: 0668c3fd-3946-42cc-8712-80a46712162d
---
At some point every business will experience a catastrophic incident. At these times it is important to have a plan that explains who to contact, the priority of restore and how to restore services.

At the time of a disaster, you should have a few objectives established and measure some results - The objectives are **RPO** (Recovery Point Objective) and **RTO** (Recovery Time Objective); and the measurements to take are **RPA** (Recovery Point Actual) and **RTA** (Recovery Time Actual).

It's recommended to practice your disaster recovery at least once every 12 months. This way you make sure that you are investing in the minimum amount of required resources, and that your plan actually works.

<!--endintro-->

### So what do these terms mean?

![Figure: RTO's vs RPO's](93c56eff-8d11-4123-a2d6-1305911f07b0.jpg)

#### RPO

RPO or Recovery Point Objective, is a measure of the maximum tolerable amount of data that the business can afford to lose during a disaster. It also helps you measure how long it can take between the last data backup and a disaster without seriously damaging your business. RPO is useful for determining how often to perform data backups.

#### RTO

RTO or Recovery Time Objective, is a measure of the amount of time after a disaster in which business operation is retaken, or resources are again available for use.  This measurement determines the amount of resources that are required for the recovery to happen within the timeframe required.

#### RPA

RPA or Recovery Point Actual, is the actual measurement of the amount of data lost during a disaster recovery.

#### RTA

RTA or Recovery Time Actual, is the actual measurement of downtime during a disaster recovery.

::: info
**Note:** these may all be different for different services. For example at a bank you may have a transaction database, this may need to be only ever able to experience a RPA\RTA of a few minutes as even in that few minutes, thousands of transactions could be lost. However the same bank may have a website that they are happy to have an RTA\RPA of several hours as this is much less critical to the banks overall operation.
:::

### How to calculate these values?\*\*

RTO and RPO are determined via a consultation called BIA (Business Impact Analysis). The organization needs to work out what the maximum amount of data that they are prepared to lose and also the maximum amount of time that they are prepared to be without services. These are both measured in time, and could be seconds, minutes, hours or days depending on the organization's requirements. This is a balancing act as generally the shorter the timeframe required, the more resources the organisation will need in order to achieve the target.  

After this a disaster should be simulated to test that the RTA/RPA values match the RTO/RPO required by the organization.

- - -

**Example:** Mr Bob Northwind experienced a catastrophic incident. The failure occurred at 8pm local time on a Friday night. Their website and sales transaction software were affected.

In his Disaster Recovery Plan he had the following objectives:

| Service           | RPO     | RTO     |
| ----------------- | ------- | ------- |
| Northwind Website | 2 days  | 4 hours |
| North Sales       | 4 hours | 8 hours |

::::info

It is important that these objectives are signed off by the Product Owner as per [this rule](/do-you-ask-clients-to-initial-your-work)

::::

After the recovery was complete they then analyzed the downtime which showed the following:

| Service           | RPA     | RTA     |
| ----------------- | ------- | ------- |
| Northwind Website | 8 hours | 2 days  |
| North Sales       | 8 hours | 8 hours |

After analyzing the data, they discovered a few issues with their Disaster Recovery Plan:

1. They didn't have any spare hardware on premises which meant that to get the website backed up and running they needed to find a shop on a weekend to buy a server and then start the recovery process. This delayed them by an entire day.

2. Mr Northwind's IT Manager had mistakenly set the backups to 12-hour backups (at midnight and midday each day). This meant that the most recent backup for both services had occurred at 12pm on Friday and they had 8 hours of missing transactions. The greatest allowable data loss should have only been 4 hours.

**This explains why it is important to practice your disaster recovery plan.** A real incident is not the ideal time to realize that your backup/procedures are inadequate.
