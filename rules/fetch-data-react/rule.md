---
type: rule
title: Do you know the best libraries to fetch data in React?
uri: fetch-data-react
authors:
  - title: Harry Ross
    url: https://www.ssw.com.au/people/harry-ross
related:
  - fetch-data-nextjs
created: 2023-08-08T05:24:35.000Z
archivedreason: null
guid: cae7be1d-2313-43e1-8cc5-cfc1e77b4bb4
---

While using a regular `useEffect` to run when a component is loaded to fetch data is super easy, it may result in unnecesary duplicate requests for data or unexpected errors when unmounting components. It is best to use a library that can provide hooks for fetching data, as not only does it solve the above issues, but also comes with useful features such as caching, background updates, and pre-fetching. 

<!--endintro-->

Below is an example of a standard data fetch in React:

::: bad
```tsx

const Component = () => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/todos/1")
      .then(res => res.json())
      .then(json => {
        setData(json);
        setLoading(false);
      })
  }, [])

  return (
    {loading
      ? <> {/* Display data here */} </>
      : <p>Loading...</p>
    }
  )
}


```
**Figure: The traditional way of fetching data in React**
:::

This example is not ideal, as it means every time we reload this page component, or if we make the same request on another page, there will be an unnecessary request made instead of pulling the data from a cache. 

Below are the two recommended options that both serve effectively the same purpose in providing developers with useful hooks for fetching data. These libraries not only give developers a wide range of other features, but also reduces the amount of boilerplate code they have to write. 

## TanStack Query (previously React Query) - Recommended

