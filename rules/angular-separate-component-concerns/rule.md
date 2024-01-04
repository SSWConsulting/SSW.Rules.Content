---
type: rule
title: Do you properly separate concerns in components?
guid: 77e033a8-1c84-431e-9ab8-53360a3968b0
uri: angular-separate-component-concerns
created: 2023-10-12T00:02:20.931Z
authors: 
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
related:
  - when-to-use-state-management-in-angular
  - isolate-your-logic-and-remove-dependencies-on-instances-of-objects
---

One common mistake in writing a front-end component is trying to fit everything in a single component. This can easily lead to unmaintainable code in the long run, especially for complex components.

<!--endintro-->

## Why should you separate the logic?
In simple components, having many logics (e.g. API calls and binding to the form) written to the component itself sometimes works okay, especially if the aim is to reduce the file footprint. However, doing this to larger-sized components can make maintaining the code challenging.  The last thing developers want to do is debug a component with 1000+ lines of code with intermingling logic.

Pros and cons of combining all logic into a single component:
- 🟢 Less file footprint
- 🟢 Easier to write
- 🟢 Less problem with reactivity
- ❌ No clear separation of logics
- ❌ Harder to debug when things go wrong
- ❌ Adding more features to this component can be challenging

Consider splitting your component's logic when:
- The file has reached 100+ lines of code
- The component has two or more sources of data (e.g. route params and API)
- UI has many fields that need to be populated from a data source
- When it is not clear which data source drives the UI or when you want to abstract it out


## How to separate the logic?

```ts
constructor(
  private route: ActivatedRoute,
  private apiService: ApiService,
) {}

ngOnInit() {
  this.route.params.pipe(
    takeUntil(this.ngDestroy$),
    switchMap(params => this.apiService.load1(params.id)),
  ).subscribe(response => {
    this.processApi(response);
  });
}

processApi(payload: ApiPayload1) {
  const calculatedData = this.calculate(payload);
  this.title = calculatedData.title;
  this.sumAmount = calculatedData.sum;
}

private calculate(...): ComponentData {
  // Calculate implementation
}
```
::: bad
Figure: Massive amount of code intermingling from API calls to calculation to UI binding
:::


Here are the steps to split the logic:
1. Group front-end logic into these processes:
    - Data fetching: fetching data from external sources
    - Data processing: processing source data to suit the UI better
    - Data display: binding the UI displayed element to a value

2. Identify which part of a smart component belongs to which process.

3. Use declarative code for UI data binding.

    Use `Observable` and `BehaviorSubject` (or [`Signal`](https://angular.io/guide/signals), but this is still in developer preview) to bind value to UI elements. This will help us remove the need to imperatively notify the UI to re-render when the source value has changed.

    ```ts
    calculatedData$ = new BehaviorSubject<CalculatedData | null>(null);

    constructor(
      private route: ActivatedRoute,
      private apiService: ApiService,
    ) {}

    ngOnInit() {
      this.route.params.pipe(
        takeUntil(this.ngDestroy$),
        switchMap(params => this.apiService.load1(params.id)),
      ).subscribe(response => {
        this.calculatedData$.next(this.calculate(payload));
      });

      // UI Binding logic
      this.calculatedData$.pipe(
        takeUntil(this.ngDestroy$),
      ).subscribe(calculatedData => {
        this.title = calculatedData.title;
        this.sumAmount = calculatedData.sum;
      });
    }

    private calculate(...): ComponentData {
      // Calculate implementation
    }
    ```
    ::: good
    Figure: Use declarative code to bind UI value
    :::

4. Split data display process.

    This gives the most benefit since having the view logic separate allows developers to easily swap out any UI elements, which is one of the frequent things to change in the front end.
    One approach is to create a sidecar service for this component.

    ```ts
    // ComponentService ================
    constructor(
      private apiService: ApiService,
    ) {}

    private _componentData$ = new BehaviourSubject<ComponentData|null>(null);
    public componentData$ = this._componentData$.asObservable();

    public initialiseComponentData(paramId: string): void {
      this.apiService.load1(params.id).subscribe(response => {
        this._componentData.next(this.calculate(payload));
      });
    }

    private calculate(...): ComponentData {
      // Calculate implementation
    }

    // Component ================
    constructor(
      private route: ActivatedRoute,
      private componentService: ComponentService,
    ) {}

    ngOnInit() {
      // API Fetching logic
      this.route.params.pipe(
        takeUntil(this.ngDestroy$),
      ).subscribe(params => {
        this.componentService.initialiseComponentData(params.id);
      });

      // UI Binding logic
      this.componentService.calculatedData$.pipe(
        takeUntil(this.ngDestroy$),
      ).subscribe(calculatedData => {
        this.title = calculatedData.title;
        this.sumAmount = calculatedData.sum;
      });
    }
    ```
    ::: good
    Figure: UI logic is separated from Data Fetching and Data Processing logic
    :::


5. (Optional) If the component is complex enough, consider splitting the data fetching with the data processing step to another component.

    In the example below, we create a parent component to handle the routing while providing the child component with the only necessary data.

    ```ts
    // ComponentService ================
    // ...Same implementation as above...

    // ParentComponent ================
    constructor(
      private route: ActivatedRoute,
      private componentService: ComponentService,
    ) {}
    
    ngOnInit() {
      // API Fetching logic
      this.route.params.pipe(
        takeUntil(this.ngDestroy$),
      ).subscribe(params => {
        this.componentService.initialiseComponentData(params.id);
      });
    }

    // Component ================
    constructor(
      private componentService: ComponentService,
    ) {}

    ngOnInit() {
      // UI Binding logic
      this.componentService.calculatedData$.pipe(
        takeUntil(this.ngDestroy$),
      ).subscribe(calculatedData => {
        this.title = calculatedData.title;
        this.sumAmount = calculatedData.sum;
      });
    }
    ```
    ::: good
    Figure: All logics (data fetching, data processing, and data display) are now separated
    :::