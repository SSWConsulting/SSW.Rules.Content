---
type: rule
title: Do you know how to fetch data in Next.js?
uri: fetch-data-nextjs
authors:
  - title: Harry Ross
    url: https://www.ssw.com.au/people/harry-ross
related:
  - use-nextjs
created: 2023-07-28T06:34:51.000Z
archivedreason: null
guid: df355ce6-47ab-461d-9ddc-d3216dc433b5
---
Next.js is great, as it gives you the ability to run code on the server-side. This means there are now new ways to fetch data via the server to be passed to Next.js app. Next.js also handles the automatic splitting of code that runs on the server and the client, meaning you don't have to worry about bloating your JavaScript bundle when you add code that only runs on the server.  

<!--endintro-->

## Server Side Fetching

There are three primary ways with the Next.js Pages Router to fetch data on the server:

1. Server-side data fetching with `getServerSideProps`
2. Static site generation (SSG) with `getStaticProps`
3. Hybrid static site generation with incremental static regeneration (ISR) enabled in `getStaticProps` 

### getServerSideProps

`getServerSideProps` allows for server-side fetching of data on each request from the client, which makes it great for fetching of dynamic data. It can also be used for secured data, as the code within the function only runs on the server. 

The below example shows an example of how we can use `getServerSideProps` to fetch data. Upon each user's request, the server will fetch the list of posts and pass it as props to the page.  

```tsx
// pages/index.tsx

export const getServerSideProps = async (context) => {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const posts = await res.json();

  return { props: { posts } };
}

export default function Page(props) {
  return (
    <div>
      {props.posts.map(post => (
        <div>
          <h2>{post.title}</h2>
          <p>{post.body}</p> 
        </div>
      ))}
    </div>
  )
}
```

This is great for dynamic data that may not be best suited for `getStaticProps` such as fetching from a database or an API route with data that changes often. 

The `context` parameter also has a lot of useful information about the request, including the request path, cookies sent from the client, and more that can be found on the [official Next.js documentation](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#context-parameter).

You can use <https://next-code-elimination.vercel.app/> to verify what code is sent to the client when using `getServerSideProps`. 

### getStaticProps

We can develop a staticly generated site in Next.js by using `getStaticProps`. Having a statically generated site is great for SEO, as it makes it much easier for Google to index your site compared to a site with complex JavaScript logic, which is harder for web crawlers to understand. Next.js will run the code inside the `getStaticProps` method when you run `npm build`, and generate associated static HTML or JSON data. 

For example, using dynamic routing we can create a static page to show post data based on the URL: 

```tsx
// pages/[slug].tsx

export const getStaticProps = async ({ params }) => {
  const id = params.slug;
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
  const post = await res.json();

  return {
    props: { post }
  };
}

export const getStaticPaths = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const posts = res.json();
  const paths = posts.map((post) => ({
    params: { slug: post.id },
  }));
  
  return { paths, fallback: false };
}

export default function Page(props) {
  return (
    <div>
      <h2>{props.post.title}</h2>
      <p>{props.post.body}</p> 
    </div>
  )
}
```

### Incremental Static Regeneration (Hybrid)

Server-side generation is great for SEO, however if we have a data source that may change between builds, we may need to regenerate the static data generated at build time. With incremental static regeneration (ISR), we can add an expiry time for static data, and Next.js will automatically refetch the data if the expiry time has been reached. However, this will not block the current request where it has noticed that the data has expired with a long loading time - it will fetch the data only for the next request.

```tsx
export const getStaticProps = async () => {
  const res = await fetch(`https://jsonplaceholder.typicode.com/comments`);
  const comments = await res.json();

  return {
    props: { comments },
    revalidate: 60
  };
}
```

This means that if 60 seconds or more has passed after the last time `getStaticProps` was run and the user makes a request to the page, it will rerun the code inside getStaticProps, and render the newly fetched data for the next page visitor.  

## Client Side Fetching

If you want to fetch secured data from a component (not a page) without exposing confidential information to the user (e.g. keys, IDs), the best way to do this is to create a basic API route to fetch this data, which allows for storage of sensitive information on the server, unable to be exposed to the client. 

This would be written in the component like so:

```tsx
const Component = () => {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch("/api/your-api-route")
      .then(res => res.json())
      .then(data => {
        setData(data)
      })
  }, [])

  return (
    <> ... </>
  )
}
```

Then place a file in the /pages/api directory named with the required API route path (i.e. `pages/api/{{ API_ROUTE_HERE }}.ts`):

```ts
// pages/api/your-api-route.ts

import { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method == "GET") {
    const res = await fetch("https://jsonplaceholder.typicode.com/posts");
    const data = await res.json();

    res.status(200).send(data);
  } else {
    res.status(405).json({ error: "Unsupported method" });
  }
}
```

This is a great workaround for the limitation of only being able to use the above server-side fetching functions at a page-level - as it allows for server-side fetching from components. However, keep in mind that this may result in performance impacts from blocking calls to API routes. 

This is also a great way to reduce the occurrence of CORS errors, as you can proxy API data through a simple Next.js API route.
