---
type: rule
title: Do you avoid using update?
uri: avoid-using-update
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:12:04.161Z
guid: d6698781-f047-48bf-93b9-7be2add4318f
---
The Update method on an entity in EF Core marks all of its fields as dirty. This will result in all the fields being written back to the database.

<!--endintro-->

Writing the entire record to the database can cause locking issues in the database server if there are foreign key relationships involving the entity being modified.

```
var entity = context
    .Products
    .FirstOrDefault(item => item.ProductID == id);
        
    if (entity != null)
    {
        entity.Name = "New name";    
        context.Products.Update(entity);
            
        context.SaveChanges();
    }
```

::: bad
Figure: Bad example - The whole record is written back to the database.
:::

```
var entity = context
    .Products
    .FirstOrDefault(item => item.ProductID == id);
        
    if (entity != null)
    {
        entity.Name = "New name";    
        context.SaveChanges();
    }
```

::: good
Figure: Good example - Only the modified fields are written back to the database.
:::