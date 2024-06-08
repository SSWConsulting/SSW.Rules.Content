---
type: rule
title: Do you look for opportunities to use Linq?
uri: do-you-look-for-opportunities-to-use-linq
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
created: 2012-04-01T09:23:06.000Z
archivedreason: null
guid: 3e87484c-47eb-4c38-9a83-3e530fed7498
---

Linq is a fantastic addition to .Net which lets you write clear and beautiful declarative code. Linq allows you to focus more on the  **what** and less on the  **how** .

You should look for opportunities to replace your existing code with Linq.

<!--endintro-->

For example, replace your foreach loops with Linq.


```csharp
var lucrativeCustomers = new List<Customer>();

foreach (var customer in Customers)
{
    if (customer.Orders.Count > 0)
    {
        lucrativeCustomers.Add(customer);
    }
}
```

Figure: Bad Example - imperative programming using a foreach loop

```csharp
var lucrativeCustomers = Customers.Where(c => c.Orders.Count > 0).ToList();
```

Figure: Good Example - declarative programming using Linq
