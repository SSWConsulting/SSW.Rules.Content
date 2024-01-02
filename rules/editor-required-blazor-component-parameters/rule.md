---
type: rule
archivedreason:
title: Do you use the EditorRequired attribute for required parameters in Blazor?
guid: 125bf5aa-7b54-4aa3-8f71-8178af185afc
uri: editor-required-blazor-component-parameters
created: 2023-08-26T00:00:00.0000000Z
authors:
  - title: Matt Parker
    url: https://ssw.com.au/people/matt-parker
related: []
redirects: []
---

When you create a Blazor component, view parameters are marked with the `[Parameter]` attribute to indicate that they must be supplied by the parent component. By default, this is not enforced, which may lead to errors where you forget to pass in parameters where you use the component.

You should use the `[EditorRequired]` attribute to mark parameters that are required in your Blazor component.

<!--endintro-->

<br>

**TestComponent.razor**

```razor
<h3>@Name</h3>

@code {
    [Parameter]
    public string? Name { get; set; }
}
```
<br>

**Index.razor**

```razor
@page "/"

<PageTitle>Home</PageTitle>

<TestComponent />
```

::: bad  
Figure: Bad example - Developers could forget to pass a variable to the Name property

:::

<br>

**TestComponent.razor**

```razor
<h3>@Name</h3>

@code {
    [Parameter, EditorRequired]
    public string? Name { get; set; }
}
```

<br>

**Index.razor**

```razor
@page "/"

<PageTitle>Home</PageTitle>

<TestComponent />
```

::: good  
![Figure: Good example - The IDE warns developers if they forget the Name parameter](ide-warning.png)

:::

<br>

You should configure this warning (RZ2012) as an error so your IDE will fail to build if you are missing a required parameter. Add `<WarningsAsErrors>RZ2012</WarningsAsErrors>` to your Blazor .csproj file:

```xml
<Project Sdk="Microsoft.NET.Sdk.BlazorWebAssembly">
	<PropertyGroup>
		<TargetFramework>net7.0</TargetFramework>
		<Nullable>enable</Nullable>
		<ImplicitUsings>enable</ImplicitUsings>
		<WarningsAsErrors>RZ2012</WarningsAsErrors>
	</PropertyGroup>
</Project>
```

::: good
![Figure: Good example - Build fails with an error](build-error.png)

:::

### References

- [EditorRequired attribute vs C# required modifier](https://github.com/dotnet/aspnetcore/issues/44974)
