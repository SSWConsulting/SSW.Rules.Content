---
type: rule
title: Do you measure your Disaster Recovery downtime?
uri: do_you_measure_disaster_recovery_downtime
authors:
  - title: Warwick Leahy
created: 2021-10-11T00:20:18.145Z
guid: b6d36a20-a688-41f7-a378-7a76e896393d
---
At some time or another all businesses will experience a catastrophic incident.  At these times it is important to track the disaster, analyse the downtime and learn from the experience.

To do this it is important that you already have a few objectives established and you measure the actual results.  The objectives you would establish are RPO (Recovery Point Objective) and RTO (Recovery Time Objective) and the measurements that you take at the time of a disaster are RPA (Recovery Point Actual) and RTA (Recovery Time Actual).

It is important to practice your disaster recovery at least every 12 months so that you can be certain that you are investing in the minimum amount of resources that you require and so that you can be certain that your plan works.        

<!--endintro-->

**So what do these terms mean?**

![](93c56eff-8d11-4123-a2d6-1305911f07b0.jpg)


**Figure: RTO's vs RPO's**

**RPO**

RPO or Recovery Point Objective, is a measure of the maximum tolerable amount of data that the business can afford to lose during a disaster. It also helps you measure how long it can take between the last data backup and a disaster without seriously damaging your business. RPO is useful for determining how often to perform data backups.

**RTO**

RTO or Recovery Time Objective, is a measure of the amount of time after a disaster in which business operation is retaken, or resources are again available for use.  This measurement determines the amount of resources that are required for the recovery to happen within the timeframe required.

**RPA** 

RPA or Recovery Point Actual, is the actual measurement of the amount of data lost during a disaster recovery.

**RTA**

RTA or Recovery Time Actual, is the actual measurement of downtime during a disaster recovery.

It is important to note that these may all be different for different services.  For example at a bank you may have a transaction database, this may need to be only ever able to experience a RPA\RTA of a few minutes as even in that few minutes, thousands of transactions could be lost.  However the same bank may have a website that they are happy to have an RTA\RPA of several hours as this is much less critical to the banks overall operation.

**How to calculate these values?**

RTO and RPO is determined via consultation called a business impact analysis (BIA).  The organisation needs to work out what the maximum amount of data that they are prepared to lose and also the maximum amount of time that they are prepared to be without services.  These are both measured in time, and could be seconds, minutes, hours or days depending on the organisation's requirements.  This is a balancing act as generally the shorter the timeframe required, the more resources the organisation will need in order to achieve the target.  

After this a disaster should be simulated to test that the RTA/RPA values match the RTO/RPO required by the organisation.

For example recently Mr Bob Northwind experienced a major system failure.  The failure occurred at 8pm local time on a Friday night.