---
type: rule
title: Do you use these useful React Hooks?
uri: do-you-use-these-useful-react-hooks
authors:
  - title: Tom Bui
    url: https://ssw.com.au/people/tom-bui
  - title: Jack Pettit
    url: https://ssw.com.au/people/jack-pettit
related: []
redirects:
  - do-you-use-these-useful-react-hooks
created: 2023-06-13T17:13:53.000Z
archivedreason: null
guid: e14a52b3-31f8-43e5-a6e7-b3f8f0de28ed
---
React Hooks streamline state management and lifecycle processes in functional components, resulting in cleaner, more performant code. These are the most common and useful hooks that you should use in your React project:

<!--endintro-->

## 1. **useState**: Managing Local State 🧠

The `useState` hook lets you add state to functional components. Call `useState` at the top level of your component to declare one or more state variables.

```jsx
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      You pressed me {count} times
    </button>
  );
}
```
**Figure: Using useState for a counter component**

::: info
***Naming Convention***:
It's a common convention to name state variables using the pattern [**count**, **setCount**] with array destructuring.
:::

`useState` returns an array with exactly two items:

1. The current state of this state variable, initially set to the initial state you provided.
2. A function that lets you update its value.

### ✅ Recommended Usage

- **Updating Objects and Arrays**: Manage and adjust objects and arrays in the state. Remember, always create new references instead of mutating
- **Avoiding Recreating the Initial State**: Ensure the initial state is set only once, avoiding recalculations in subsequent renders
- **Resetting State with a Key**: Reset the component's state by altering its key
- **Storing Information from Previous Renders**: On rare occasions, adjust state as a reaction to a rendering process

### ⚠️ Pitfalls

- **State Updates**: A change in state doesn't instantly reflect within the current executing code. It determines what `useState` will return in future renders
- **Initializer Function**: When you pass a function to `useState`, it gets called only during the initialization phase
- **State Updates with Functions**: When deriving new state values from the previous state, it's better to use an updater function as an argument of the setter function instead of the new value i.e. `setObj(prev => { key: value ...prev }`. This ensures you're working with the most up-to-date state

