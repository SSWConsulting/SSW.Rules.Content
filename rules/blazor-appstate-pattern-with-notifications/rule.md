---
type: rule
title: State Management - Do you use the AppState pattern with State Change
  Notification?
uri: blazor-appstate-pattern-with-notifications
authors:
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
related:
  - blazor-basic-appstate-pattern
created: 2022-09-16T08:50:26.562Z
guid: efbed182-a72c-408e-93ec-f6ea26d366a1
---
Implementing the `INotifyPropertyChanged` interface is one of the most popular and .NET native approaches to notify other components of changes to a shared state object.

<!--endintro-->

Implementing the `INotifyPropertyChanged` interface allows listeners (other pages / components / classes) to be notified when the `PropertyChanged` event is invoked.

Listeners subscribe to the event by adding their own handling code to the `PropertyChanged` event.

In this example we made the `BaseState` class generic so that we can have a reusable abstraction that works for all types of state objects.

``` cs
public abstract class BaseState<T> : INotifyPropertyChanged
{
    private T _state;

    public BaseState(T initialState)
    {
        _state = initialState;
    }

    protected T State => _state;

    public event PropertyChangedEventHandler? PropertyChanged = null!;

    protected void OnPropertyChanged([CallerMemberName] string name = "")
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
    }
}
```

**Figure: Generic State object that implements `INotifyPropertyChanged` interface**

One of the main considerations with the `BaseState` abstraction is to keep the `T State` as a `protected` member and not expose it publicly. This restricts the possibility of external changes to our `T State`.

The next code snippet shows the `Counter` class which is a shared state object that is wrapped by the generic `BaseState<Counter>`. This enables us to notify listeners when the `Counter` state is explicitly changed.

The `CounterState` implementation will call the `OnPropertyChanged()` method whenever we explicitly changed the protected `Counter`.

``` cs
public class Counter
{
    public int Count { get; set; }
}

public class CounterState : BaseState<Counter>
{
    public CounterState() : base(
        new Counter()
        {
            Count = 0
        })
    {
    }

    public void Reset()
    {
        State.Count = 0;
        OnPropertyChanged();
    }

    public void Increment()
    {
        ++State.Count;
        OnPropertyChanged();
    }
}
```

**Figure: Implementation of the generic `BaseState<T>` object to notify listeners when the `Counter` object has been changed**

In order for us to inject our `CounterState` object into a page or component, we must register it as a service (typically in `Program.cs`).

``` cs
// register our CounterState object with a scoped lifetime
builder.Services.AddScoped<CounterState>();
```

**Figure: Registering `CounterState` so that it can be injected to a page or component**

The ideal time to add a state change handler is when the page/component is being initialized via `OnInitializedAsync()`.


```cs
protected override async Task OnInitializedAsync()
{
    _state.PropertyChanged += async (s, p) => await InvokeAsync(StateHasChanged);

    await base.OnInitializedAsync();
}
```

Once a property is changed, the `PropertyChanged` event will be invoked (by `BaseState<>`) and our custom handler code will be executed.

The Counter page example below calls `StateHasChanged()` when the `PropertyChanged` event is invoked to refresh the view to display the latest state. 

``` cs
@page "/counterWithPropertyChangeNotification"
@implements IDisposable

@* Inject our scoped CounterState and use it in the view / code section *@
@inject CounterState _state

<PageTitle>Counter with Observed State</PageTitle>

<p class="h2">Counter with Observed State</p>
<p class="mb-4">Current count: @_state.Value.Count</p>

@* Note: Due to user interaction, the page will refresh and show updated state value, even though we have not called StateHasChanged *@
<button type="button" class="btn btn-primary" @onclick="IncrementCount">Click me</button>
<button type="button" class="btn btn-warning" @onclick="Reset">Reset</button>

@code {

    protected override async Task OnInitializedAsync()
    {
        _state.PropertyChanged += async (s, p) => await InvokeAsync(StateHasChanged);

        await base.OnInitializedAsync();
    }

    public void Dispose()
    {
        _state.PropertyChanged -= async (s, p) => await InvokeAsync(StateHasChanged);
    }

    private void IncrementCount()
    {
        _state.Increment();
    }

    private void Reset()
    {
        _state.Reset();
    }
}

```

**Figure: Full example showing how to inject state, subscribe to state changes and how to unsubscribe from state changes**


**Note:** Remember to unsubscribe from the `PropertyChanged` event to avoid any memory leaks. See rule about [when to implement IDisposable](/when-to-implement-idisposable).

Whenever the `IncrementCount()` or `Reset()` methods are invoked, any listeners on the page will invoke the handling code attached to the `PropertyChanged` event - and be able to invoke `StateHasChanged` in order to update their respective views.

T﻿he real value of implementing `INotifyPropertyChanged` (or by using an abstraction like `BaseClass<T>` above) is when the same shared state object is used multiple times on the same page and having the `PropertyChanged` event handlers invoked from a single interaction and automatically keeping the view up to date for all components. 
