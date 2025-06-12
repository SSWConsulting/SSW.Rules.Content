---
type: rule
seoDescription: Learn the best practices for generating API clients from OpenAPI specifications. Compare manual coding vs. NSwag, Refit, Kiota, and other tools for creating strongly-typed HTTP clients.
uri: generate-api-clients
title: Do you generate API clients?
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
related:
  - the-best-way-to-generate-your-entities-from-swagger
  - generate-interfaces-for-your-dtos
  - decouple-api-from-blazor-components
guid: a8f2e943-7c45-4e89-8f12-d3a7b6e8c9f2
---

When consuming APIs in your applications, you need to make HTTP requests and handle responses. You have several options for generating API clients, ranging from manual implementation to automated code generation from OpenAPI specifications.

<!--endintro-->

### Why generate API clients?

Generating API clients from OpenAPI specifications provides several key benefits:

* **Type safety** - Strongly-typed models prevent runtime errors
* **Reduced boilerplate** - Eliminates repetitive HTTP client code
* **Automatic updates** - Client stays in sync when API changes
* **Better developer experience** - IntelliSense and compile-time error checking
* **Consistency** - Standardized approach across your codebase

### Best practices
* **Automate generation** - Include client generation in your build pipeline
* **Separate generated code** - Keep generated clients in separate projects/folders
* **Don't modify generated code** - Use partial classes or wrapper services for customizations
* **Use dependency injection** - Register generated clients with your DI container

## API client generators

### Kiota ⭐ (Recommended)

<https://github.com/microsoft/kiota>

Kiota is Microsoft's next-generation API client generator designed for modern cloud APIs.

**How it works:** Generates fluent clients from OpenAPI specifications with focus on Microsoft Graph APIs and modern patterns.

✅ **Pros**
* Modern async/await patterns
* Supports complex API scenarios
* Growing ecosystem and active development
* Extendable - easy to add handlers to the client

❌ **Cons**
* Smaller community compared to alternatives
* Newer tool with fewer examples

### NSwag

<https://github.com/RicoSuter/NSwag>

NSwag generates strongly-typed C# and TypeScript clients from OpenAPI specifications.

**How it works:** Reads your OpenAPI/Swagger specification and generates complete client classes with methods, models, and error handling.

✅ **Pros**
* Generates C# and TypeScript clients
* Full-featured with extensive customization options
* Handles complex scenarios (inheritance, polymorphism)
* Strong tooling support (CLI, MSBuild, Visual Studio)

❌ **Cons**
* Needs configuration
* Can generate complex code for simple APIs
* Large generated files for big APIs

### Refit

<https://github.com/reactiveui/refit>

Refit generates HTTP client implementations from interface definitions using attributes.

**How it works:** You define interfaces with HTTP attributes, and Refit generates the implementation at runtime.

✅ **Pros**
* Simple attribute-based API definitions
* Lightweight and easy to learn
* Great integration with .NET dependency injection
* No code generation step required

❌ **Cons**
* REST HTTP only (no GraphQL, gRPC, etc.)
* Manual model definition required
* Runtime generation (no compile-time validation of endpoints)

### Manual Coding

Hand-writing HTTP client code for each API endpoint without any code generation.

✅ **Pros**
* Full control over implementation
* No external dependencies
* Simple

❌ **Cons**
* Time consuming and repetitive
* Error prone (typos, wrong URLs, etc.)
* No automatic updates when API changes
* Manual serialization/deserialization
* No compile-time validation
