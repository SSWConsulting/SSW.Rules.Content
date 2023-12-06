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

Domain Events and Integration Events are a concept primarily found in Domain-Driven Design (DDD) that can be applied in various other architectural patterns such as [Clean Architecture](https://github.com/sswconsulting/SSW.CleanArchitecture).

Domain Events and Integration Events are powerful patterns improve decoupling and facilitate communication between different components of an application. They serve as a means of **notification** for important domain concepts that have occurred.

<!--endintro-->

In [Clean Architecture](https://github.com/sswconsulting/SSW.CleanArchitecture), Domain Events can be employed to enhance the communication between the `Domain` layer and other outer layers, such as the `Application` layer or `Infrastructure` layer. By raising Domain Events within the `Domain` layer, we achieve loose coupling between different parts of the application while ensuring that the domain layer remains independent of other concerns.

For an example implementation of DDD Domain and Integration events with Clean Architecture, check out this [example project](https://github.com/william-liebenberg/CleanArchitectureWithDomainEvents).

Here's a brief overview of how Domain Events fit into Clean Architecture:

`Domain` Layer: The domain layer, as discussed earlier, contains the domain model and business logic. When a significant event occurs within the domain, the relevant domain entity can raise a domain event without being concerned about what happens next.

`Application` Layer: The application layer, which orchestrates the flow of the application, is responsible for subscribing to Domain Events raised by the domain layer. When a domain event is raised, the application layer can react to it by initiating additional processes or triggering other actions in response to the event.

`Infrastructure` Layer: The infrastructure layer is responsible for implementing the actual event handling mechanisms. It provides the infrastructure to publish and subscribe to Domain Events, and it ensures that the events are properly handled and dispatched to interested parties, such as external systems or other services.

## What are Domain Events

Domain Events are an integral part of the Domain Model.

Domain Events are immutable and can be considered as **historical facts** capturing something that occurred in the Domain process. They are meant to be a representation of past events and cannot be altered or disputed.

Domain Events are raised within the `Domain` Layer of your application when an entity or aggregate makes a significant decision or undergoes a state change. The main purpose of Domain Events is to enable loose coupling and keep domain logic isolated from the application's infrastructure.

For example, when an `Order` is placed, a domain event can be raised (e.g. `OrderReceivedEvent`) to notify other parts of the domain that need to react to this event, such as updating inventory or sending confirmation emails.

Another example could be when the `Order`'s `Status` changes from `OrderStatus.Received` to `OrderStatus.Processing`, we can publish an `OrderStatusChanged` event.

Domain Events should not depend on external dependencies or external systems, adhering to the principles of the Domain Layer.

When publishing a domain event, the entire Entity or Aggregate can be included since the event's scope is confined to the current bounded context.

::: greybox
It is important to remember that the definition and behavior of a `Product` in one bounded context might differ from another bounded context, like an e-commerce application product versus the product of a chemical reaction in a laboratory.
:::

In the `Application` Layer, Domain Events are typically in-process of the application. Any database side-effects are tracked as part of the current transaction of the original request, ensuring strong consistency in the response sent back to the user once the transaction is committed.

## What are Integration Events

Integration Events are used for communication between different bounded contexts (or microservices in a distributed system) and enable potentially long-running asynchronous operations like sending a large number of emails, generating thumbnail images, or performing additional business logic.

It is recommended that Integration Events should only be raised from the `Application` layer when the need for communication or coordination between different parts of the application arises. For example, after a specific use case (command / query) is handled successfully, the `Application` layer might raise an Integration Event to notify other microservices or external systems about the outcome of that use case.

::: bad
If there is a strict domain requirement for Integration Events to be raised from the `Domain` layer then you need to be aware that you may inadvertently introduce coupling between domain logic and infrastructure concerns which could lead to violating one of the core principles of Clean Architecture ([Dependency Inversion Principle](/the-main-principles-of-clean-architecture/#principles))
:::

Integration Events are published **after** the original transaction completes and are typically dispatched through a Message Broker or Event Bus (e.g., [Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-queues-topics-subscriptions), [RabbitMQ](https://www.rabbitmq.com/), [Redis PubSub](https://redis.io/docs/interact/pubsub/), [Dapr PubSub](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-overview/)). To ensure reliability and consistency, systems often implement mechanisms like a [Transactional Outbox](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transactional-outbox-cosmos#solution).

## Naming Events

When describing Domain or Integration Events, we commonly use a past-tense naming convention, such as `OrderCreated`, `UserRegistered`, `InvoiceConsolidated`.

It's essential to identify suitable events as not everything qualifies as an important event. For instance, "client walked into the store" or "chicken crossed the road" may not be appropriate for a Domain Event.

## When to use Domain vs Integration Events

Use Domain Events within the `Domain` layer to decouple domain-specific logic and enable better maintainability and testability within the core of your application.

Use Integration Events (preferably from the `Application` layer) when you need to communicate and coordinate between different parts of an application or distributed system (such as microservices), to achieve eventual consistency and loose coupling among services.
