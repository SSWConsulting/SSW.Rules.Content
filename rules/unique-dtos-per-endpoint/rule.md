---
seoDescription: Learn why creating unique DTOs for each API endpoint improves performance, reduces coupling, and leads to better maintainability in Clean Architecture.
type: rule
title: Do you use unique DTOs per use case?
guid: 19a53ef8-5b5c-4e44-baef-1433d4a77e48
uri: unique-dtos-per-endpoint
authors:
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related:
  - serialize-view-models-not-domain-entities
  - the-difference-between-data-transfer-objects-and-view-models
redirects: []
created: 2025-05-15T00:00:00.000Z
archivedreason: null
---

In Clean Architecture, it is normally better to have a unique Data Transfer Object (DTO) for each endpoint or use case.

While sharing DTOs across multiple endpoints might seem like a way to save some code, it often leads to several problems:

* **Unnecessary Data Transfer:** Endpoints sending more data than what is actually needed, this can lead to performance issues.
* **Increased Coupling:** When multiple endpoints share the same DTO, a change required by one endpoint can inadvertently affect others.
* **Developer Confusion:** Developers will find it hard to understand which properties are relevant for a specific endpoint, leading to potential misuse or misunderstanding of the data structure.

<!--endintro-->

By creating unique DTOs tailored to each endpoint's specific requirements, you ensure that:

* Endpoints only deal with the data they need.
* Performance is optimized by avoiding the transfer of superfluous data.
* Endpoints are decoupled, making them easier to develop, test, and maintain independently.

```csharp
namespace Northwind.Trading.Application.Contracts.Models;

public class OrderItemModel
{
    public int OrderId { get; set; } 
    public string CustomerId { get; set; }
    public DateTime OrderDate { get; set; }
    public decimal TotalAmount { get; set; }
    public OrderStatus Status { get; set; }

    /// <summary>
    /// Used for GetOrderListEndpoint. Ignore when updating
    /// </summary>
    public string? ShipFromCountry { get; set; }

    /// <summary>
    /// Used only for GetOrdersEndpoint. 
    /// </summary>
    public DateTimeOffset ModifiedDateUtc { get; set; }

    /// <summary>
    /// Detailed list of order items. Only for GetOrderDetails.
    /// Not used for GetOrderList
    /// </summary>
    public List<OrderItemViewModel> OrderItems { get; set; } = [];
}
```

::: bad
Figure: Bad example - `OrderViewModel` is used for multiple purposes (e.g., `GetOrderList`, `GetOrderDetails`, `CreateOrder`) and has accumulated many properties, making it hard to read and maintain.
:::

```csharp
namespace Northwind.Trading.Application.Contracts.OrderQueries.Models;

public class GetOrderListItemDto
{
    public int OrderId { get; set; }
    public string CustomerId { get; set; }
    public DateTime OrderDate { get; set; }
    public decimal TotalAmount { get; set; }
    public OrderStatus Status { get; set; }
}
```

::: good
Figure: Good example - A simple `OrderSummaryDto` designed specifically for an endpoint that lists orders.
:::
