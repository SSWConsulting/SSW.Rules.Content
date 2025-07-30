---
seoDescription: Generic names like "manager" are easy and can trick us into thinking they are good for consistency. But they can quickly undermine conveying the meaning of your code.
type: rule
archivedreason:
title: Do you avoid generic names like “manager” or "helper"?
uri: avoid-generic-names
created: 2024-11-05T00:00:00.0000000Z
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related:
  - clear-meaningful-names
  - verbs-for-method-names
  - nouns-for-class-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
guid: f0b473e1-c892-4a21-8319-68f56f713c0d
---

Generic names like “manager”, "helper", “processor”, “data”, and “info” are easy to reach for, but they tell us very little about a class or method’s true purpose. These words are catch-alls — they don’t communicate what the code actually does or what entity it represents. Avoiding these vague terms forces us to choose names that reflect a specific role or responsibility.

<!--endintro-->

## Why generic names are problematic

Words like "manager" and "processor" imply something that handles various tasks, which can make it tempting to pile unrelated responsibilities into one class. "Helper" makes this worse as it becomes a catch-all for a collection of disorganized functionality. Names like "data" or "info" are similarly ambiguous, as they could apply to nearly anything, from a database connection to a simple string.

Specific names are always preferable, as they make the code easier to understand and prevent code bloat from accumulating unrelated functionality.

:::greybox
Using **`OrderManager`** as a class to handle orders in an e-commerce system.
:::
:::bad
Bad example - While this name suggests that it might have something to do with orders, it doesn’t clarify how it interacts with them. Creating orders? Updating them? Processing payments? All of the above?
:::

:::greybox
Using **`OrderCreator`** for specifically creating orders  

Using **`ShippingOrderHandler`** or **`OrderShipmentService`** specifically handles only one aspect of the order - sending for shipment
:::
:::good
Good example - This name directly reflects its purpose, making it immediately clear what the class is responsible for
:::  

:::greybox
Using **`UserData`** for tracking the data for each user account.
:::
:::bad
Bad example - The name 'data' could mean just about anything
:::

:::greybox
Using **`UserOrderHistory`** requires no explanation!
:::
:::good
Good example - Immediately tells us the scope and purpose of the class
:::
