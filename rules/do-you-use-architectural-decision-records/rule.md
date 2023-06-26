---
type: rule
title: Do You Use Architectural Decision Records?
uri: do-you-use-architectural-decision-records
authors:
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
created: 2023-06-26T06:03:20.995Z
guid: a131455c-96db-4c0d-829c-20a506c1bcc8
---
Architectural Decision Records (ADRs) are lightweight documents use to record important decisions in your project.  They do not necessarily have to be related to architecture, but could be any important decision made by the team.

<!--endintro-->

## What are the advantages of using ADRs?

1. Providing documentation and historical context
2. Collaboration and communication
3. Informed Decision making
4. Decision re-evaluation
5. Avoiding blind acceptance or reversal

## Where should ADRs be stored?

They should be stored wherever the technical documentation for your project lives.  Storing them in Git along with your code works well, but alternatively where ever your technical documentation lives (i.e. a wiki).

## What Can I use to Create and Manage ADRs?

There are several tools available to help create and managed ADRs, but one of the best ones is [Log4Brains](https://github.com/thomvaill/log4brains).  Log4Brains can help to create and view ADRs.

This can be installed by running:

```bash
npm install -g log4brains
```

You can then initialize your git repo by running:


```bash
log4brains init
```


Which will guide you through a simple setup process.



To create a new ADR, run:



```bash
log4brains adr new
```

Lastly, to preview your ADRs, run:

```bash
log4brains preview
```

You can see an example of this in use in the [SSW.CleanArchitecture template](https://sswconsulting.github.io/SSW.CleanArchitecture/).