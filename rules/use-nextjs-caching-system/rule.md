---
type: rule
tips: ""
title: Do you know how to use NextJS caching system?
seoDescription: How to use NextJS caching system
uri: use-nextjs-caching-system
authors:
  - title: Gilles Pothieu
    url: https://ssw.com.au/people/gilles-pothieu
guid: 27aa1f0a-3a29-4c3c-a8aa-1deccb4cd6c5
related: 
 - use-nextjs
 
---

Next.js 15 introduced a more explicit and developer-friendly caching system. 
But it's not automatic—caching only activates when you *opt in* using three mechanisms: enabling two flags (`dynamicIO`, `useCache`) in your config and adding the `"use cache"` directive inside a file, a component or a function. This triple-lock prevents accidental caching and gives you fine-grained control over revalidation and tagging.

<!--endintro-->

## Why it matters

Without this opt-in model, stale content can easily sneak into your UI. Now, you’re in full control. You decide what gets cached, for how long, and what tags are used for easy invalidation.

`youtube: https://www.youtube.com/watch?v=xWkozeculPo`  
**Video: Is Next.js 15 any good? "use cache" API first look (8 min)**

## How to enable caching introduced by Next.js 15

To start using the new cache layer, you need to activate two experimental flags in `next.config.js`, and then opt in at the file or function level using the `"use cache"` directive:

```javascript
// next.config.js
module.exports = {
  experimental: {
    dynamicIO: true,
    useCache: true
  }
}
```

Then, inside your route:

```javascript
// app/products/page.js
'use cache'

export default async function ProductPage() {
  const data = await fetch('/api/products', {
    next: { tags: ['products'] }
  })
  return
}
```

## Caching API options

Use the built-in functions below to fine-tune caching behavior:

- **`cacheLife(seconds)`**: Sets a time-to-live (TTL), similar to ISR’s `revalidate`.
- **`cacheTag(tag)`**: Associates a label (e.g. `user-123`) to allow grouped invalidation.
- **`revalidateTag(tag)`**: Clears all entries with that tag on next request—ideal for post-write updates.

```javascript
cacheLife(3600)
cacheTag(`user-${id}`)
revalidateTag('products')

export async function POST() {
  await updateDB()
  revalidateTag('products')
}
```

## Important changes with `dynamicIO`

When using `dynamicIO`, some core Next.js behaviors change:

1. `cookies()` and `headers()` become async functions:
   ```javascript
   import { cookies } from 'next/headers'
   const token = (await cookies()).get('token')
   ```

2. Route files are dynamic by default. You must explicitly add:
   ```javascript
   export const dynamic = 'force-static'
   ```
   if you want to guarantee build-time rendering.

## Pro Patterns

Use hybrid caching for best results:

```javascript
'use cache'
export default async function Dashboard() {
  const staticData = await fetch('/api/metrics', { cacheLife: 3600 })
  const liveData   = await fetch('/api/activity', { cache: 'no-store' })
  return
}

cacheTag(`user-${crypto.randomUUID()}`)
```

::: good
Figure: Good example - Mixing real-time and cached content gives you performance *and* freshness
:::

## Additional Notes

- Cache keys are based on build ID + args, so new props auto-generate new cache entries.
- The client router cache uses `staleTime: 0` by default—navigations recheck the server.
- Deploys automatically clear cache, so no need for manual flushing.

You can learn more in depth about how to cache with Next.js in the [official documentation](https://nextjs.org/docs/app/building-your-application/caching).

## Common Pitfalls

Avoid caching components that depend on non-serializable props (e.g. `children`):

```javascript
'use cache'
function SafeCache({ children }) {
  return <section>{children}</section>
}
```

## Debugging Tips

To inspect what was cached or missed:

```bash
NEXTJS_CACHE_ANALYTICS=1 next build
```

This emits a hit/miss report for each route to the console, giving visibility into caching behavior.