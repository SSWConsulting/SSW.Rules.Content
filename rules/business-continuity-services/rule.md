---
type: rule
title: Redundancy - Do you ensure the business continuity of your services?
uri: business-continuity-services
authors:
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kiki
related:
  - azure-site-recovery
  - rules-to-better-backups
created: 2021-10-14T05:29:39.921Z
guid: a93c7265-c1d1-43c0-9dc3-21ccd7532f4e
---
Business continuity is present in any good disaster recovery plan and means that when your services (e.g. websites, hardware, software) fail or suffer an outage, you have measures in place to ensure downtime is minimal.        

<!--endintro-->

Before diving further, some terms need to be understood to fully understand the concept of business continuity: Redundancy, High Availability, Fault Tolerance and Disaster Recovery. These are concepts used to ensure that a system has as little downtime as possible, by applying different strategies or actions in case of a fault. 

### Redundancy

Redundancy is a base concept that is applied to all other concepts e.g. High Availability and Fault Tolerance. Redundancy mainly means having extra hardware or software that can be used as backup (or in tandem) with the primary one e.g. having 2 virtual machines, one on-premises and one in Azure. When one fails, the other one can be used as the backup.

There are many ways to automate or apply redundancy, check the below for more information.

### High Availability (HA)

A high available system is one that is designed to be up and available as much as possible. Generally, this means that a secondary system, mirror of the primary, is also up and running at the same time as the primary, and if the primary system goes down, the secondary takes over as soon as it sees a fault in the first one - ensuring the system is online. Swapping to the secondary system might take a bit of time, and that adds to the time the system is down.

This can be applied in many levels and layers, e.g.:

1. Hardware - Two (or more) UPS on different electrical circuits powering the same servers
2. Hardware - Two (or more) virtual machine hosts available for the same set of virtual machines
3. Hardware - Two (or more) Firewalls working on an active-passive state
4. Software - Two (or more) webservers behind a load balancer

For HA, one of the key points is having a system that redirects workloads in case of a failure - without that, you might have a redundant system, but not necessarily high available.



This takes the downtime from days to hours - or even less - due to the services being synced or replicated constantly in a secondary location. This secondary location can even be in the same physical place.

It's always a good idea to have redundancy on-premises and also in an off-premises (e.g. Azure) location, so in cases of any location disasters, you can rest assured your data and services are not affected.

A good example of business continuity tools is Azure Site Recovery, which you can find more about here: https://www.ssw.com.au/rules/azure-site-recovery

Backups are also important in your business continuity and disaster recovery plan, check out our other rules for backups: https://www.ssw.com.au/rules/rules-to-better-backups

![Figure: Good Example - It's crucial to add a redundancy plan to your disaster recovery plan](redundancy2.png)