TanStack Query is a feature-rich data fetching library developed by [Tanstack](https://tanstack.com/). It can be used with existing data fetching libraries such as [Axios](https://www.npmjs.com/package/axios), GraphQL packages such as [graphql-request](https://www.npmjs.com/package/graphql-request), or just plain fetch. 

`youtube: https://www.youtube.com/watch?v=novnyCaa7To`
**Video: React Query in 100 Seconds by Fireship (2 mins)**

Here's a basic example of how you can use Tanstack Query:

```tsx
import {
  useQuery,
  QueryClient,
  QueryClientProvider,
} from "react-query";

const queryClient = new QueryClient();

function useTodos() {
  return useQuery("todos", async () => {
    const res = await fetch("/api/todos");
    const json = await res.json();
    return json;
  })
}

export const Page = () => {
  const { status, data, error, isFetching } = useTodos();

  if (status === "error") return <div>Error loading data: {error}</div>
  if (status === "loading") return <div>Loading...</div>

  return (
    <QueryClientProvider client={queryClient}>
      <div>
        <div>{/* Display todos here */}</div>
        {isFetching && <p>Re-fetching data in the background...</p>}
      </div>
    </QueryClientProvider>
}

```

Some features of Tanstack Query:

* **Request caching** - [key values pairs using `useQuery`](https://tanstack.com/query/latest/docs/react/guides/query-keys)
* **Duplicate request flattening** - 
* **Background data fetching** - [using the `isFetching` value](https://tanstack.com/query/latest/docs/react/guides/background-fetching-indicators)
* **Automatic retries** - failed fetches are retried with the [`retry` and `retryDelay` options in `useQuery`](https://tanstack.com/query/latest/docs/react/guides/query-retries), allowing you to specify the number of retries before giving up
* **Built-in pagination** - using the [`data.hasMore` value](https://tanstack.com/query/latest/docs/react/guides/paginated-queries)
* **Automatic revalidation** - data revalidated on window focus - [learn more](https://tanstack.com/query/latest/docs/react/guides/window-focus-refetching)
* **Prefetching data** - [using `prefetchQuery`](https://tanstack.com/query/latest/docs/react/guides/prefetching)
* **Optimistic updates** - if a request made fails, but a state variable in UI has already been updated optimistically, Tanstack Query can revert to the old UI state - [learn more](https://tanstack.com/query/v4/docs/react/guides/optimistic-updates)
* **Suspense** - built-in support for [React 18's Suspense](https://react.dev/reference/react/Suspense) with the [`{ queries: { suspense: true }}` option](https://tanstack.com/query/v4/docs/react/guides/suspense) added to `QueryClient`
* **Scroll Restoration** - maintains the exact position you are scrolled on a webpage - [learn more](https://tanstack.com/query/v4/docs/react/guides/scroll-restoration)
* **React Query DevTools** - a Chrome extension that allows for easy debugging of data fetches + caching - [learn more](https://tanstack.com/query/v4/docs/react/devtools)


You can find out more about Tanstack Query at [tanstack.com/query](https://tanstack.com/query/).

## SWR

SWR is an alternative to Tanstack Query developed by Vercel, the team behind Next.js. Much like Tanstack Query, SWR is library-agnostic, meaning you can use whatever data fetching library you are comfortable with.

Here's a basic example of how you can use the library's fetching hook:

```tsx
const fetcher = (url) => fetch(url).then(res => res.json())

export const Page = () => {
  const { data, error, isLoading } = useSWR("/api/todos", fetcher);

  if (error) return <div>Error loading data</div>
  if (loading) return <div>Loading...</div>

  return <div>{/* Display todos here */}</div>
}
```

Some features of SWR: 

* **Small bundle size** - [only 4.4 kB](https://bundlephobia.com/package/swr@2.2.0)
* **Caching** - automatic caching of requests to avoid making duplicate requests
* **Duplicate request flattening** - a global cache to prevent different components fetching the same data
* **Automatic revalidation** - can happen when either the page is focused or when a user reconnects to the internet
* **Pagination** - using the [`useSWRInfinite` hook](https://swr.vercel.app/docs/pagination)
* **Suspense** - Built-in support for [React 18's Suspense](https://react.dev/reference/react/Suspense) with the [`{ suspense: true }` option](https://swr.vercel.app/docs/suspense)
* **Next.js** - Integration with [Next.js's SSR/SSG capabilities](https://swr.vercel.app/docs/with-nextjs)
* **Real-time data** - support for technologies such as WebSockets and SSE with the [`useSWRSubscription` hook](https://swr.vercel.app/docs/subscription)

**Note:** Currently, the vast majority of SWR APIs are [not compatible with the App router in Next.js 13.](https://swr.vercel.app/docs/with-nextjs)

You can find out more about using SWR at [swr.vercel.app](https://swr.vercel.app/).

## RTK Query

Additionally, RTK Query, part of the Redux Toolkit, is a similar library to SWR and React Query with tight integration with Redux and seamless type-safe importing sourced from OpenAPI specifications. 

Here's a basic example of how you can use RTK Query:

```tsx
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const todosApi = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: (builder) => ({
    getTodos: builder.query<Array<Todo>, void>({
      query: () => 'todos',
    }),
  }),
});

const { useGetTodosQuery } = todosApi;

// For use with Redux
const todosApiReducer = todosApi.reducer;

const TodoPage = () => {
  const { data, isError, isLoading } = useGetTodosQuery();

  if (isLoading) return <p>Loading...</p>;
  if (isError) return <p>Error fetching todos</p>;

  return (
    <div>{/*( Display todos here */}</div>
  );
};
```

Some features of RTK Query: 

- **Seamless Redux integration:** Designed as part of the Redux Toolkit, RTK Query is intrinsically designed to work with Redux, providing a cohesive data management experience. [Learn more](https://redux-toolkit.js.org/introduction/getting-started#rtk-query)
- **OpenAPI schema code generation:** Auto-generates end-to-end typed APIs based on OpenAPI schemas, drastically reducing boilerplate and ensuring type safety. [Learn more](https://redux-toolkit.js.org/rtk-query/usage/code-generation#openapi)
- **Caching** - cache management based on endpoint and serialized arguments - [learn more](https://redux-toolkit.js.org/rtk-query/usage/cache-behavior)
- **Automatic retries** - built-in mechanism to automatically retry failed queries, enhancing resilience - [learn more](https://redux-toolkit.js.org/rtk-query/usage/polling)
- **Prefetching** - fetches data in anticipation of user actions to enhance UX - [learn more](https://redux-toolkit.js.org/rtk-query/usage/prefetching)
- **Parallel and dependent queries:** Efficient handling of multiple simultaneous or dependent data fetching. [Learn more](https://redux-toolkit.js.org/rtk-query/usage/customizing-queries#performing-multiple-requests-with-a-single-query)

Discover more about RTK Query in Redux Toolkit's official documentation at [redux-toolkit.js.org/rtk-query/overview](https://redux-toolkit.js.org/rtk-query/overview/).