Read more about `useState` on the [offical docs](https://react.dev/reference/react/useState)

## 2. **useEffect**: Side Effects & Lifecycles 🔄

In React functional components, **useEffect** serves as your toolkit to execute side effects, reminiscent of lifecycles in class-based components. Through dependencies, you can control when these effects run, granting granular control over side effect operations.

```jsx
import { useState, useEffect } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCount(c => c + 1); 
    }, 1000);
    return () => clearInterval(intervalId);
  }, []); 

  return <h1>{count}</h1>;
}
```
**Figure: useEffect Count example**

::: info
It's similar in concept to **Angular's** **ngOnChanges** lifecycle hook. While **ngOnChanges** in Angular detects and reacts to changes in input-bound properties, React's useEffect serves a broader purpose.
:::

### ✅ Recommended Usage

- **External System Connection**: Link React components to other systems like APIs, networks, or third-party libraries
- **Custom Hooks Encapsulation**: Nest your effect logic inside custom hooks for clarity and better structure
- **Non-React Widget Control**: Bridge the gap between React components and non-React widgets
- **Data Fetching**: While `useEffect` can fetch data, it's optimal to use the framework's standard mechanisms or custom hooks
- **Reactive Dependencies**: Identify reactive items (e.g., props, state) that influence your effect. When these alter, the effect kicks in again
- **State Updates**: Adjust state values referencing their former versions using `useEffect`
- **Access to Recent Props & State**: `useEffect` ensures the most recent props and state are at your disposal
- **Distinct Server/Client Content**: With effects operational solely on the client, you can orchestrate unique content for server and client views

### ⚠️ Pitfalls

- **Placement**: Ensure `useEffect` remains at the top level of your components/custom hooks. Bypass calling it within loops or conditionals
- **Avoid Overuse**: Turn to `useEffect` mainly for external synchronization
- **Strict Mode Nuances**: In strict mode, a preliminary setup+cleanup cycle, exclusive to development, verifies your cleanup's alignment with your setup
- **Dependencies Oversight**: If dependencies comprise inner-component objects or functions, they might trigger frequent effect repetitions
- **Visual Effects Caution**: A visual glitch before an effect suggests `useLayoutEffect` might be a better pick
- **Server Rendering**: `useEffect` is client-centric and doesn't engage during server-side rendering

Read more about `useEffect` on the [offical docs](https://react.dev/reference/react/useEffect)

## 3. **useContext**: Using Context Seamlessly 🌍

`useContext` is a pivotal React Hook, giving you the power to both read and subscribe to context values right within your component. 

```jsx
import { createContext, useContext } from 'react';

// Create a context
const ThemeContext = createContext({
  background: 'light',
  foreground: 'dark',
});

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return (
    <button style={{ background: theme.background, color: theme.foreground }}>
      I am styled by theme context!
    </button>
  );
}

export default function App() {
  return (
    <ThemeContext.Provider value={{ background: 'black', foreground: 'white' }}>
      <ThemedButton />
    </ThemeContext.Provider>
  );
}
```
**Figure: A Themed button example using useContext**


### ✅ Recommended Usage

- **Reading and Subscribing to Context**: Directly access and subscribe to context values straight from your component
- **Passing Data Deeply**: Bypass manual prop-drilling, letting you transmit data deeply through the component hierarchy
- **Updating Data Passed via Context**: Easily modify context values and integrate them with state for seamless updates across various components
- **Specifying a Fallback Default Value**: If no context provider is present upstream, `useContext` will resort to the default value established during context creation
- **Overriding Context**: For tailored requirements, override the context in specific parts of the component tree by enveloping it in a provider with a distinct value
- **Optimizing Re-renders**: Amplify performance when transferring objects or functions through context using techniques such as `useCallback` and `useMemo`

### ⚠️ Pitfalls

- **Provider Position**: The context search strategy employed by `useContext` is top-down, always eyeing the nearest provider. It disregards providers present in the invoking component
- **Re-rendering Children**: Context shifts compel React to re-render all child components stemming from the provider with a changed value. The assessment hinges on the `Object.is` comparison, meaning that even `memo` cannot fend off updates stemming from refreshed context values
- **Duplicate Modules**: Be wary of build systems churning out duplicate modules (e.g., due to symlinks). This can disintegrate context as both the provider and consumer must be the exact same object, passing the `===` comparison test
- **Provider Without a Value**: An absent value prop in a provider translates to `value={undefined}`. The default from `createContext(defaultValue)` comes into play only when there's a complete absence of a matching provider
- **Provider Cannot be Accessed**: If `useContext` is used in a component that is not wrapped by a provider, this can cause client-side errors as the value accessed will be null

Read more about `useContext` on the [offical docs](https://react.dev/reference/react/useContext)

## 4. **useRef**: Direct DOM Access & Persistent References 🎯

The `useRef`` hook in React allows you to access and interact with DOM elements or maintain a mutable reference to values across renders without triggering a re-render.

```jsx
import { useRef } from 'react';

function MyComponent() {
  const inputRef = useRef(null);

  function handleFocus() {
    inputRef.current.focus();
  }

  return (
    <>
      <input ref={inputRef} />
      <button onClick={handleFocus}>Focus the input</button>
    </>
  );
}
```
**Figure: On button click focus the input using useRef**

### ✅ Recommended Usage

- **Referencing a Value:** `useRef`` lets you reference a value that doesn't affect the rendering of your component
- **Manipulating the DOM:** By attaching the returned ref object as a ref attribute to a JSX node, React sets its current property to that DOM node, allowing direct DOM manipulations
- **Avoiding Recreating the Ref Contents:** React preserves the initial ref value and doesn't recreate it during subsequent renders. This is beneficial for computationally expensive values
- **Storing Information from Previous Renders:** Refs persist their data across renders and can store information that doesn’t initiate a re-render
- **Accessing Another Component's DOM Nodes:** With `React.forwardRef()`, you can expose refs of the DOM nodes inside custom components

### ⚠️ Pitfalls

- **Mutable current Property:** Although `ref.current`` is mutable, avoid mutating objects used in rendering
- **No Re-render on Change:** Adjusting ref.current doesn’t trigger a re-render; React doesn’t detect changes to the ref
- **Avoid Reading/Writing During Rendering:** Refrain from accessing or altering ref.current while rendering, except for its initialization
- **Strict Mode Double Render:** In strict mode, React may execute your component twice for side effect detection. This double execution results in the ref object being created twice, though one is discarded
- **Pure Component Behavior:** React assumes your component is a pure function. Interacting with a ref during rendering contradicts this presumption

Read more about `useRef` on the [offical docs](https://react.dev/reference/react/useRef)

## 5. **useReducer**: Advanced State Logic 📊

The `useReducer` is a React Hook that lets you add a reducer to your component, providing a more predictable state management method compared to useState.

```jsx
import React, { useReducer } from 'react';

function counterReducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
    </div>
  );
}
```
**Figure: React Counter Component Using useReducer**

### ✅ Recommended Usage

- **Adding a Reducer to a Component:** useReducer allows you to manage your component's state using a reducer function
- **Predictable State Updates:** Reducers specify how the state transitions from one state to the next, making state updates more predictable
- **Handling Complex State Logic:** It's suitable for managing state logic that's more complex than what useState can handle
- **Avoiding Recreating the Initial State:** React saves the initial state once and ignores it on subsequent renders. This is useful for values that are expensive to compute
- **Dispatching Actions:** Actions describe user interactions or events that trigger state changes. By convention, actions are objects with a type property
- **Batching State Updates:** React batches state updates, ensuring that the screen updates after all event handlers have run

### ⚠️ Pitfalls

- **State Mutations:** State in reducers should be treated as immutable. Avoid mutating state directly; always return new state objects
- **Incomplete State Updates:** Ensure that every branch in your reducer returns all parts of the state
- **Unexpected State Values:** If your state unexpectedly becomes undefined, it's likely due to missing state in one of the reducer cases or a mismatched action type
- **Too Many Re-renders:** This error typically indicates that you're unconditionally dispatching an action during render, leading to an infinite loop
- **Impure Reducers:** Reducers should be pure functions. Impurities can lead to unexpected behaviors, especially in strict mode where reducers might be called twice

Read more about `useReducer` on the [offical docs](https://react.dev/reference/react/useReducer)
