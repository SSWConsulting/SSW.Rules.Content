---
type: rule
title: Do you know how to manage compatibility between different Target Framework Monikers (TFMs)?
uri: manage-compatibility-for-different-tfms
authors:
  - title: Yazhi Chen
    url: https://www.ssw.com.au/people/yazhi-chen
created: 2023-09-01T01:39:10.755Z
guid: 05a2bdf2-d173-4c46-a700-b2b3b83408e2
---
Migrating your project to a new Target Framework Moniker (TFM) can be a complex task, especially when you're dealing with compatibility issues between different Target Framework Monikers (TFMs). It is suggested to handle your migration PBIs (Product Backlog Items) collectively and transition your main branch to the new TFM. Making this judgment call requires careful consideration of factors like the number of PBIs and their estimated completion time.

Here are some essential tips for managing changes that are not compatible with both the old and new TFMs:

<!--endintro-->

### Using #if Pragma Statements

You can use #if pragma statements to compile code exclusively for a specific TFM. This technique also simplifies the removal process during post-migration cleanup, especially for incompatible code segments.

Whenever possible, consider using dependency injection or factory patterns to inject the appropriate implementation based on the TFM you are targeting. This approach promotes code flexibility and maintainability, as it abstracts away TFM-specific details.

```cs
public static class WebClientFactory
{
  public static IWebClient GetWebClient()
  {
#if NET472
    return new CustomWebClient();
#else
    return new CustomHttpClient();
#endif
  }
}
```

::: good
Code: Good example - Using #if Pragma statements and factory pattern
:::

### Using MSBuild conditions

You can use MSBuild conditions to add references to different libraries that are only compatible with a specific TFM. This enables you to manage references dynamically based on the TFM in use.

```cs
<ItemGroup Condition="'$(TargetFramework)' == 'net472'">
    <Reference Include="System.Web" />
    <Reference Include="System.Web.Extensions" />
    <Reference Include="System.Web.ApplicationServices" />
</ItemGroup>
```

::: good
Code: Good example - Using MSBuild conditions
:::
