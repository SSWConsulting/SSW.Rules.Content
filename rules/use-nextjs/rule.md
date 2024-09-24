---
type: rule
title: Do you know why Next.js is awesome?
uri: use-nextjs
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
related:
  - best-static-site-tech-stack
created: 2023-03-03T06:35:51.965Z
guid: bb878e77-248d-428e-9681-cdb722a0e4c1
---
React is a powerful JavaScript library for building user interfaces. However, it doesn't provide built-in support for server-side rendering (SSR). This lack of SSR can lead to slow website load times and poor search engine optimization (SEO). That's where [Next.js](https://nextjs.org) comes in. Next.js is a framework built on top of React that provides several features and benefits for building high-performance websites. 

<!--endintro-->

A quick summary of Next.js (pay attention to the first 2.5 min)

`youtube: Sklc_fQBmcs`
**Video: Next.js in 100 Seconds // Plus Full Beginner's Tutorial (11 min)**

A deeper dive on Next.js

`youtube: W4UhNo3HAMw`
**Video: Theo Browne: Next.js is a backend framework (11 min)**

### ✅ Reasons to choose Next.js 

Here are some reasons to consider using Next.js instead of React alone:


1. **Incremental Static Regeneration:** Next.js allows you to create or update static pages _after_ you’ve built your site. Incremental Static Regeneration (ISR) enables you to use static-generation on a per-page basis, **without needing to rebuild the entire site**. With ISR, you can retain the benefits of static while scaling to millions of pages.

2. **TypeScript:** Next.js provides an integrated TypeScript experience, including zero-configuration set up and built-in types for Pages, APIs, and more.

3. **Internationalized Routing:** Next.js has built-in support for internationalized (i18n) routing since v10.0.0. You can provide a list of locales, the default locale, and domain-specific locales and Next.js will automatically handle the routing.

4. **API routes:** API routes provide a solution to build your API with Next.js. Any file inside the folder `pages/api` is mapped to `/api/*` and will be treated as an API endpoint instead of a page. They are server-side only bundles and won't increase your client-side bundle size.

5. **Server-side rendering:** Next.js provides built-in support for SSR, which can significantly improve website performance and SEO by rendering pages on the server and sending HTML to the client. 

6. **Dynamic Import:** Next.js supports lazy loading external libraries with `import()` and React components with `next/dynamic`. Deferred loading helps improve the initial loading performance by decreasing the amount of JavaScript necessary to render the page. Components or libraries are only imported and included in the JavaScript bundle when they're used. `next/dynamic` is a composite extension of `React.lazy` and `Suspense`, components can delay hydration until the Suspense boundary is resolved.

7. **Automatic code splitting:** Next.js automatically splits code into smaller chunks, which can improve website performance by reducing the initial load time.

8. **Built-in CSS, image, and font optimization:** Next.js has built-in support for optimizing CSS, images and fonts. These can help reduce website load times and improve performance.

9. **Automatic Static Optimization:** Next.js automatically determines that a page is static (can be prerendered) if it has no blocking data requirements. This feature allows Next.js to emit hybrid applications that contain **both server-rendered and statically generated pages**.

10. **MDX:** MDX is a superset of markdown that lets you write JSX directly in your markdown files. It is a powerful way to add dynamic interactivity, and embed components within your content, helping you to bring your pages to life.

11. **Incremental adoption:** Next.js allows developers to add server-side rendering and other advanced features incrementally to an existing React application, making it easy to adopt and integrate into existing projects.
  
12. **Codemods:** Next.js provides Codemod transformations to help upgrade your Next.js codebase when a feature is deprecated. Codemods are transformations that run on your codebase programmatically. This allows for a large amount of changes to be applied without having to manually go through every file.

### Summary


By using Next.js instead of React alone, developers can reduce the pain points users may experience and build high-performance websites more efficiently. However, it's important to note that Next.js may not be the best choice for every project, and developers should evaluate their project's specific needs and requirements before making a decision.
