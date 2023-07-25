---
type: rule
archivedreason: 
title: Do you know when to use dynamic imports in Next.js?
guid: 9cc784b6-b0a2-4892-863f-2d697017de9e
uri: dynamically-load-components
created: 2023-07-14T02:13:28Z
authors:
- title: Harry Ross
  url: https://www.ssw.com.au/people/harry-ross
related:
- use-nextjs
- manage-bundle-size
- improve-performance-with-lazy-loading-of-media-assets

---

Components with large imports loaded in on runtime may result in a much worse UX for users of your web app. Next.js can help with this by using [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import) to only load these large components when they are rendered on the page.

<!--endintro-->

When using the Next.js pages router, we can use `next/dynamic` to lazy load components, based on React's [`React.lazy`](https://react.dev/reference/react/lazy) and [`Suspense`](https://react.dev/reference/react/Suspense). 

```jsx 

const HeavyComponent = dynamic(import("./components/HeavyComponent"), {
  loading: () => <p>Loading...</p>
});

export const Page = () => {
  const [showComponent, setShowComponent] = useState(false);

  return (
    <>
      ...
      {showComponent && <HeavyComponent />}
      ...
    </>
  )
}

```

This means that the `<HeavyComponent>` element will only be loaded in when the `showComponent` state variable is true. When condition is then set to `true`, the paragraph component in the `loading` field will display until the component has been loaded onto the page. 


This works by packing the heavy component into a separate JavaScript bundle, which Next.js then sends to the client when the `showComponent` variable is true. 


You can learn more about how to use `next/dynamic` in the [official Next.js documentation](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading#nextdynamic). 
