---
seoDescription: Understand the differences between anemic and rich domain models to improve your software architecture.
type: rule
title: Do you understand the difference between anemic and rich domain models?
uri: anemic-vs-rich-domain-models
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
created: 2024-06-17T13:42:55.753Z
guid: 346475FF-7255-4BE2-BD09-C8113CA40399
---

When using Domain-Centric architectures such as Clean Architecture, we need to decide where the business logic will go. There are two main approaches to this: Anemic Domain Model and Rich Domain Model. Understanding the differences between these two models is crucial for making informed decisions about your software architecture.

<!--endintro-->

## Anemic Domain Model

An Anemic Domain Model is characterized by:

* **Property Bags:** Entities are simple data containers with public getters and setters
* **No Behavior:** No logic or validation within the entities

### Pros of Anemic Domain Model

* Good for simple or CRUD (Create, Read, Update and Delete) projects
* Easier to understand for developers new to the project

### Cons of Anemic Domain Model

* Doesn’t scale well with complexity - complex logic can be duplicated across many places in the client code
* Difficult to maintain as the project grows - changes to logic need to be updated in multiple places
* Less readable code - Code related to an entity is scattered across multiple places

::: greybox
class Order {
    public int Id { get; set; }
    public DateTime OrderDate { get; set; }
    public decimal TotalAmount { get; set; }
}
:::
Figure: Example - Anemic model where the Order class is just a data container with no behavior.
:::

## Rich Domain Model

A Rich Domain Model, on the other hand, embeds business logic in the model (within Aggegates/Entities/Value Objects/Services). This approach makes the domain the heart of your system, as opposed to being database or UI-centric.

A Rich Domain Model is characterized by:

* **Data and Behavior:** Combines data and behavior (business logic and validation) in the same entity
* **Encapsulation:** Entities are responsible for maintaining their own state and enforcing invariants

### Pros of Rich Domain Model

* Scales well with complexity - encapsulation (fundamental OOP principle) of the Domain model makes the calling client code simpler
* Easier to maintain - cohesion (fundamental OOP principle) of the Domain model means logic is closer to the data it applies to
* Encourages better testability - Domain model is easy to test in isolation

### Cons of Rich Domain Model

* Steeper learning curve
* May require more initial setup and design

::: greybox
class Order {
    public int Id { get; private set; }
    public DateTime OrderDate { get; private set; }
    public decimal TotalAmount { get; private set; }

    public Order(DateTime orderDate) {
        OrderDate = orderDate;
        TotalAmount = 0;
    }

    public void AddItem(decimal itemPrice) {
        if (itemPrice <= 0)
        {
            throw new ArgumentException("Item price must be greater than zero.");
        }

        TotalAmount += itemPrice;
    }
}
:::
Figure: Example - Rich model where the Order class encapsulates data and business logic.
:::

In both cases the Application is still responsible for communicating with external systems via abstractions implemented in the Infrastructure Layer.

## Choosing the Right Model

Projects with complex domains are much better suited to a Rich Domain model and Domain Driven Design (DDD) approach. DDD is not an all-or-nothing commitment; you can introduce the concepts gradually where they make sense in your application.

One side-effect of pushing logic into our Domain layer is that we can now start to write unit tests against our domain models. This is easy to do as our Domain is independent of our infrastructure or persistence layer.

### Tips for Transitioning to a Rich Domain Model

* **Start Small:** Introduce DDD concepts gradually
* **Focus on Key Areas:** Identify the most complex parts of your domain and refactor them first
* **Emphasize Testability:** Take advantage of the isolated domain model to write comprehensive unit tests
* **Iterate and Improve:** Continuously refine your domain model as the project evolves

By understanding the differences between anemic and rich domain models, you can make informed decisions about your software architecture and ensure that your project scales effectively with complexity.

## How does the Application Layer interact with the Model?

When using Clean Architecture we consider the Application Layer is part of the 'Core' of our system.  It needs to interact with the Domain Layer for the system to function.  This will happen in two slightly different ways depending on the underlying model.

1. **Anemic Domain Model**: Application Layer follows the 'Transaction Script' pattern. The Application will contain all logic in the system.  It will use the Domain Layer to update state, but will be in full control of the changes.  There is no logic in the Domain and the entities become 'Data Access Objects'.
2. **Rich Domain Model**:  Application Layer becomes the 'Orchestrator' of the Domain.  It is responsible for fetching the entities from the Persistence Layer, but will delegate to the Domain for any updates.  The Domain Layer will be responsible for maintaining the state of the system and enforcing invariants.
