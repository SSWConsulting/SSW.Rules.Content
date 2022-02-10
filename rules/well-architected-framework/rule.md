---
type: rule
title: Do you use the Well-Architected Framework?
uri: well-architected-framework
authors:
  - title: Calum Simpson
    url: https://www.ssw.com.au/people/calum-simpson
related:
  - cloud-architect
  - the-goal-of-devops
created: 2022-02-10T07:49:50.377Z
guid: 16cd6da6-fbe3-4234-ae55-6281bccc5279
---
The Well-Architected Framework is a set of best practices which form a repeatable process for designing solution architecture, to help identify potential issues and optimize workloads.

![Figure: The Well-Architected Framework includes the five pillars of architectural excellence. Surrounding the Well-Architected Framework are six supporting elements](waf-diagram-revised.png)

<!--endintro-->

### The 5 Pillars

* **Reliability** – Handling and recovering from failures <https://docs.microsoft.com/en-us/azure/architecture/framework/resiliency/principles>
* **Cost Optimization** – Minimizing costs without impacting workload performance <https://docs.microsoft.com/en-us/azure/architecture/framework/cost/principles>
* **Performance Efficiency** **(Scalability)** – Testing, monitoring and adapting to changes in load e.g. new product launch, Black Friday sale, etc. <https://docs.microsoft.com/en-us/azure/architecture/framework/scalability/principles>
* **Security** – Protecting from threats and bad actors <https://docs.microsoft.com/en-us/azure/architecture/framework/security/security-principles>
* **Operational Excellence** **(DevOps)** – Deploying and managing workloads once deployed <https://docs.microsoft.com/en-us/azure/architecture/framework/devops/principles>

### Trade-offs

There are trade-offs to be made between these pillars. E.g. improving reliability by adding Azure regions and backup points will increase the cost.

### Why use it?

Thinking about architecting workloads can be hard – you need to think about many different issues and trade-offs, with varying contexts between them. WAF gives you a consistent process for approaching this to make sure nothing gets missed and all the variables are considered.

Just like Agile, this is intended to be applied for continuous improvement throughout development and not just an initial step when starting a new project. It is less about architecting the perfect workload and more about maintaining a well-architected state and an understanding of optimizations that could be implemented.

### What to do next?

[Assess your workload against the 5 Pillars of WAF with the Microsoft Azure Well-Architected Review](https://docs.microsoft.com/en-us/assessments/?mode=pre-assessment).
