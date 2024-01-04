---
type: rule
title: Do you understand what "testing" really means?
uri: what-testing-really-means
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-10-04T23:47:00.656Z
guid: e49fd41e-0790-42bb-b6e4-da3ed85d984c
---
Everyone thinks they know what "testing" is. Like most things, though, there isn't a shared understanding of what testing really means across the IT industry. 

Distinguishing "testing" and "checking" is a great way to help build this shared understanding when we're talking about this critical part of the software development process.

<!--endintro-->

### Common perceptions of "testing"

A commonly held view is that the purpose of testing is to detect non-conformances between a product and its specifications, so that they may be resolved. Specifications may exist on several levels and the concept of "verification" means checking a component against its immediate specification.

"Testing" is often conflated with "finding bugs" and we all know how easy it is to find bugs in the software we use every day:


> There's a reason that many people think testing is easy, due to an asymmetry. No one ever fired up a computer and stumbled into creating a slick UI or a sophisticated algorithm, but people stumble into bugs every day. Finding bugs is easy, they think. So testing must be easy.
>     - Michael Bolton

### Testing and checking

Let's dive into the definitions of ***testing*** and ***checking*** from James Bach and Michael Bolton (in [Testing and Checking Refined](https://www.satisfice.com/blog/archives/856)):

::: info
**Testing** is the process of evaluating a product by learning about it through experiencing, exploring, and experimenting, which includes to some degree: questioning, study, modeling, observation, inference, etc.

**Checking** is the process of making evaluations by applying algorithmic decision rules to specific observations of a product.
:::

Many people view "testing" as what is defined above as "checking". While checking particular facts about the product is important (e.g. checking that a  story meets its acceptance criteria), there is much more to good testing than just checking "known knowns" like this. (Notice how checking sounds like work that is amenable to automation).

As a good tester, we are tasked with evaluating a product by learning about it through exploration, experimentation, observation and inference. This requires us to adopt a curious, imaginative and critical thinking mindset, while we constantly make decisions about what’s interesting to investigate further and evaluate the opportunity cost of doing so. We look for inconsistencies by referring to descriptions of the product, claims about it and within the product itself. These are not easy things to do.

We study the product and build models of it to help us make conjectures and design useful experiments. We perform risk analysis, taking into account many different factors to generate a wealth of test ideas. This modelling and risk analysis work is far from easy.

We ask questions and provide information to help our stakeholders understand the product we've built so that they can decide if it’s the product they wanted. We identify important problems and inform our stakeholders about them – and this is information they sometimes don’t want to hear. Revealing problems (or what might be problems) in an environment generally focused on proving we built the right thing is not easy and requires emotional intelligence & great communication skills.

We choose, configure and use tools to help us with our work and to question the product in ways we’re incapable of (or inept at) as humans without the assistance of tools. We might also write some code (e.g. code developed specifically for the purpose of exercising other code or implementing algorithmic decision rules against specific observations of the product, “checks”), as well as working closely with developers to help them improve their own test code. Using tooling and test code appropriately is not easy.

This heady mix of aspects of art, science, sociology, psychology and more – requiring skills in technology, communication, experiment design, modelling, risk analysis, tooling and more – makes it clear why good software testing is hard to do!

### Testing is a learning process and provides valuable information about the product

Testing is an information service provider, helping stakeholders to make informed risk-based decisions about the software. The information produced by testing relies on learning, evaluation and experimentation, human skills that are not replaceable by machines (even the most sophisticated AI lacks the social context to be good at these kinds of activities).

You might want to check out Michael Bolton’s "Testing Rap" (from which some of the above was inspired) as a fun way to remind people about all the awesome things involved in really good testing!

`youtube: https://youtu.be/KePxuKpwqoI`
**Video: Michael Bolton's Hamilton Inspired Rap From TestBash Manchester (2 min)**
