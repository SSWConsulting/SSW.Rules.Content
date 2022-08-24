---
type: rule
title: Do you know the importance of paying back technical debt?
uri: technical-debt
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: William Liebenberg
    url: https://ssw.com.au/people/william-liebenberg
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related:
  - refactor-your-code-and-keep-methods-short
  - well-architected-framework
redirects:
  - do-you-know-the-importance-of-paying-back-technical-debt
created: 2020-12-16T23:19:05.000Z
archivedreason: null
guid: de86d886-3341-43d0-a487-5e8b3cee3938
---
### What is Technical Debt?

Technical Debt is when you take a shortcut to get a feature in to get some feedback.

`youtube: https://www.youtube.com/embed/ASVD4YIOgpU`

<!--endintro-->

Code that is hard to understand after reading it multiple times or a single method that spans multiple screens is also considered to be Technical Debt.

Systems need to have features added to them to continually remain useful (or competitive).

As new features are added to the system, often more Technical Debt will be introduced.

**Example:** A developer takes a shortcut to get some early feedback on a new feature

* $100 - full feature
* $20 - feature with shortcuts (no tests, dirty code, whatever it takes)
* $80 - IOU via PBI in the backlog e.g. \[FeatureName] – Tech Debt - Planned

::: good
![Figure: Good example - Tech Debt is very visible to the Product Owner](waf-tech-debt-backlog-northwind.png)
:::

### What are the consequences of Technical Debt?

* Fewer features overtime for the customers
* More molasses (developer friction) for the developers

`youtube: https://www.youtube.com/embed/0FlLE8AdZgk`

### The 2 types of Technical Debt

#### 1. Planned Technical Debt

Sometimes you do want to quickly implement a new feature to get it out and receive some feedback.

::: greybox
PBI: **\[FeatureName] – Tech Debt - Planned** 
:::

**Note:** Martin Fowler calls this "Deliberate Technical Debt".

#### 2. Discovered Technical Debt

During a code review, you or the team notice something as part of the system that is clearly Technical Debt. This code is hindering the ability to add new features or is hard to read/understand.

::: greybox
PBI: **\[FeatureName] – Tech Debt - Discovered** 
:::

**Note:** Martin Fowler calls this "Inadvertent Technical Debt".

### How to repay Technical Debt

Just like a business that receives pre-payment from customers, a software team should be reviewing the size of their liabilities (being the list of PBIs with Technical Debt).

At the Sprint Planning:

1. Show the Product Owner the list of outstanding Technical Debt PBIs
2. The Product Owner should make sure that the developers review the list of Technical Debt list and pick at least 1 PBI to pay back during the upcoming sprint

### Screenshots

![Figure: Screenshot of code with tech debt comment and link to GitHub issue](techdebt-github.png)

![Figure: Screenshot of tech debt on backlog](techdebt-backlog.png)

![Figure: SugarLearning architecture diagram](techdebt-architecture.png)
