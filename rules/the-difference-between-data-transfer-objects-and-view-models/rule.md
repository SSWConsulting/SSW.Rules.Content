---
type: rule
archivedreason: 
title: Do you know the difference between data transfer objects and view models?
guid: 3b46e163-56d5-43e5-a035-8dbbcaa40e48
uri: the-difference-between-data-transfer-objects-and-view-models
created: 2019-04-15T21:58:44.0000000Z
authors:
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related:
  - use-mvvm-pattern
redirects:
- do-you-know-the-difference-between-data-transfer-objects-and-view-models

---

Data Transfer Objects (DTOs) and View Models (VMs) are similar concepts, but the terms are not interchangeable. To make matters more confusing the term `ViewModel` has a special meaning inside the [MVVM pattern](/use-mvvm-pattern).

Do you understand the subtle difference between these terms?

<!--endintro-->

## What is a DTO?

A DTO is a type that is used to move data from one part of an application to another. This could be between a command and a service, or between an API and a UI. Typically, a DTO represents an entity or other resource.

Unlike regular classes, a DTO only includes data - not behaviour.

```csharp
public class CarDto
{
  public int Id { get; set; }

  public int MakeId { get; set; }
  public string Make { get; set; }
  
  public int ModelId { get; set; }
  public string Model { get; set; }

  public int Year { get; set; }

  public bool IsInsurable()
  {
    return this.Year > DateTime.Now.AddYears(-25).Year; 
  }
}
```
::: bad
Bad example - A DTO that encapsulates data but also includes behaviour (or logic in this case)
:::


```csharp
public class CarDto
{
  public int Id { get; set; }

  public int MakeId { get; set; }
  public string Make { get; set; }
  
  public int ModelId { get; set; }
  public string Model { get; set; }

  public int Year { get; set; }
}
```
::: good
Good example - A DTO that encapsulates some data
:::

## What is a view model?

A view model (vm) is also a DTO, but it's a special kind of DTO. Rather than return data that corresponds to an entity or resource, it returns data that corresponds to a view. A view in this case is typically some part of a UI; although a view model could also be used to return a data structure that corresponds to the specific requirements of any part of an application. The distinction is that it represents the needs of the consumer, rather than the structure defined by the source.

This can be useful in situations where you have full control of both the consumer and provider. In a full-stack application this means both the UI and the API. In this case, you might have well-defined requirements for a view in the UI. Let's use a sales dashboard as an example; rather than have the dashboard make multiple calls to the API (say for the salespeople's names, their monthly figures, their targets, etc.), you can define a view model that returns all of the required data in one call.

## What is a ViewModel?

In the MVVM pattern, the term ViewModel (VM) (in PascalCase) has a special meaning. A ViewModel provides functionality and state for a view (in this case, this is explicitly part of a UI), and therefore _must_ contain logic as well as data. It also provides state, and acts as the glue between the UI (the View) and the service layer (the Model).

Learn more about the above concepts in the following Weekly Dev Tips podcasts:

·  [Data Transfer Objects (part 1)](https&#58;//www.weeklydevtips.com/008)

·  [Data Transfer Objects (part 2)](https&#58;//www.weeklydevtips.com/009)
