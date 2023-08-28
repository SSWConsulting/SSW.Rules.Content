---
type: rule
title: Do you seal your classes by default?
uri: seal-your-classes-by-default
authors:
  - title: Gordon Beeming
    url: /people/gordon-beeming
created: 2022-11-25T07:17:00.000Z
guid: 77F8E9B0-2BCB-4AFA-B022-3CFDD3B36C56
redirects:
- do-you-seal-your-classes-by-default
---

Traditionally you would only seal a class if you wanted to prevent it from being inherited. This is a good practice, but it's also a good practice to seal all classes by default and only unseal them when you need to inherit from them.
            
<!--endintro-->

On the surface it appears that you are just preventing someone from inheriting from your class, but there are a few other benefits to sealing your classes by default:

- Performance gains
- Only things that are designed to be inherited can be inheritable
- Inheritance can be easily abused and as a result is considered a minor anti-pattern
- Composition is preferred over inheritance

Watch this video by Nick Chapsas, to see the performance benefits of sealing your classes for different usage scenarios:

`youtube: https://www.youtube.com/embed/d76WWAD99Yo`
**Video: Why all your classes should be sealed by default in C# by Nick Chapsas (11 min)**
