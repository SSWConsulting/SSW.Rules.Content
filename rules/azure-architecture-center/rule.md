---
type: rule
title: Do you use Azure Architecture Center?
uri: azure-architecture-center
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
related:
  - well-architected-framework
  - cloud-architect
  - the-goal-of-devops
  - technical-debt
created: 2022-02-17T02:13:56.672Z
guid: 80f8f6e4-c332-4852-aef9-d2f7696b4a5a
---
In a Specification Review you should include an [architecture diagram](/architecture-diagram) so the client has a visual idea of the plan. There are lot of tools to help build out an architecture diagram, but the best one is [Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/)

It is a one stop shop for all things Azure Architecture. It’s got a library of reference implementations to get you started. Lots of information on best practices from the big decisions you need to make down to the little details that can make a huge difference to how your application behaves.

`youtube: https://www.youtube.com/watch?v=AhAz3BcXy0A`

**Video: Discovering the Azure Architecture Center | Azure Tips and Tricks (2 mins)**

## Reference Architectures

![Figure: Use Browse Architectures to find a reference architecture that matches your application](referencearchitectures.png)

The architectures presented fit into 2 broad categories:

* Complete end to end architectures. These architectures cover the full deployment of an application.
* Architectures of a particular feature. These architectures explain how to incorporate a particular element into your architecture. The Caching example above explains how you might add caching into your application to improve performance.

Each architecture comes with comprehensive documentation providing all the information you need to build and deploy the solution.

## Best Practices

![Figure: Use Explore Best Practices to find information on particular best practice](bestpractices.png)

The Best Practices is a very broad set of documentation from things like performance tuning all the way through to designing for resiliency and some of the more common types of applications and their requirements. Because of this there is almost always something useful, no matter what stage your application is at. Many teams will add a Sprint goal of looking at one best practise per Sprint or at regular intervals. The Product Owner would then help prioritise which areas should be focussed on first.
