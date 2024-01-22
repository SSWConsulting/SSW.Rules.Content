---
type: rule
title: Do you know the Modular Monolithic Architecture?
uri: modular-monoliths
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Luke Parker
    url: https://www.ssw.com.au/people/luke-parker
created: 2024-01-20T02:50:25.269Z
guid: 5213ed1f-8ae5-4631-9b76-e464d4011c17
---
A Modular Monolith is an architectural style in software development that emphasizes modularity within a monolithic application structure. 

<!--endintro-->

### Key aspects

1. **Monolithic Architecture** - Traditionally, a monolithic application is a single-tiered software application where different components are combined into a single project. This means all components of the application are interconnected and interdependent

2. **Modularity** - In a Modular Monolith, the application is still a monolith, but it's structured in a way that components or modules within it are highly modular. This modularity refers to dividing the application into distinct modules, each responsible for a specific piece of functionality. Eg. Invoicing
These modules are designed to be loosely coupled, meaning they interact with each other through well-defined interfaces and are largely independent in terms of development and deployment

3. **Use Cases* - It's often used in scenarios where an application is expected to be complex but not so large or varied that it requires a distributed architecture. It's also a good fit for teams transitioning from a monolithic architecture to microservices, as it offers a middle ground

#### ✅ Advantages

- **Simplicity in Deployment**: Since it's a monolith, the deployment is typically simpler than distributed systems like microservices
- **Ease of Development**: Developers can work on separate modules without significantly affecting other parts of the application
- **Performance**: Inter-module communication is often faster and more reliable than inter-service communication in distributed architectures

#### ❌ Challenges

- **Scalability**: While more scalable than a traditional monolith, it may not scale as effectively as microservices

- **Modular Discipline**: Maintaining strict modularity can be challenging as the application grows and evolves

A Modular Monolith offers a balance between the simplicity and coherence of a monolith and the modularity and maintainability of more distributed architectures. It is particularly useful for certain kinds of applications and organizational contexts. 
