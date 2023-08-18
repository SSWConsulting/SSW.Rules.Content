---
type: rule
archivedreason: 
title: Do you use these useful React Hooks?
guid: e14a52b3-31f8-43e5-a6e7-b3f8f0de28ed
uri: do-you-use-these-useful-react-hooks
created: 2023-06-13T17:13:53.0000000Z
authors:
- title: Tom Bui
  url: https://ssw.com.au/people/tom-bui
related: []
redirects:
- do-you-use-these-useful-react-hooks

---

React Hook is an extremely useful feature in React that makes managing state a lot easier in functional components. Hooks enable you to handle state, side effects, and component lifecycle within functional components, promoting code reusability, better organization, and improved performance in React applications. These are the most common and useful hooks that you should use in your React project:

<!--endintro-->

1. `useState` Hook

    `useState` is the most used and practical hook that is used for managing and updating states within a functional component. It takes an initial state value as an argument and returns an array containing two elements: the current state value and a function to update that value.
    
    ``` javascript
    import React, { useState } from 'react';
    
    function Counter() {
      const [count, setCount] = useState(0);
    
      return (
        <div>
          <p>You clicked {count} times</p>
          <button onClick={() => setCount(count + 1)}>
            Click me
          </button>
        </div>
      );
    }
    ```
    
    In this example, useState is used to declare a state variable count with an initial value of 0. setCount is a function that updates the count state value when the button is clicked. When the button is clicked, the onClick event calls the setCount function with the new value of count + 1, which updates the state value and re-renders the component with the new state value displayed in the p tag.

2. `useEffect` Hook

    `useEffect` is used to perform side effects in functional components, similar to `ngOnChanges` in **Angular** that listens to state changes, such as fetching data from an API or updating a title. It takes two arguments: a function that performs the side effect, and an optional array of dependencies that specify when the effect should be re-run (If second argument not provided, the effect will run on every re-render of the component). 
    
    ``` javascript
    import React, { useState, useEffect } from 'react';
    
    function Example() {
      const [count, setCount] = useState(0);
    
      useEffect(() => {
        document.title = `You clicked ${count} times`;
      }, [count]);
    
      return (
        <div>
          <p>You clicked {count} times</p>
          <button onClick={() => setCount(count + 1)}>
            Click me
          </button>
        </div>
      );
    }
    ```
    
    In this example, useEffect is used to update the document title with the current count value whenever count changes. The useEffect hook takes a function that updates the document.title property with the current count value, and an array of dependencies that includes count. This means that the effect will only be re-run if the count state value changes.

3. `useContext` Hook

    useContext is a React Hook that allows you to consume a context in a functional component. Context provides a way to pass data through the component tree without having to pass props down manually at every level.
    
    ``` javascript
    import React, { useContext } from 'react';
    
    // Create a context
    const ThemeContext = React.createContext('light');
    
    // Create a component that uses the context
    function ThemedButton() {
      const theme = useContext(ThemeContext);
      return (
        <button style={{ background: theme.background, color: theme.foreground }}>
          I am styled by theme context!
        </button>
      );
    }
    
    // Create a component that provides the context
    function App() {
      return (
        <ThemeContext.Provider value={{ background: 'black', foreground: 'white' }}>
          <ThemedButton />
        </ThemeContext.Provider>
      );
    }
    ```
    
    In the example above, ThemedButton uses the useContext hook to consume the ThemeContext. App provides the ThemeContext with the value prop, which is an object with background and foreground properties. The ThemedButton component uses the background and foreground properties from the context to style the button. This way, the button can be styled dynamically based on the context without passing props down manually.

4. `useRef` Hook

    `useRef` is a React Hook that returns a mutable ref object that can be used to store a value or reference to a DOM element. The value stored in a ref persists between renders and can be updated without triggering a re-render of the component.
    
    ``` javascript
    import React, { useRef } from 'react';
    
    function TextInput() {
      const inputRef = useRef(null);
    
      function handleButtonClick() {
        inputRef.current.focus();
      }
    
      return (
        <div>
          <input type="text" ref={inputRef} />
          <button onClick={handleButtonClick}>Focus Input</button>
        </div>
      );
    }
    ```
    
    In the example above, useRef is used to create a reference to the text input element using the ref attribute. The reference is stored in the inputRef variable. The handleButtonClick function uses the current property of the inputRef object to get a reference to the actual DOM element and call its focus() method. This allows the button to focus the input element when clicked.

5. `useReducer` Hook

    `useReducer` is a React Hook that allows you to manage state in a more complex way than useState. It is based on the reducer pattern from functional programming and takes in a reducer function and an initial state value as arguments. The reducer function takes in the current state and an action and returns a new state.
    
    ```javascript
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
    
    In the example above, useReducer is used to create a state variable called state and a dispatch function called dispatch. The counterReducer function is used as the reducer function. The initial state is an object with a count property set to 0. The Counter component uses the state.count value to render the current count, and the dispatch function to update the count by dispatching actions with the type property set to either 'increment' or 'decrement'. The reducer function updates the state based on the action dispatched by returning a new state object with the updated count value.


