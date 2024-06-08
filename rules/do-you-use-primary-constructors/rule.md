---
type: rule
archivedreason:
title: C# Code - Do you use primary constructors to keep your code clean?
guid: D400380F-30B1-4943-8983-4C95316CC40A
uri: do-you-use-primary-constructors
created: 2023-12-06T00:00:00.0000000Z
authors:
    - title: Daniel Mackay
      url: https://ssw.com.au/people/daniel-mackay
related: []
redirects:

---

When following best practices and using dependency injection, you will often find yourself with a class that has a lot of properties that are only set once, in the constructor.  This can lead to a lot of boilerplate code that is not needed.  C#12 introduces Primary Constructors, which allow you to define the constructor and the properties in one place.

<!--endintro-->

``` cs
public class Hero
{
    public Hero(string name, string power, string city)
    {
        _name = name;
        _power = power;
        _city = city;
    }

    private readonly string _name;
    private readonly string _power;
    private readonly string _city;

    public override string ToString() => $"{_name} has {_power} and lives in {_city}";
}
```
::: bad
Figure: Bad example - large amount of boiler plate code needed to store injected properties.  
:::

``` cs
public class Hero(string name, string power, string city)
{
    public override string ToString() => $"{name} has {power} and lives in {city}";
}
```
::: good
Figure: Good example - using Primary Constructors to reduce boilerplate code.
:::

In the example above we the `Hero` class has access to the parameters passed into the Primary Constructor so we don't need to store them in private fields.  We can use them directly in the `ToString()` method.

For more information on Primary Constructors see [learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/primary-constructors](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/primary-constructors)
