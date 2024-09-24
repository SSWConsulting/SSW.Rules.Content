---
type: rule
title: Tools - Do you know the best Packages and Libraries to use with React?
uri: tools-do-you-know-the-best-packages-and-libraries-to-use-with-react
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2019-05-16T08:32:42.000Z
archivedreason: null
guid: 00c34a19-49ef-4a04-b3e5-74f107c1761f
---

The whole React ecosystem improves every month. Tons of additional tools, libraries and components are released to simplify the developer’s job and minimize the required effort. 

<!--endintro-->

### Starter kits

Developers still struggle on making a decision on how to setup their React project when joining the React community. There are thousands of boilerplate projects to choose from and every boilerplate project attempts to fulfil different needs. They vary in a range of minimalistic to almost bloated projects. Here are 4 great Starter kits for React developers.

* **[Vite](https://vitejs.dev/guide/)** - A modern tool for quicker development and building, compatible with different front-end frameworks, including React
* **[Create React App](https://github.com/facebook/create-react-app)** - A popular and easy way to start React projects with minimal setup
* **[Next.js](https://nextjs.org/)** - A flexible React framework that's great for making websites. It helps pages load fast and is user-friendly for developers while also providing SEO capabilities
* **[Gatsby](https://www.gatsbyjs.com/)** - A powerful React framework for static websites and blogs with robust static site generation capabilities and SEO optimization

See more at [Start a New React Project](https://react.dev/learn/start-a-new-react-project).

### Utility Libraries for React

JavaScript ES6 and beyond gives you plenty of built-in functionalities dealing with arrays, objects, numbers, objects and strings. One of the most used JavaScript built-in functionalities in React is the [built-in map() Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

* [Lodash](https://lodash.com/) is the most widespread utility library in JavaScript. Lodash comes with a powerful set of functions to access, manipulate and compose
* [Ramda](https://ramdajs.com/) is also great utility library when leaning towards functional programming (FP) in JavaScript

### Asynchronous Requests in React

* [native fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) - Nowadays, recent browsers implement the **fetch API** to conduct asynchronous requests. It uses promises under the hood

* [axios](https://github.com/axios/axios) - It can be used instead of the native fetch API when your application grows in size. Another alternative is called [superagent](https://github.com/visionmedia/superagent)

### State Management Helpers

*  **[Reselect](https://github.com/reduxjs/reselect)** - Creates a selector where the first functions passed in compute props for a final function. If none of those props have changed, then that function is not run and the result from the previous invocation is returned. This keeps the state from needlessly causing components to re-render

### Global Serverless Deployments

*  **[Vercel](https://vercel.com/home)** - Makes serverless application deployment easy

### Testing

* **[Jest](https://jestjs.io/)** - Testing suite that provides a click-and-check API for automated in-browser smoke tests
