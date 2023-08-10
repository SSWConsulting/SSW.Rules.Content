---
type: rule
archivedreason: 
title: Do you use dynamic routing in NextJS?
guid: 
uri: next-dynamic-routes
created: 2023-07-28T12:00:00.0000000Z
authors:
- title: Jack Reimers
  url: https://ssw.com.au/people/jack-reimers
related:
- 
---

NextJS supports dynamic routes out of the box, meaning you can create routes from dynamic data at request or build time. This is especially useful for sites such as blogs that have large amounts of content.

<!--endintro-->

You can create a dynamically routed page by wrapping a folders name in square brackets, and then exporting the `getStaticProps` and `getStaticPaths` functions from that page. 
Eg: [filename] or [slug].

### getStaticProps

When you export getStaticProps, your page will be pre-rendered at build time. You can use `getStaticProps` to retrieve data that will be used to render the page.
For example, you might receive a file name as params to `getStaticProps`, which you can then use in an API call to get the props for that page:

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

### getStaticPaths

The `getStaticPaths` function is used alongside `getStaticProps` to 
