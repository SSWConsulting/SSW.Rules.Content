---
type: rule
title: Do you know how to use single codebase for multiple domains with TinaCMS and Next.js?
seoDescription: Optimize your Next.js and TinaCMS project with a single codebase
  to efficiently manage multiple domains, locations, and content.
uri: single-codebase-for-multiple-domains-with-tinacm-nextjs
authors:
  - title: Gilles Pothieu
    url: https://www.ssw.com.au/people/gilles-pothieu
created: 2024-08-28T17:37:00.000Z
guid: 2bba887b-9dd7-4f07-978c-a793611e2f85
---
Using multiple domains using TinaCMS and Next.js requires few steps. This setup is particularly useful for managing content across different locations or websites, all from a centralized codebase. We will cover how to structure your project, configure middleware for domain-specific content, and manage environment variables for different locations.

<!--endintro-->

## Project Structure

We will detail a project structure using a simple example of a cooking application. We are using the [App Router](https://nextjs.org/docs/app) introduced with version 13.4 of Next.js.

To support multiple domains, the project structure is organized as follows:

### 1. **Content Directory**

The content for each location is organized under the `content` directory, which contains various subdirectories for recipies, posts, and pages. Each location, such as Australia or France, has its own subdirectory under `pages` and `recipes` which contains the content relevant to that location.

```bash
├── content
|   ├── pages
│   │   ├── Australia
│   │   ├── France
│   ├── posts
│   └── recipes
│       ├── Australia
│       └── France
```

### 2. **Application Directory**

The src/app/\[location] directory contains the shared codebase for all locations. This includes components like the posts, recipes, and other custom pages. The `layout.tsx` and `page.tsx` files handle the layout and page rendering for each location.

```bash
├── src
│   ├── app
│   │   ├── [location]
|   |   |   ├── [filename]
│   │   │   |   ├── page.tsx
|   │   │   ├── layout.tsx
|   │   │   ├── not-found.tsx
|   |   |   ├── page.tsx
│   │   │   ├── posts
|   |   |   ├── recipes
```

## Middleware Configuration

To handle domain-specific routing, we use a middleware file `middleware.ts` located in the src directory. This middleware rewrites URLs based on the hostname, routing requests to the appropriate location's content.

### Middleware Implementation

```js
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

/**
 * Middleware function to handle URL rewriting based on the request's hostname.
 * 
 * This middleware dynamically rewrites incoming requests to ensure that 
 * content is served according to the domain (hostname) being accessed.
 * 
 * - For local development, it redirects requests to a default location.
 * - For production, it matches the domain to a location and rewrites the URL 
 *   accordingly.
 *
 * @param {NextRequest} request - The incoming HTTP request object.
 * @returns {NextResponse} - The response object with the rewritten URL.
 */
export function middleware(request: NextRequest) {
  // Retrieve the hostname from the request headers
  const hostname = request.headers.get('host');
  
  // Extract the pathname from the requested URL (e.g., /about, /contact)
  const { pathname } = request.nextUrl;

  // Check if the request is coming from a local development environment
  const isLocal =
    hostname?.includes('localhost') || hostname?.includes('127.0.0.1'); 

  // Variable to store the response after applying the rewrite rules
  let nextResponse;

  // Retrieve the list of locations and corresponding domains from environment variables
  const locationsList = process.env.NEXT_PUBLIC_LOCATION_LIST
    ? JSON.parse(process.env.NEXT_PUBLIC_LOCATION_LIST)
    : [];

  // If running locally, rewrite the URL to include the default location
  if (isLocal) {
    nextResponse = NextResponse.rewrite(
      new URL(
        `/${process.env.DEFAULT_LOCALHOST_LOCATION}${pathname}`,
        request.url
      )
    );
  } else {
    // Loop through the list of locations to find a matching domain
    for (const location of locationsList) {
      if (hostname == location.domain) {
        // Rewrite the URL to the corresponding location's content
        nextResponse = NextResponse.rewrite(
          new URL(`/${location.location}${pathname}`, request.url)
        );
        break; // Exit the loop once a match is found
      }
    }
  }

  // Return the response with the rewritten URL
  return nextResponse;
}

/**
 * Configuration object for the middleware.
 *
 * Specifies the paths that should be handled by the middleware. The matcher 
 * excludes certain paths (e.g., Next.js internals, static files, favicon) 
 * to avoid unnecessary processing.
 */
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - _next (Next.js internals like static files and scripts)
     * - static (static assets like images or stylesheets)
     * - favicon.ico (the site's favicon)
     * - Files with extensions (e.g., .js, .css, .png)
     */
    '/((?!api|_next|static|favicon.ico|.*\\..*).*)',
  ],
};
```

## Environment Variables and Vercel Configuration (or other host)

You need to configure the following environment variables for the middleware to function correctly:

1. **NEXT_PUBLIC_LOCATION_LIST**: A JSON string representing the list of locations and their corresponding domains.
2. **DEFAULT_LOCALHOST_LOCATION**: The default location to use when running the application locally.

Example of `.env` file:

```bash
NEXT_PUBLIC_LOCATION_LIST='[{"location": "australia", "domain": "website-australia.com.au"}, {"location": "france", "domain": "website-france.fr"}]'
DEFAULT_LOCALHOST_LOCATION="australia"
```

If deploying on Vercel, ensure that the environment variables are set up in the project settings under Environment Variables. This will allow Vercel to use these variables during the build and runtime.
