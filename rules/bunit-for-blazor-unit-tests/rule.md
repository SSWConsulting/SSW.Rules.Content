---
type: rule
archivedreason:
title: Do you use BUnit for unit tests in Blazor?
guid: 0d378d5a-c864-4655-8818-0dd1a744c2e6
uri: bunit-for-blazor-unit-tests
created: 2023-11-15T00:00:00.0000000Z
authors:
  - title: Matt Parker
    url: https://ssw.com.au/people/matt-parker
related: []
redirects: []
---

Unit testing is an essential part of the software development process, especially for Blazor applications. BUnit is a testing library specifically designed for Blazor components, making it easier to write robust unit tests. It is installed via a [NuGet package](https://www.nuget.org/packages/bunit) and can be used with any testing framework such as XUnit.

When you use BUnit, you can simulate user interactions and assert component behavior in a way that is close to how your users will interact with your application. This can significantly increase the reliability of your components.
<!--endintro-->

<br>

**ExampleComponent.razor**

```razor
<button class="incrementButton" @onclick="IncrementCount">Click me</button>
<p>Current count: @currentCount</p>

@code {
    public int currentCount = 0;

    public void IncrementCount()
    {
        currentCount++;
    }
}
```

<br>

**ExampleComponentTests.cs**

```csharp
using Bunit;
using Xunit;

public class ExampleComponentTests
{
    [Fact]
    public void ExampleComponent_ClickingButton_IncrementsCount()
    {
        // Arrange
        using var ctx = new TestContext();
        var cut = ctx.RenderComponent<ExampleComponent>();

        // Act
        cut.Find(".incrementButton").Click();

        // Assert
        cut.Instance.currentCount.ShouldBe(1);
    }
}
```
::: good
Figure: Good example - Using BUnit to test a Blazor component

:::
<br>

This is a very simple example, but the same concepts apply to more complex components. BUnit also provides a number of other features that make it easier to write unit tests for Blazor components, such as the ability to mock services and inject them into components.

Complex components such as complicated searching and filtering are good candidates for BUnit tests, to ensure that a component behaves as expected.

### References

- [BUnit: A testing library for Blazor components](https://bunit.dev/)
- [Microsoft Learn: Unit Testing Blazor Components with BUnit](https://learn.microsoft.com/en-us/aspnet/core/blazor/test?view=aspnetcore-7.0)
