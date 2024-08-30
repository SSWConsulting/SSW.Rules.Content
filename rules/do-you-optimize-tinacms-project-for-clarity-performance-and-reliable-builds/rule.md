---
type: rule
title: Do you Optimize Your TinaCMS Project for Clarity, Performance, and
  Reliable Builds
seoDescription: Learn effective strategies to structure and optimize your
  TinaCMS project for clarity, performance, and successful builds.
uri: do-you-optimize-tinacms-project-for-clarity-performance-and-reliable-builds
authors:
  - title: "Gilles Pothieu"
    url: https://www.ssw.com.au/people/gilles-pothieu/
created: 2024-08-28T16:15:00.000Z
guid: 3c59f56f-34b0-47a7-902a-718eb340d2e5
---
Structuring and optimizing your TinaCMS project is essential to achieve clarity, enhance performance, and prevent build failures. Poorly optimized projects can lead to slow site performance, increased server load, and even failed builds due to excessive or inefficient data requests.

Let’s explore how to structure your project effectively and apply best practices to boost performance both in runtime and during the build process.

## 1. Structuring Your TinaCMS Architecture

When working with large datasets or generating multiple subcomponents, following best practices is crucial to maintain performance and clarity.

### Bad Practices:

* **Making Individual Requests with Tina Client for Each Subcomponent:**

  * This method can overwhelm the build process, particularly when dealing with a large number of subcomponents.
* **Using Deeply Nested Schemas with Nested References:**

  * Complex and deeply nested schemas increase the complexity of the project, making it harder to manage and more prone to build failures.
  * They can also lead to inefficient data fetching, further slowing down both runtime and build processes.

### Good Practices:

* **Making a Single Request at a Top-Level Server Component and Passing Props Down:**

  * Data fetched at the top level is cached by default, which enhances performance by reducing redundant API calls.
  * Subcomponents can directly access the necessary data, eliminating the need for repeated requests.

![✅ Figure: Good example - Single request at the top-level server and passing props down](2024-08-28_16-21-56.png)

* **Caching Data at a Top-Level and Accessing It When Necessary:**

  * If passing props is not feasible (e.g., when a component depends on Next.js router information), you should make a general top-level request, cache the data, and then access it directly from the cache within the component.
  * This approach ensures efficient data retrieval and reduces the server load at build time.

## 2. Improving Runtime Performance

Optimizing runtime performance is key to delivering a fast and responsive user experience.

### Bad Practices:

* **Using Client-Side Requests Instead of Cached Values from Server-Side Components:**

  * This approach bypasses pre-fetched, cached data, increasing server load and slowing down the application.
  * It negates the benefits of static site generation, where data should be ready and waiting.

### Common Practices:

* **Utilizing Next.js caching via fetch:** 

  * Next.js’s fetch API is designed to cache by default during static generation and server-side rendering.

### Good Practices:

* **Utilizing Caching at the Highest Level of the Application:**

  * By caching data at the top level, you ensure that it is readily available throughout your application, reducing redundant data fetching and improving overall performance.
  * This approach allows for more efficient data management and quicker response times.
* **Using Dedicated Caching Packages:**

  * [**Redis**:](https://redis.io/fr/solutions/cas-dutilisation/cache/) An in-memory data structure store, Redis is fast and versatile, making it ideal for caching data in memory. 
  * **[Node-cache](https://www.npmjs.com/package/node-cache)**: A lightweight, in-memory caching solution for Node.js applications.

### Gold Plating:

* **Implementing a Singleton Service for Data Requests:**

  * A singleton service that encapsulates general requests and provides data via cache ensures consistent data retrieval and minimizes repetitive API calls, thereby enhancing performance.

## 3. Preventing Build Crashes

To ensure smooth and reliable builds, it’s important to follow best practices that prevent excessive server load and manage data efficiently.

### Best Practices:

* **Avoid Isolating Tina Client Calls in Multiple Subcomponents:**

  * Centralize data fetching to avoid overwhelming the build process with excessive API requests.
* **Cache Large Datasets at a Top Level:**

  * By caching large datasets at a top level, you reduce the number of data fetches during the build process, lowering the risk of overwhelming the system.
* **Avoid Using Deeply Nested References:**

  * Simplifying your data structure and avoiding deeply nested references can help ensure smoother and faster builds.
* **Write custom Tina queries:**

  * You can improve build generation and prevent build crash by creating your own Tina GraphQL queries.

### One last option:

* If a build fails due to overload activities, you can consider reducing the server load by modifying the `next.config.js` file as follows, but this should be done cautiously. This will slow the build process.

```
experimental: 
{
   workerThreads : false,
   cpus: 1
}
```
