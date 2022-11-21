---
type: rule
title: State Management - Do you use the AppState pattern?
uri: blazor-basic-appstate-pattern
authors:
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
related:
  - blazor-appstate-pattern-with-notifications
created: 2022-09-16T08:40:45.591Z
guid: 1dc53cdd-5c19-414b-8275-c6c8dcfc030e

---

The **AppState** pattern is one of the simplest **State Management** patterns to implement with Blazor WebAssembly.

<!--endintro-->

To start implementing the pattern, declare a class that describes the collection of fields that represents the state of a page, a form, or a model.

Here are some basic example state objects:

```cs
public class Counter
{
    public int Counter { get; set; }
}

public class RegistrationForm
{
    public Guid FormId { get; set; }
    public string EmailAddress { get; set; }
    public string GivenName { get; set; }
    public string Surname { get; set; }
    public string JobTitle { get; set; }
}

public class TimesheetEntry
{
    public int Id { get; set; }
    public int ClientId { get; set; }
    public string ClientName { get; set; }
    public int ProjectId { get; set; }
    public string ProjectName { get; set; }
    public decimal HourlyRate { get; set; }
    public DateTime StartTime { get; set; }
    public DateTime EndTime { get; set; }
    public string Notes { get; set; }
}

public class Timesheet
{
    public int Id { get; set; }
    public string UserName { get; set; }
    public TimesheetEntry[] Entries { get; set; }
}
```

Typically, these state objects would be hydrated from user input or a request to the backend API. In order for us to use this state object, we first need to register it as an injectable service (in `Program.cs`):


```cs
builder.Services.AddScoped<Counter>();
builder.Services.AddScoped<RegistrationForm>();
builder.Services.AddScoped<Timesheet>();
```

Once registered, we can use the `@inject` directive to inject the object into a page or component:

```cshtml
@page "/counterWithState"

@* Inject our CounterState and use it in the view and/or code section *@
@inject Counter _state

<PageTitle>Counter</PageTitle>

@* we can reference the state object in the Razor markup *@
<p>Current count: @_state.Count</p>

@* Note: Due to user interaction, the page will refresh and show updated state value, even though we have not called StateHasChanged *@
<button type="button" @onclick="IncrementCount">Click me</button>
<button type="button" @onclick="Reset">Reset</button>

@code {

    private void IncrementCount()
    {
        // we can modify the state object in the @code section
        ++_state.Count;
    }

    private void Reset()
    {
        _state.Count = 0;
    }
}
```

Alternatively if we are using code-behind (separate .razor and .razor.cs files), then we can use the `[Inject]` attribute to inject the object as a parameter for the code-behind class.

::: info
**Note:** Constructor based injection is not supported for Blazor code-behind. Only Parameter based injection is supported.
:::

```cs
public partial class Counter : ComponentBase
{
    [Inject]
    public Counter State { get; set; }

    private void IncrementCount()
    {
        ++_state.Count;
    }

    private void Reset()
    {
        _state.Count = 0;
    }
}
```


### Drawbacks of basic AppState pattern

❌ We are unable to react to state changes made to the state object by other components

❌ We can modify the state but the page will not refresh to reflect the change

❌ We need to call `StateHasChanged()` manually when we modify the state


### Benefits of basic AppState pattern

✅ Implementation is trivial - register, inject, consume

✅ Works for very basic scenarios - especially if there are basic user interactions and basic state mutations directly on the `@code` (aka `ViewModel`) section  
