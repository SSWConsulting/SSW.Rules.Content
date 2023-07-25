---
type: rule
title: Do you know when to use Domain and Integration Events?
guid: e91f22d2-d385-49b6-a27b-1195b4bb13f9
uri: when-to-use-domain-and-integration-events
created: 2023-07-25T11:01:35.0000000Z
authors:
- title: William Liebenberg
  url: https://ssw.com.au/people/william-liebenberg
archivedreason:
related: []
redirects:
---

Domain Events and Integration Events are powerful patterns used in Domain-Driven Design (DDD) to enable loosely coupled communication between different parts of an application. They serve as a means of **notification** for important domain concepts that have occurred.

<!--endintro-->

## What are Domain Events

In the Domain Layer of the [Clean Architecture](https://github.com/sswconsulting/SSW.CleanArchitecture), Domain Events are an integral part of the Domain Model.

Domain Events are raised within the Domain Layer of your application when an entity or aggregate makes a significant decision or undergoes a state change. The main purpose of Domain Events is to enable loose coupling and keep domain logic isolated from the application's infrastructure.

For example, when an `Order` is placed, a domain event can be raised (e.g. `OrderReceivedEvent`) to notify other parts of the domain that need to react to this event, such as updating inventory or sending confirmation emails.

Another example could be when the `Order`'s `Status` changes from `OrderStatus.Received` to `OrderStatus.Processing`, we can publish an `OrderStatusChanged` event.

It's essential to identify suitable events as not everything qualifies as a Domain Event. For instance, "client walked into the store" or "chicken crossed the road" may not be appropriate for a Domain Event.

Domain events are immutable and can be considered as **historical facts** capturing something that occurred in the domain process. They are meant to be a representation of past events and cannot be altered or disputed.

When describing domain events, we commonly use a past-tense naming convention, such as `OrderCreated`, `UserRegistered`, `InvoiceConsolidated`.

Domain events should not depend on external dependencies or external systems, adhering to the principles of the Domain Layer.

When publishing a domain event, the entire Entity or Aggregate can be included since the event's scope is confined to the current bounded context.

Note: It is important to remember that the definition and behavior of a `Product` in one bounded context might differ from another bounded context, like an e-commerce application product versus the product of a chemical reaction in a laboratory.

In the `Application` Layer, domain events are typically handled synchronously. Any database side-effects are tracked as part of the current transaction of the original request, ensuring strong consistency in the response sent back to the user once the transaction is committed.

## What are Integration Events

Integration Events are used for communication between different bounded contexts (or microservices in a distributed system) and enable potentially long-running asynchronous operations like sending large number of emails, generating thumbnail images, or performing additional business logic.

In terms of Clean Architecture, Integration Events can be published from both the `Domain` and `Application` layers depending on the requirements of the applications.

Integration Events can be raised from the `Application` layer when the need for communication or coordination between different parts of the application arises. For example, after a specific use case (command / query) is handled successfully, the `Application` layer might raise an Integration Event to notify other microservices or external systems about the outcome of that use case.

These events are usually published **after** the original transaction completes and are typically dispatched through a Message Broker or Event Bus (e.g., Azure Service Bus, RabbitMQ, Redis PubSub). To ensure reliability and consistency, systems often implement mechanisms like a Transactional Outbox.

Ultimately, the decision on whether to raise Integration Events from the `Application` layer or the `Domain` layer depends on the specific design and requirements of the application. However, it is essential to ensure that raising Integration Events from the `Domain` layer doesn't lead to tight coupling between the domain logic and the infrastructure concerns. If raising Integration Events from the `Domain` layer is chosen, it's good practice to use an abstraction to decouple the domain entities from the actual event handling mechanisms, ensuring a clean separation of concerns.

## When to use Domain vs Integration Events

Use Domain Events within the `Domain` layer to decouple domain-specific logic and enable better maintainability and testability within the core of your application.

Use Integration Events (preferably from the `Application` layer) when you need to communicate and coordinate between different parts of an application or distributed system (such as microservices), to achieve eventual consistency and loose coupling among services.
