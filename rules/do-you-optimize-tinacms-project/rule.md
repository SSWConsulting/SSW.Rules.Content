---
type: rule
title: Do you optimize your TinaCMS project for clarity, performance, and reliable builds?
seoDescription: Learn effective strategies to structure and optimize your
    TinaCMS project for clarity, performance, and successful builds.
uri: do-you-optimize-tinacms-project
authors:
    - title: 'Gilles Pothieu'
      url: https://www.ssw.com.au/people/gilles-pothieu/
created: 2024-08-28T16:15:00.000Z
guid: 3c59f56f-34b0-47a7-902a-718eb340d2e5
---

Structuring and optimizing your TinaCMS project is essential to achieve clarity, enhance performance, and prevent build failures. Poorly optimized projects can lead to slow site performance, increased server load, and even failed builds due to excessive or inefficient data requests.

Let’s explore how to structure your project effectively and apply best practices to boost performance both in runtime and during the build process.

<!--endintro-->

## 1. Structuring your TinaCMS Architecture

When working with large datasets or generating multiple subcomponents, following best practices is crucial to maintain performance and clarity.

### ❌ Bad practices

-   **Using deeply nested schemas with nested references**

    -   Complex and deeply nested schemas increase the complexity of the project, making it harder to manage and more prone to build failures
    -   They can also lead to inefficient data fetching, further slowing down both runtime and build processes

### ✅ Good practices

-   **Making a single request at a top-level server component and using React Context or a state management library**

    -   Data fetched at the top level can be stored in a React Context or a global state management solution (e.g., [Redux](https://redux.js.org/)). This allows all components to access the data without the need to pass props manually
    -   This approach ensures better scalability, as subcomponents can access the necessary data directly from the context or store, eliminating redundant API calls and avoiding prop drilling

::: good

```js
export default async function Home({ params }: HomePageProps) {
    const location = params.location;

    const websiteProps = await client.queries.website({
        relativePath: `${location}/website.md`,
    });

    const { conferencesData, footerData, speakers } = websiteProps.data;

    return (
        <ConferenceContext.Provider value={conferencesData}>
            <FooterContext.Provider value={footerData}>
                <PageTransition>
                    <HomeComponent speakers={speakers} />
                </PageTransition>
            </FooterContext.Provider>
        </ConferenceContext.Provider>
    );
}

export async function generateStaticParams() {
    const contentDir = path.join(process.cwd(), 'content/websites');
    const locations = await fs.readdir(contentDir);

    return locations.map((location) => ({ location }));
}
```

**Figure: This code provides `conferencesData` and `footerData` via contexts, while passing `speakers` directly as props to `HomeComponent` for immediate use**
:::

-   **Caching data at a Top-level and accessing it when necessary**

    -   If passing props is not feasible (e.g., when a component depends on Next.js router information), you should make a general top-level request, cache the data, and then access it directly from the cache within the component
    -   This approach ensures efficient data retrieval and reduces the server load at build time

## 2. Improving Runtime Performance

Optimizing runtime performance is key to delivering a fast and responsive user experience.

### ❌ Bad practices

-   **Using client-side requests instead of relying on cached data from build process**

    -   This approach can negate the benefit of static site generation, where data is fetched and cached during the process
    -   Making too many client-side requests increses server load and slows down the application

### ✅ Good practices

-   **Using static site generation (SSG) to fetch and cache content during the build**

    -   With TinaCMS, data can be fetched at build time, this will :
        -   minimizes dynamic fetching and enhances performance
        -   faster load time
        -   less strain on the server

## 3. Improving Build Performance

To ensure smooth and reliable builds, it’s important to follow best practices that prevent excessive server load and manage data efficiently.

### ✅ Best practices

-   **Write custom GraphQL queries**

    -   You can improve data retreival by creating your own GraphQL queries  
        Auto-generated GraphQL queries are not optimized, as a result, they may include nested objects with redundant data. For example, recipes that include an ingredients object, which in turn includes the same recipes again. Creating custom queries can reduce the size of objects and improve performance
