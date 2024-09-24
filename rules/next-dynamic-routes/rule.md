---
type: rule
title: Do you use dynamic routing in Next.js?
uri: next-dynamic-routes
authors:
  - title: Jack Reimers
    url: https://ssw.com.au/people/jack-reimers
related:
  - use-nextjs
  - fetch-data-nextjs
created: 2023-07-28T12:00:00.000Z
archivedreason: null
guid: cbf26a37-1f65-43c7-b440-e65a548db7f5
---

NextJS supports dynamic routes out of the box, meaning you can create routes from dynamic data at request or build time. This is especially useful for sites such as blogs that have large amounts of content.

<!--endintro-->

Dynamic routes allow developers to accommodate unpredictable URLs. Instead of defining a static path, segments of the path can be dynamic.

## Why Use Dynamic Routes?

- **Flexibility**: Easily cater to a wide variety of content without setting up individual routes.
- **Optimization**: Efficiently serve content based on real-time data or user-specific requirements.

## Folder Structure

To tap into this feature, wrap your folder's name in square brackets, for instance, `[filename].tsx` or `[slug].tsx`.

::: info
The directory structure should mirror the dynamic nature of the routes. Here's a standard representation:
:::

```bash
pages/
|-- [slug]/
|   |-- index.tsx
|-- [id]/
|   |-- settings.tsx
```
**Figure: Here, both _slug_ and _id_ are dynamic route segments**

For scenarios where routes need to capture multiple path variations, Next.js introduces the "catch-all" feature. This can be employed by prefixing an ellipsis "..." to the dynamic segments.

To delve deeper into the intricacies of Dynamic Routes, consider exploring the [official Next.js documentation](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes).


### getStaticProps

When you export getStaticProps, your page will be pre-rendered at build time. You can use `getStaticProps` to retrieve data that will be used to render the page.
For example, you might receive a file name from the requested URL, i.e. `/page/{{ FILENAME }}`, which you can then use in an API call to get the props for that page:

```js
export const getStaticProps = async ({ params }) => {
  const apiUrl = {{ API URL }} + params.filename;
  const response = await fetch(apiUrl);

  return {
    props: { data: response }
  }
}
```

The props from above can then be used from your page, and the data will be filled depending on the dynamic route the user has navigated to:

```js
export default function Page(
  props: InferGetStaticPropsType<typeof getStaticProps>
}) {
  <p>
    props.data
  </p>
}
```

When using `getStaticProps`, you **must** also use `getStaticPaths` in order for dynamic routing to work.

### getStaticPaths

The `getStaticPaths` function is used alongside `getStaticProps` and returns a list of paths, which NextJS will use to generate the dynamic pages.

```js
export const getStaticPaths = async () => {
  const apiUrl = {{ API URL }};
  const response = await fetch(apiUrl);

  return {
    paths: response,
    fallback: false,
  }
}
```

`paths` is the list of pages you want to generate.  
`fallback` is a boolean value that determines how NextJS handles routes that are not generated at build time, and can be set to:

- `false (default)` - Any request for a page that has not been generated will return a 404
- `true` - The page will be generated on demand if not found and stored for subsequent requests
- `blocking` - Similar to true, except NextJS will not respond to the request until the page has finished generating
