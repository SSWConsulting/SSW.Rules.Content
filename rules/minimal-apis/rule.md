---
type: rule
title: Do you use Minimal APIs over Controllers?
uri: minimal-apis
authors:
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
  - title: William Liebenberg
    url: https://ssw.com.au/people/william-liebenberg
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
related: []
redirects: []
created: 2023-12-01T02:55:57.0000000Z
archivedreason: null
guid: 300ef178-e0b9-43bb-bb92-3076253005b1
---

Traditional controllers require a lot of boilerplate code to set up and configure. Most of the time your endpoints will be simple and just point to a mediator handler.

Minimal APIs are a simplified approach for building fast HTTP APIs with ASP.NET Core. You can build fully functioning REST endpoints with minimal code and configuration. Skip traditional scaffolding and avoid unnecessary controllers by fluently declaring API routes and actions.

Check out the Microsoft Docs for more information on [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis).

<!--endintro-->

```csharp
[ApiController]
[Route("[controller]")]
public class HelloWorldController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok("Hello World!");
    }
}
```
::: bad
Figure: Bad Example - 9 lines of code for a simple endpoint
:::

```csharp
app.MapGet("/", () => "Hello World!");
```
::: good
Figure: Good Example - 1 line of code for a simple endpoint
:::

Minimal APIs are great for
- Learning
- Quick prototypes
- Vertical Slice Architecture
- A similar developer experience to NodeJS
- Performance
