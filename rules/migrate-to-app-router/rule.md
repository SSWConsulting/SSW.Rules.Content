---
seoDescription: Migrate your Next.js application to modern App Router for more dynamic content and interactivity..
type: rule
title: Do you know how to migrate Page Router to App Router?
uri: migrating-to-app-router
authors:
  - title: Aman Kumar
    url: https://www.ssw.com.au/people/aman-kumar
related:
  - migrate-react-to-nextjs
  - migration-plans
  - modernize-your-app
created: 2025-02-28T00:54:42.810Z
guid: ac979bc0-b37e-4611-9b30-b6c147ed2379
---

Upgrade your Next.js app from **Page Routing** to **App Routing** for better performance, faster navigation, and improved flexibility. With features like React Server Components and optimized data fetching, App Routing enhances interactivity while reducing re-renders. Stay ahead with a more scalable, modern approach to web development. 🚀

<!--endintro-->

### 1. Page Routing (Traditional Routing)

Each route corresponds to a page and loads a new HTML file from the server (or a static file).

**✅ Pros**:

* Simple & Easy to Implement – Suitable for small applications with basic navigation.
* SEO-Friendly – Works well with search engines since each page is independently loaded.
* Direct URL Access – Users can access any page via direct links without additional configuration.

**❌ Cons**:

* Full Page Reloads – Every route change triggers a full reload, affecting performance.
* Limited Interactivity – Does not support dynamic content updates without reloading the page.
* Slower Transitions – Navigation between pages is not as smooth compared to client-side routing.

### 2. App Routing (Client-Side Routing)

App routing (also known as Single Page Application (SPA) Routing) uses JavaScript to handle route changes dynamically without reloading the page. Frameworks like React, Angular, Vue, and Next.js use this approach.

**✅ Pros**:

* Persistent Layout & Faster Navigation - It keeps layouts mounted, reducing re-renders and enabling
* Clear Client-Server Split – App Routing optimizes performance by handling data on the server and interactivity on the client. 🚀
* Better User Experience – Feels like a native app with smooth navigation.
* Dynamic Content – Enables real-time updates without reloading the page.
* Reduced Server Load – Only API calls are made instead of reloading entire pages.

**❌ Cons**:

* Client-Side Performance Considerations – Handling large-scale applications with extensive client-side rendering may lead to higher memory usage and performance bottlenecks.
* Potential State Management Challenges – Managing global state across dynamically loaded components can be more complex compared to traditional page-based navigation.

## Steps to migrate

Here are the steps you can follow to migrate your app from Page Router to App Router.

```ts
// pages/[slug].tsx

// Page Router - Component 

export const getStaticProps = async ({ params }) => {
  const id = params.slug;
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
  const post = await res.json();
  return {
    props: { post },
  };
};
export const getStaticPaths = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const posts = res.json();
  const paths = posts.map((post) => ({
    params: { slug: post.id },
  }));
  return { paths, fallback: false };
};
export default function Page(props) {
  return (
    <div>
      <h2>{props.post.title}</h2>
      <p>{props.post.body}</p>
    </div>
  );
}
```

In the App Router of Next.js, routing is managed through a directory-based system. Instead of creating individual files like ```[filename].tsx``` for dynamic routes, you define a folder corresponding to the route and place a ```page.tsx``` file inside it to serve as the actual page.

| **Page Router**                | **App Router**                      | **Route**                |
|-----------------------------------|----------------------------------------|----------------------------------|
| `/pages/post/[slug].tsx`          | `/app/post/[slug]/page.tsx`            | `/post/123`, `/post/abc`, `post/*`         |

## Step 1 - Move the Component to the App Router Folder

In the App Router, pages are now inside the `/app` directory instead of /pages. Create a new folder for dynamic routes:

```bash
/app/post/[slug]/page.tsx
```

## Step 2 - Update the Component to Use Server Components

By default, components in the App Router are Server Components, meaning you can directly fetch data without getStaticProps or getServerSideProps. Update your component:

**Migrated App Router Component** (```/app/post/[slug]/page.tsx```)

```ts
export default async function Page({ params }: { params: { slug: string } }) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.slug}`);
  const post = await res.json();

  return (
    <div>
      <h2>{post.title}</h2>
      <p>{post.body}</p>
    </div>
  );
}
```

✅ No Need for getStaticProps or getStaticPaths – The App Router automatically handles static generation and caching. (`dynamicParams` can be used as replacement of `fallback`)

## Step 3 - Handle Dynamic Routes with ```generateStaticParams```

In the Page Router, ```getStaticPaths``` was used to predefine dynamic routes. In the App Router, use ```generateStaticParams```:

Add ```generateStaticParams``` for Static Pre-rendering

```ts
export async function generateStaticParams() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const posts = await res.json();

  return posts.map((post: { id: number }) => ({
    slug: post.id.toString(),
  }));
}
```

✅ Equivalent to ```getStaticPaths```, ensuring pre-rendering for static pages.

## Step 4 - Enable Caching and Revalidation (Optional)

In the App Router, **fetching is cached by default**. You can configure it with ```revalidate``` to enable **Incremental Static Regeneration (ISR)**:

```ts
export default async function Page({ params }: { params: { slug: string } }) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.slug}`, {
    next: { revalidate: 60 }, // Revalidate every 60 seconds
  });
  const post = await res.json();

  return (
    <div>
      <h2>{post.title}</h2>
      <p>{post.body}</p>
    </div>
  );
}
```

✅ Improves Performance – Pages are cached and revalidated only when needed.

## Step 5 - Remove the Old pages Directory

Once all your components are migrated, delete the old /pages directory to fully transition to the App Router.

For a comprehensive guide on [migrating from the Pages Router to the App Router](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration) in Next.js, please refer to the official Next.js documentation.
