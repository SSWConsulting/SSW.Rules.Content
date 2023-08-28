---
type: rule
archivedreason: 
title: Do you use dynamic routing in NextJS?
guid: cbf26a37-1f65-43c7-b440-e65a548db7f5
uri: next-dynamic-routes
created: 2023-07-28T12:00:00.0000000Z
authors:
- title: Jack Reimers
  url: /people/jack-reimers
related:
- use-nextjs
- fetch-data-nextjs
---

NextJS supports dynamic routes out of the box, meaning you can create routes from dynamic data at request or build time. This is especially useful for sites such as blogs that have large amounts of content.

<!--endintro-->

You can create a dynamically routed page by wrapping a folders name in square brackets, and then exporting the `getStaticProps` and `getStaticPaths` functions from that page. 
Eg: [filename].tsx or [slug].tsx.

### getStaticProps

When you export getStaticProps, your page will be pre-rendered at build time. You can use `getStaticProps` to retrieve data that will be used to render the page.
For example, you might receive a file name from the requested URL, i.e. /page/{{ FILENAME }}, which you can then use in an API call to get the props for that page:

```
export const getStaticProps = async ({ params }) => {
  const apiUrl = {{ API URL }} + params.filename;
  const response = await fetch(apiUrl);

  return {
    props: { data: response }
  }
}
```

The props from above can then be used from your page, and the data will be filled depending on the dynamic route the user has navigated to:

```
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

```
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

- `false (default)` - any request for a page that has not been generated will return a 404.
- `true` - the page will be generated on demand if not found and stored for subsequent requests.
- `blocking` - similar to true, except NextJS will not respond to the request until the page has finished generating.
