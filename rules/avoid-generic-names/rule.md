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
related:
  - clear-meaningful-names
  - verbs-for-method-names
  - nouns-for-class-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - when-to-use-technical-names
  - avoid-using-your-name-in-client-code
  - use-meadningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
guid: f0b473e1-c892-4a21-8319-68f56f713c0d
---

Generic names like “manager,” “processor,” “data,” and “info” are easy to reach for, but they tell us very little about a class or method’s true purpose. These words are catch-alls — they don’t communicate what the code actually does or what entity it represents. Avoiding these vague terms forces us to choose names that reflect a specific role or responsibility.


<!--endintro-->

## Why generic names are problematic
Words like "manager" and "processor" imply something that handles various tasks, which can make it tempting to pile unrelated responsibilities into one class. Names like "data" or "info" are similarly ambiguous, as they could apply to nearly anything, from a database connection to a simple string. Specific names are always preferable, as they make the code easier to understand and prevent code bloat from accumulating unrelated functionality.

:::bad
Imagine you’re writing a class to handle orders in an e-commerce system. You name it `OrderManager`. While this name suggests that it might have something to do with orders, it doesn’t clarify how it interacts with them. Is it creating orders, updating them, processing payments, or all of the above? The generic term “manager” gives us no clear indication.
:::

:::good
A better name could be `OrderProcessor`, but if the class specifically handles only one aspect — say, sending orders for shipment — a more precise name would be `ShippingOrderHandler` or `OrderShipmentService`. This name directly reflects its purpose, making it immediately clear what the class is responsible for.
:::

:::bad
Let’s say you’re building a system to track medical records, and you create a class called `PatientData`. The name could apply to anything — health information, appointment history, test results. There’s no way to tell what role this class actually plays.
:::

:::good
If the class is responsible for managing a patient’s appointment history, a more accurate name could be `PatientAppointmentHistory`. This name immediately tells us the scope and purpose of the class without relying on catch-all terms.
:::
