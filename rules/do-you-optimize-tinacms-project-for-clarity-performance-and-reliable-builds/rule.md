---
type: rule
tips: ""
title: Do you Optimize Your TinaCMS Project for Clarity, Performance, and
  Reliable Builds
seoDescription: Learn effective strategies to structure and optimize your
  TinaCMS project for clarity, performance, and successful builds.
uri: do-you-optimize-tinacms-project-for-clarity-performance-and-reliable-builds
authors:
  - title: ""
created: 2024-08-28T16:15:00.000Z
guid: 3c59f56f-34b0-47a7-902a-718eb340d2e5
---
Structuring and optimizing your TinaCMS project is essential to achieve clarity, enhance performance, and prevent build failures. Poorly optimized projects can lead to slow site performance, increased server load, and even failed builds due to excessive or inefficient data requests.

Let’s explore how to structure your project effectively and apply best practices to boost performance both in runtime and during the build process.

## 1. Structuring Your TinaCMS Architecture

When working with large datasets or generating multiple subcomponents, following best practices is crucial to maintain performance and clarity.

### Bad Practices:

- **Making Individual Requests with Tina Client for Each Subcomponent:**
  - It leads to performance degradation and deviates from Next.js paradigms, which prioritize static generation and server-side rendering.
  - This method can overwhelm the build process, particularly when dealing with a large number of subcomponents.

- **Using Deeply Nested Schemas with Nested References:**
  - Complex and deeply nested schemas increase the complexity of the project, making it harder to manage and more prone to build failures.
  - They can also lead to inefficient data fetching, further slowing down both runtime and build processes.

### Good Practices:

- **Making a Single Request at a Top-Level Server Component and Passing Props Down:**
  - Data fetched at the top level is cached by default, which enhances performance by reducing redundant API calls.
  - Subcomponents can directly access the necessary data, eliminating the need for repeated requests.

- **Caching Data at a Top-Level and Accessing It When Necessary:**
  - If passing props is not feasible (e.g., when a component depends on Next.js router information), you should make a general top-level request, cache the data, and then access it directly from the cache within the component.
  - This approach ensures efficient data retrieval and reduces the server load.

## 2. Improving Runtime Performance

Optimizing runtime performance is key to delivering a fast and responsive user experience.

### Bad Practices:

- **Using Client-Side Requests Instead of Cached Values from Server-Side Components:**
  - This approach bypasses pre-fetched, cached data, increasing server load and slowing down the application.
  - It negates the benefits of static site generation, where data should be ready and waiting.

- **Relying on React Cache:**
  - React’s cache is still a beta feature with limited applicability and minimal performance improvements. Relying on it can lead to unpredictable results, making it unsuitable for most production environments.

### Good Practices:

- **Utilizing Caching at the Highest Level of the Application:**
  - By caching data at the top level, you ensure that it is readily available throughout your application, reducing redundant data fetching and improving overall performance.
  - This approach allows for more efficient data management and quicker response times.

- **Using Dedicated Caching Packages:**
  - **Redis**: An in-memory data structure store, Redis is fast and versatile, making it ideal for caching data in memory. This reduces the need for repeated database queries or API calls, particularly in applications requiring quick data retrieval and scalability.
  - **Node-cache**: A lightweight, in-memory caching solution for Node.js applications, Node-cache is perfect for caching smaller datasets directly in your application, reducing latency and improving performance.

- **Implementing a Singleton Service for Data Requests:**
  - A singleton service that encapsulates general requests and provides data via cache ensures consistent data retrieval and minimizes repetitive API calls, thereby enhancing performance.

## 3. Preventing Build Crashes

To ensure smooth and reliable builds, it’s important to follow best practices that prevent excessive server load and manage data efficiently.

### Best Practices:

- **Avoid Isolating Tina Client Calls in Multiple Subcomponents:**
  - Centralize data fetching to avoid overwhelming the build process with excessive API requests.

- **Cache Large Datasets at a Top Level:**
  - By caching large datasets at a top level, you reduce the number of data fetches during the build process, lowering the risk of overwhelming the system.

- **Avoid Using Deeply Nested References:**
  - Simplifying your data structure and avoiding deeply nested references can help ensure smoother and faster builds.

- **Carefully Adjust `next.config.js` Settings:**
  - While adjusting `next.config.js` settings can help manage server load, such as by modifying `workerThreads` and `cpus` options, this should be done cautiously. Reducing these values might underutilize server resources and could negatively impact build performance rather than improve it.

## 4. Special Consideration: TinaCMS

When using TinaCMS, favoring the use of a singleton cache over the native fetch API (which caches by default) can significantly improve build speed, nearly doubling it in some cases.
