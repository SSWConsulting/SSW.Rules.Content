---
seoDescription: TODO
type: rule
title: Do you know to choose the best software architecture?
uri: software-architecture-decision-tree
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
  - title: William Liebenberg
    url: https://ssw.com.au/people/william-liebenberg/
  - title: Luke Parker
    url: https://www.ssw.com.au/people/luke-parker
created: 2024-06-13
guid: TODO
---

A Modular Monolith is a software architecture pattern that combines elements of both monolithic and modular architectures. In this approach, the application is built as a single, unified codebase like a traditional monolith, but it is designed and organized in a modular manner, allowing for logical separation of different components or modules within the codebase.

<!--endintro-->

> The Modular Monolith architecture is the “goldilocks” approach that combines the modularity of microservices with the simplicity of traditional Monoliths
>
> - Steve “Ardalis” Smith

## Modular Monolith characteristics

![Figure: Modular Monolith architecture](modular-monolith.jpg)

- Single Host/Process
- Single Deployment
- Loosely coupled modules that each have their own
  - Domain
  - Application
  - Infrastructure
  - Presentation (API or UI)
- Each module represents a business capability or domain
- Each module should be as highly cohesive and loosely coupled with other modules
- Each module manages it's own data and persistence

### ✅ Advantages

- **Simplicity in Deployment** - Since it's a monolith, the deployment is typically simpler than distributed systems like microservices
- **Ease of Development** - Developers can work on separate modules without significantly affecting other parts of the application
- **Performance** - Inter-module communication is often faster and more reliable than inter-service communication in distributed architectures

### ❌ Challenges

- **Scalability** - While more scalable than a traditional monolith, it may not scale as effectively as microservices
- **Modular Discipline** - Maintaining strict modularity can be challenging as the application grows and evolves

A Modular Monolith offers a balance between the simplicity and coherence of a monolith and the modularity and maintainability of more distributed architectures. It is particularly useful for certain kinds of applications and organizational contexts.

### Modular Monolith compared to other architectures

| Trade-Offs  | Layered / CA | Microservices | Modular Monolith |
| ----------- | ------------ | ------------- | ---------------- |
| Modularity  | ❌           | ✅            | ✅               |
| Cost        | $            | $$$           | $                |
| Scalability | ❌           | ✅            | ❌               |
| Simplicity  | ✅           | ❌            | ✅               |
