---
type: rule
title: Do you avoid micro-culture jargon and insider terms?
seoDescription: Using a shortcut term that's well-understood within your team
  can seem like a powerful heuristic, but it requires specific insider knowledge
  that's at risk of being lost.
uri: avoid-micro-jargon
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related:
  - clear-meaningful-names
  - verbs-for-method-names
  - nouns-for-class-names
  - avoid-generic-names
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
created: 2024-11-05T00:00:00.000Z
archivedreason: null
guid: bf8b49d4-82f7-42fc-9e56-01076e6e5732
---

Code that relies on nicknames, abbreviations, or internal jokes can create unnecessary obstacles for new team members or future collaborators. Terms that only make sense to the “in-group” (like a specific project team or company department) can be hard to interpret, causing frustration and slowing down onboarding. Instead, favor widely understandable names or domain-specific terms that reflect a shared understanding of the business or domain.


<!--endintro-->

:::greybox
**How this differs from ubiquitous language**    
Using ubiquitous language (see our rule [Do you use ubiquitous language?](/ubiquitous-language)) is about naming concepts in ways that align with terms used by domain experts and stakeholders. While this might seem like micro-culture jargon at first glance, it’s different for an important reason. Unlike insider terms, ubiquitous language refers to widely recognized ideas within the domain, making code clearer for anyone familiar with the field. Avoid in-grouped terms that don’t convey meaning to people outside the team, even if they seem descriptive to those who are “in the know.”
:::


Imagine you’re working on a temperature regulation system and need functions to identify areas where the temperature has exceeded an upper or lower threshold. You write an enum to represent the state of an area that’s too hot or too cold:
```csharp
enum ThresholdBreachState
{
  Hoth,
  Mustafar
}
```
:::bad
These names are cool but require specific knowledge as well as context about the person who wrote them
:::

Now, this is actually pretty awesome, and if I saw this in your code, I’d probably buy you a beer. But realistically, this is too niche a description, and the mental leap required to connect the dots is burdensome.

A more universally understandable version would be:
```csharp
enum ThresholdBreachState
{
  MaxExceeded,
  MinExceeded
}
```
:::good
These names are _not_ cool, but they are meaningful and easy for any developer to understand
:::

Let’s say you have two developers on your team who are unusually tall and short, colloquially referred to as Big John and Little Dave. You’re working on code to compress and decompress messages entering and leaving a queue and name the methods `BigJohnify` and `LittleDavify`. Although the prefixes may hint at the methods’ functions, this requires a specific knowledge of the team dynamic and could easily lead to confusion.

```csharp
public byte[] BigJohnify(Stream input)
{
    //
}

public byte[] LittleDavify(Stream input)
{
    //
}
```
:::bad
You might think this is fun - John and Dave might even think so too - but the meaning here is completely unclear
:::

For instance, if nicknames are used ironically (think of “Little John” from Robin Hood), it’s possible that `LittleDavify` actually decompresses messages while `BigJohnify` compresses them. Did you spot the word "respectively" at the end of the first sentence? Anyone “in the know” might understand this, but it demands unique insider knowledge and risks being both unprofessional and confusing.


A far better method name pair would be `CompressMessage` and `DecompressMessage`. They are clear and concise to anyone reading the code, without the need for insider knowledge or the cognitive load of applying it.

```csharp
public byte[] Compress(Stream input)
{
    //
}

public byte[] Decompress(Stream input)
{
    //
}
```
:::good
These method names are much better - they instantly convey to anyone what they do
:::
