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

Up to this point, whether we realize it or not, we've been building an Anemic Domain Model. In an Anemic Domain Model, our entities are simple property bags with no behavior. Instead of having a Rich Domain layer, we have ended up with a Simple Data Access layer.

We've also been using a pattern called a Transaction Script. In this pattern, we have a single class that handles all the logic for a given transaction.

For simple projects or projects only requiring CRUD functionality, this is fine. However, for more complex projects, this can lead to a lot of complexity in the Application layer, and a lot of duplication of logic.

<!--endintro-->

### Anemic Domain Model

An anemic domain model is characterized by:

* **Property Bags:** Entities are simple data containers with getters and setters.
* **No Behavior:** No logic or validation within the entities.
* **Transaction Scripts:** Organizes business logic by procedures where each procedure handles a single request and transaction from the presentation layer.

#### Pros of Anemic Domain Model:
- Good for simple or CRUD projects.
- Easier to understand for developers new to the project.

#### Cons of Anemic Domain Model:
- Doesn’t scale well with complexity.
- Logic duplication across the application.
- Difficult to maintain as the project grows.

::: greybox
class Order {
public int Id { get; set; }
public DateTime OrderDate { get; set; }
public decimal TotalAmount { get; set; }
}
:::
::: bad
Figure: Bad Example - Anemic model where the Order class is just a data container with no behavior.
:::

### Rich Domain Model

A rich domain model, on the other hand, embeds business logic within the entities. This approach makes the domain the heart of your system, as opposed to being database or UI-centric.

#### Key Characteristics:
- **Data and Behavior:** Combines data and behavior (business logic and validation) in the same entity.
- **Isolation from Infrastructure:** The domain model is isolated from infrastructure concerns.
- **Scales well with complexity:** Better suited for projects with complex domains.
- **Easily Testable:** Business logic is easier to test due to its encapsulation within the domain model.

#### Pros of Rich Domain Model:
- Scales well with complexity.
- Promotes encapsulation and cohesion.
- Easier to maintain and extend.
- Encourages better testability.

#### Cons of Rich Domain Model:
- Steeper learning curve.
- May require more initial setup and design.

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
        if (itemPrice <= 0) throw new ArgumentException("Item price must be greater than zero.");
        TotalAmount += itemPrice;
    }
}
:::
::: good
Figure: Good Example - Rich model where the Order class encapsulates data and business logic.
:::

### Choosing the Right Model

Projects with complex domains are much better suited to a Domain Driven Design (DDD) approach. DDD is not an all-or-nothing commitment; you can introduce the concepts gradually where they make sense in your application.

One side-effect of pushing logic into our Domain layer is that we can now start to write unit tests against our domain models. This is easy to do as our Domain is independent of our infrastructure or persistence layer.

#### Tips for Transitioning to a Rich Domain Model:
- **Start Small:** Introduce DDD concepts gradually.
- **Focus on Key Areas:** Identify the most complex parts of your domain and refactor them first.
- **Emphasize Testability:** Take advantage of the isolated domain model to write comprehensive unit tests.
- **Iterate and Improve:** Continuously refine your domain model as the project evolves.

By understanding the differences between anemic and rich domain models, you can make informed decisions about your software architecture and ensure that your project scales effectively with complexity.
