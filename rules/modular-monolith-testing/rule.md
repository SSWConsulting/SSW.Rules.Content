---
seoDescription: Learn the best testing strategies for modular monoliths, focusing on effective unit, integration, and workflow testing.
type: rule
title: Do you know how effectively test Modular Monoliths?
uri: modular-monolith-testing
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
created: 2024-11-13T17:00:00.000Z
guid: A3DF3BDF-C0FA-4615-8EC9-F42EA85755CD
---

In modular monolith applications, establishing a strong testing strategy is essential to ensure robust functionality and maintainable code across multiple modules. Modular monoliths often centralize domain logic, require clear interactions across module boundaries, and should provide cohesive end-to-end workflows. Implementing a well-structured testing strategy will help catch errors early, validate integrations, and prevent issues from arising in production.

<!--endintro-->

There are 3 main testing strategies that can be used to effectively test modular monoliths:

1. Unit Testing
2. Integration Testing
3. Workflow Testing

## Unit Testing

Unit testing is critical in a modular monolith to validate the core business rules and domain logic within individual modules. Effective unit tests ensure that each module functions as expected, enabling:

* **Verification of isolated business logic** within each module, such as validation rules or calculations.
* **Maintenance of a clean, well-defined contract** for each module’s internal methods.

::: greybox
Ensure each module’s domain logic has comprehensive unit tests that cover typical and edge cases.
:::
::: good
Figure: Good Example - Unit tests confirm the integrity of domain logic in isolation from external dependencies.
:::

## Integration Testing

Integration testing in modular monoliths is one of the highest-value forms of testing, as it verifies that modules interact as intended with infrastructure such as databases, and that modules also communicate correctly together. This is essential since a failure in module interactions can lead to complex issues in production.

A reliable integration testing approach involves:

* **Testing interactions between modules** to ensure data is handled and processed correctly across boundaries.
* **Simulating database and service dependencies** to validate that modules function cohesively in a realistic environment.

There are several strategies that can make integration tests even more effective:

1. **Do not mock (where possible)** - Mocking can lead to false positives and hide issues that only occur when modules interact. It also makes tests more brittle and harder to maintain.
2. **Use a real database** - Using a real database in integration tests can uncover issues that would not be caught with an in-memory database.
3. **Isolate test infrastructure** - If the modular monolith uses multiple databases, an isolated set of databases should be used for each modules tests. This ensures that inter-module communication is tested correctly without interference from other module tests.

Integration tests allow teams to identify and resolve issues that occur only when modules interact, which can be challenging to catch with unit tests alone.

## Implement Workflow Tests for Full End-to-End Scenarios

Workflow (or end-to-end) tests are invaluable in modular monoliths as they cover the application’s key business flows from start to finish. These tests simulate real user actions across multiple modules and validate that all components work together to produce the expected outcomes. This type of testing should be focused on:

* **Simulating critical application workflows** that span multiple modules, such as user registration, order processing, or data retrieval.
* **Ensuring that each step in the workflow** completes successfully and transitions correctly to the next, providing a realistic assessment of application stability.

While workflow tests are the most complex and resource-intensive, they provide confidence that major application processes are functioning correctly and as intended.

::: greybox
Design workflow tests that cover the main paths users take, ensuring all modules work together to deliver expected end results.
:::
::: good
Figure: Good Example - Workflow tests simulate full user journeys, giving comprehensive validation of the application’s functionality.
:::

By incorporating unit, integration, and workflow tests, teams can ensure that modular monoliths remain reliable, maintainable, and scalable. An effective testing strategy with these layers will provide better insights into system functionality and facilitate easier troubleshooting and faster development cycles.
