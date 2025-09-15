---
seoDescription: Learn the importance of encapsulating domain models in domain-driven design and how it leads to better maintainability and scalability.
type: rule
title: Do you encapsulate domain models in Domain-Driven Design?
uri: encapsulate-domain-models
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
created: 2024-06-13T13:42:55.753Z
guid: C490FD8A-EF45-46A8-BF91-14B24AA40AD3
---

Encapsulating domain models is a critical aspect of domain-driven design (DDD) that helps maintain the integrity and consistency of your application's core logic. Without proper encapsulation, the domain logic can become scattered and difficult to manage, leading to increased complexity and maintenance challenges.

<!--endintro-->

## Why encapsulate domain models?

When the domain model is not properly encapsulated, business rules and logic might be spread across various parts of the application, making it difficult to understand, maintain, and extend. Encapsulation ensures that the domain model is self-contained, with a clear and coherent structure.

## Key benefits of encapsulation

* **Maintains Integrity:** By keeping domain logic within the domain model, you ensure that all business rules (i.e. invariants) are enforced consistently
* **Improves Maintainability:** Encapsulated models are easier to understand and modify because all relevant logic is contained within the model itself
* **Enhances Testability:** Encapsulated domain models can be tested in isolation, improving the reliability of your tests
* **Promotes Clear Boundaries:** Encapsulation helps define clear boundaries between different parts of the system, adhering to the principles of bounded contexts

## Best practices for encapsulating domain models

1. **Use Aggregates:** Aggregates are clusters of domain objects that are treated as a single unit. Ensure that all changes to the domain model are done through aggregates. This means that Entities are not directly modified, but rather through the Aggregate Root

2. **Hide Internal State:** Keep the internal state of the domain model private and provide methods to interact with the state safely

3. **Encapsulate Collections:** Collections should be exposed as read-only interfaces to prevent external code from modifying the collection directly (e.g. using `IEnumerable<T>` or `IReadOnlyList<T>` instead of `List<T>`)

4. **Use Factory Methods:** Use factory methods to create instances of domain objects, ensuring that the object is always created in a valid state

5. **Use Value Objects:** Value objects are immutable objects that represent a concept in the domain. Use value objects to encapsulate domain concepts that are not entities

### Examples

```csharp
public class Order
{
    public required Guid CustomerId { get; set; }
    public OrderStatus OrderStatus { get; set; }
    public decimal PaidTotal { get; set; }

    public Customer? Customer { get; set; }
    public ICollection<OrderItem> Items { get; set; } = [];
}
```

::: bad
Figure: Bad example - Public setters, exposed collections, no constructor
:::

```csharp
    public class Order
    {
        public Guid Id { get; private set; }
        
        public Guid CustomerId { get; private set; }
    
        public OrderStatus OrderStatus { get; private set; }
    
        public Customer Customer { get; private set; } = null!;
    
        public decimal PaidTotal { get; private set; }
    
        private readonly List<OrderItem> _items = [];
    
        public IReadOnlyList<OrderItem> Items => _items.AsReadOnly();
    
        public static Order Create(CustomerId customerId)
        {
            Guard.Against.Null(customerId);
    
            var order = new Order()
            {
                Id = new OrderId(Guid.NewGuid()),
                CustomerId = customerId,
                OrderStatus = OrderStatus.New,
                PaidTotal = Money.Default
            };
    
            return order;
        }
    }
```

::: good
Figure: Good example - Private setters, read-only collection, factory method
:::
