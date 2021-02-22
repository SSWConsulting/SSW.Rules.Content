---
type: rule
archivedreason: 
title: Tools - Do you know the best Packages and Libraries to use with React?
guid: 00c34a19-49ef-4a04-b3e5-74f107c1761f
uri: tools-do-you-know-the-best-packages-and-libraries-to-use-with-react
created: 2019-05-16T08:32:42.0000000Z
authors: []
related: []
redirects: []

---

The whole React ecosystem improves every month. Tons of additional tools, libraries and components are released to simplify the developer’s job and minimize the required effort. 

<!--endintro-->

### Starter kits

Developers still struggle on making a decision on how to setup their React project when joining the React community. There are thousands of boilerplate projects to choose from and every boilerplate project attempts to fulfil different needs. They vary in a range of minimalistic to almost bloated projects. Here are 2 great Starter kits for React developers.

* **[Create React App](https&#58;//github.com/facebook/create-react-app)** - An officially supported way to start a client-side React project with no configuration
* **[Next.js](https&#58;//nextjs.org/)** - Framework for server-rendered or statically-exported React apps


See more at     [https://reactjs.org/community/starter-kits.html](https&#58;//reactjs.org/community/starter-kits.html)

### Utility Libraries for React

JavaScript ES6 and beyond gives you plenty of built-in functionalities dealing with arrays, objects, numbers, objects and strings. One of the most used JavaScript built-in functionalities in React is the     [built-in map() Array](https&#58;//developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

* [Lodash](https&#58;//lodash.com/) is the most widespread utility library in JavaScript. Lodash comes with a powerful set of functions to access, manipulate and compose.
* [Ramda](http&#58;//ramdajs.com/) is also great utility library when leaning towards functional programming (FP) in JavaScript.


### Asynchronous Requests in React

* [native fetch API](https&#58;//developer.mozilla.org/en/docs/Web/API/Fetch_API) . Nowadays, recent browsers implement the 
       **fetch API** to conduct asynchronous requests. It uses promises under the hood.


* [axios](https&#58;//github.com/mzabriskie/axios). It can be used instead of the native fetch API when your application grows in size. Another alternative is called 
      [superagent](https&#58;//github.com/visionmedia/superagent).


### State Management Helpers

**Reselect** 
[https://github.com/reduxjs/reselect](https&#58;//github.com/reduxjs/reselect)

Creates a selector where the first functions passed in compute props for a final function. If none of those props have changed, then that function is not run and the result from the previous invocation is returned. This keeps the state from needlessly causing components to re-render.

### Global Serverless Deployments

**Now** makes serverless application deployment easy.
[https://zeit.co/now](https&#58;//zeit.co/now)

### Testing

**Jest** 
[https://jestjs.io/](https&#58;//jestjs.io/)

Testing suite that provides a click-and-check API for automated in-browser smoke tests.
