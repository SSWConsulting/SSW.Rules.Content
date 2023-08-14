---
type: rule
archivedreason: 
title: Do you know the best libraries to fetch data in React?
guid: cae7be1d-2313-43e1-8cc5-cfc1e77b4bb4
uri: fetch-data-nextjs
created: 2023-08-08T05:24:35Z
authors:
- title: Harry Ross
  url: https://www.ssw.com.au/people/harry-ross
related:
- fetch-data-nextjs
---

While using a regular `useEffect` to run when a component is loaded to load data from an API is super easy, it may result in unnecesary duplicate requests for data. It is best to use a library for this purpose, as not only does it solve the afforementioned issue, but also comes with a variety of other useful features such as caching, background updates, and pre-fetching. 

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
:::

This example is not ideal, as it means every time we reload this page component, or if we make the same request on another page, there will be an unneeded request made instead of pulling the data from a cache. 

Below are the two recommended options that both serve effectively the same purpose in providing developers with useful hooks for fetching data. These libraries not only give developers a wide range of other features, but also reduces the amount of boilerplate code they have to write. 

## TanStack Query (previously React Query)

TanStack Query is a feature-rich data fetching library developed by [Tanstack](https://tanstack.com/). It can be used with existing data fetching libraries such as Axios, GraphQL packages such as graphql-request, or just plain fetch. 

`youtube: https://www.youtube.com/watch?v=novnyCaa7To`
**Video: React Query in 100 Seconds by Fireship (2 mins)**

Here's an basic example of how you can use Tanstack Query:

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

* Caching of requests at [key values using `useQuery`](https://tanstack.com/query/latest/docs/react/guides/query-keys)
* Flattening of duplicate requests 
* Background data fetching [using the `isFetching` value](https://tanstack.com/query/latest/docs/react/guides/background-fetching-indicators)
* Automatic retry of failed fetch [with the `retry` and `retryDelay` options in `useQuery`](https://tanstack.com/query/latest/docs/react/guides/query-retries), allowing you to specify the number of retries before giving up
* Easy built-in pagination by [using the `data.hasMore` value](https://tanstack.com/query/latest/docs/react/guides/paginated-queries)
* Automatic revalidation of data [on window focus](https://tanstack.com/query/latest/docs/react/guides/window-focus-refetching)
* Prefetching data [using `prefetchQuery`](https://tanstack.com/query/latest/docs/react/guides/prefetching)
* [Optimistic updates](https://tanstack.com/query/v4/docs/react/guides/optimistic-updates)
* Built-in support for [React 18's Suspense](https://react.dev/reference/react/Suspense) with the [`{ queries: { suspense: true }}` option](https://tanstack.com/query/v4/docs/react/guides/suspense) added to the `QueryClient`
* ["Scroll Restoration"](https://tanstack.com/query/v4/docs/react/guides/scroll-restoration) - maintains the exact position you are scrolled on a webpage
* [React Query DevTools](https://tanstack.com/query/v4/docs/react/devtools) to allow easy debugging of data fetches + caching


You can find out more about Tanstack Query at [tanstack.com/query](https://tanstack.com/query/).

## SWR

SWR is an alternative to Tanstack Query developed by Vercel, the team behind Next.js. Similar to Tanstack Query, SWR is library-agnostic, meaning you can use whatever data fetching library you are comfortable with.

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

* Small bundle size - [only 4.4 kB](https://bundlephobia.com/package/swr@2.2.0)
* Data caching
* Automatically flattens duplicate requests 
* Automatic revalidation of data (either when the page is focused or when a page reconnects to the internet)
* Pagination with [`useSWRInfinite`](https://swr.vercel.app/docs/pagination)
* Built-in support for [React 18's Suspense](https://react.dev/reference/react/Suspense) with the [`{ suspense: true }` option](https://swr.vercel.app/docs/suspense)
* Integration with [Next.js's SSR/SSG capabilities](https://swr.vercel.app/docs/with-nextjs)
* Real-time data support (i.e. WebSockets, SSE) with [`useSWRSubscription`](https://swr.vercel.app/docs/subscription)

**Note:** Currently, the vast majority of SWR APIs are [not compatible with the App router in Next.js 13.](https://swr.vercel.app/docs/with-nextjs)

You can find out more about using SWR at [swr.vercel.app](https://swr.vercel.app/).
