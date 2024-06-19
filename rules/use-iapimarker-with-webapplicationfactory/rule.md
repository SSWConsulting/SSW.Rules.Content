---
seoDescription: Do you use IApiMarker with WebApplicationFactory?
type: rule
title: Do you use IApiMarker with WebApplicationFactory?
uri: use-iapimarker-with-webapplicationfactory
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
created: 2022-11-25T07:17:00.000Z
guid: 81F456F4-689B-47CD-B4BF-883A7B423072
redirects:
  - do-you-use-iapimarker-with-webapplicationfactory
---

The `WebApplicationFactory` class is used for bootstrapping an application in memory for functional end to end tests. As part of the initialization of the factory you need to reference a type from the application project.

Typically in the past you'd want to use your `Startup` or `Program` classes, the introduction of top-level statements changes how you'd reference those types, so we pivot for consistency.

<!--endintro-->

Top level statements allows for a cleaner `Program` class, but it also means you can't reference it directly without some additional changes.

### Option 1 - Using InternalsVisibleTo attribute

::: bad
![Figure: Bad example - Using an InternalsVisibleTo attribute in the csproj](Using-InternalsVisibleTo-attribute.jpg)
:::

Adding the `InternalsVisibleTo` attribute to the csproj is a way that you'd be able to reference the `Program` class from your test project.

This small change leads to a long road of pain:

1. Your `WebApplicationFactory` needs to be internal
2. Which means you need to make your tests internal and
3. In turn add an `InternalsVisibleTo` tag to your test project for the test runner to be able to access the tests.

### Option 2 - public partial program class

::: bad
![Figure: Bad example - Using a public partial program class](Using-public-partial-program-class.jpg)
:::

A much quicker option to implement is to create a partial class of the `Program` class and make it public.

This approach means you don't need to do all the InternalsVisibleTo setup, but does mean you are adding extra none application code to your program file which is what top level statements is trying to avoid.

### Option 3 - Using an IApiMarker interface (recommended)

The `IApiMarker` interface is a simple interface that is used to reference the application project.

```cs
namespace RulesApi;

// This marker interface is required for functional testing using WebApplicationFactory.
// See https://www.ssw.com.au/rules/use-iapimarker-with-webapplicationfactory/
public interface IApiMarker
{
}
```

::: good
Figure: Good example - Using an `IApiMarker` interface
:::

Using the `IApiMarker` interface allows you reference your application project in a consistent way, the approach is the same when you use top level statements or standard Program.Main entry points.
