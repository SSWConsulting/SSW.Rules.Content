---
type: rule
title: Do you start reading code?
uri: do-you-start-reading-code
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
created: 2012-03-20T03:46:01.000Z
archivedreason: null
guid: 86eae955-ca88-429d-abde-70cc608f6ada
---

Great code isn't just about making computers do stuff; it's about making sure humans can understand and work with it too. Good code is like a well-written story - it's clear, easy to read, and everything has a name that makes sense. There's no unnecessary stuff thrown in, and it's all neatly organized. It's not just a set of instructions; it's a roadmap that explains not only "how" things work but also "why" they work that way when you read through it.

<!--endintro-->

> “Aim for simplicity. I want to code to read like poetry”*
> - Terje Sandstrom  

### Good code characteristics

* Is clear and easy to read
* Has consistent and meaningful names for everything
* Has no repeated or redundant code
* Has neat formatting
* Explains "why" when you read down, and "how" when you read left to right

```csharp
public IEnumerable<Customer> GetSupplierCustomersWithMoreThanZeroOrders(int supplierId) {
    var supplier = repository.Suppliers.Single(s => s.Id == supplierId);

    if (supplier == null) {
        return Enumerable.Empty<Customer>();
    }

    var customers = supplier.Customers
        .Where(c => c.Orders > 0);

    return customers;
}
```

**Figure: This code explains what it is doing as you read left to right, and why it is doing it when you read top to bottom**

::: greybox
**Tip:** Read the book [Clean Code: A Handbook of Agile Software Craftsmanship](https://www.amazon.com.au/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) by Robert. C. Martin.
:::

### Good code is declarative

For example, I want to show all the products where the unit price less than 20, and also how many products are in each category.

```csharp
Dictionary<string, ProductGroup> groups = new Dictionary<string, ProductGroup>();

foreach (var product in products) {
    if (product.UnitPrice >= 20)
    {
        if (!groups.ContainsKey(product.CategoryName))
        {
            ProductGroup productGroup = new ProductGroup();
            productGroup.CategoryName = product.CategoryName;
            productGroup.ProductCount = 0;
            groups[product.CategoryName] = productgroup;
        }
        groups[p.CategoryName].ProductCount++;
    }
}

var result = new List<ProductGroup>(groups.Values);

result.Sort(delegate(ProductGroup groupX, ProductGroup groupY) {
    return
        groupX.ProductCount > groupY.ProductCount ? -1 :
        groupX.ProductCount < groupY.ProductCount ? 1 :
        0;
});
```
::: bad
Figure: Bad example - Not using LINQ
:::

**Tip:** Resharper can automatically convert this code.

```csharp
result = products
    .Where(product => product.UnitPrice >= 20)
    .GroupBy(product => product.CategoryName)
    .OrderByDescending(group => group.Count())
    .Select(group => new { CategoryName = group.Key, ProductCount = group.Count() });
```
::: good
Figure: Good example - using LINQ
:::

**Tip:** For more information on why declarative programming (aka LINQ, SQL, HTML) is great, watch the TechDays 2010 Keynote by Anders Hejlsberg.Anders explains why it's better to have code "tell what, not how".

### Clean HTML 

Anyone who creates their own HTML pages today should aim to make their markup semantically correct. For more information on semantic markup, see [HTML Semantic Elements](https://www.w3schools.com/html/html5_semantic_elements.asp).

For example, `<p>` is for a paragraph, not for defining a section.

### Clean Front-End code

Clean code and consistent coding standards are not just for server-side code. It is important that you apply your coding standards to your front-end code as well e.g. JavaScript, TypeScript, React, Angular, Vue, CSS, etc.

You should use a linter and code formatter like Prettier to make development easier and more consistent.
