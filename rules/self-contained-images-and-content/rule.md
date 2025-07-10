---
type: rule
tips: ""
title: Do you keep your images and content self-contained in your TinaCMS +  Next.js project?
seoDescription: Best practices for keeping your content and images self-contained in TinaCMS + Next.js, with three options and a recommended setup.
uri: self-contained-images-and-content
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Gilles Pothieu
    url: https://www.ssw.com.au/people/gilles-pothieu
  - title: Hugo Pernet
    url: https://www.ssw.com.au/people/hugo-pernet
related:
  - using-markdown-to-store-your-content
guid: fbe98e99-b57f-4605-a498-459bbbfc5ea7
---

When building a website using TinaCMS and Next.js, not all images need to live next to your content. Shared assets like logos, icons, or other global visuals are best stored in a central media folder (e.g. /public/uploads). This keeps things simple and avoids duplication.

However, for documents that embed images—like blog posts or rules like this one—it’s important to keep the content (Markdown/MDX files) and related media together in the same folder. This self-contained structure improves maintainability, makes GitHub editing clearer, and supports portability.

<!--endintro-->

`youtube: https://www.youtube.com/watch?v=JX90jbgAvRw`
**Video: Tina.io - The 3 options for storing markdown in GitHub for TinaCMS (5 min)**

By default, Tina stores content in a `/content` folder and images in `/public`, which breaks self-containment and can cause confusion.

Let's explore three solutions to fix that and store content and images together.
---

You have 3 options:

## 1. Default structure + matching folders

* Content in `/content`
* Images in `/public`
* Add a link to image folder in frontmatter of content file

**✅ Pros**

* Works out of the box  
  
**❌ Cons**

* Not self-contained  
* Prone to errors when renaming/moving files
* You must manually manage matching folder names and use frontmatter to point to images.

## 2. Everything inside content folder

* Each document gets a folder in `/content`
* Images are stored alongside the MDX file

![Figure: Option 2 - Folder structure - rules example](option-2-structure.png)

**✅ Pros**

* Fully self-contained  
* Tina Media Manager works  
  
**❌ Cons**

* Requires extra setup: update config, collections, and add a middleware

### Example implementation (Rules)

```js
import { NextResponse } from 'next/server';

export function middleware(req) {
  if (process.env.DEVELOPMENT !== 'true') {
    return NextResponse.next();
  }

  const url = req.nextUrl;

  // Check if the request is for an image in the content/rules folder
  if (url.pathname.startsWith('/rules/') && url.pathname.match(/\.(png|jpg|jpeg|gif|webp)$/i)) {
    const escapedUrl = encodeURIComponent(url.pathname);
    const apiUrl = `http://localhost:3000/api/serve-image?filepath=${escapedUrl}`;
    console.log('Redirecting to API for image:', apiUrl);
    return NextResponse.redirect(apiUrl);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/rules/:path*'],
};
```
**Figure: Middleware to intercept media requests and call internal API**  


   
```js
import { NextApiRequest, NextApiResponse } from 'next';
import fs from 'fs';
import path from 'path';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (process.env.DEVELOPMENT !== 'true') {
    res.status(403).send('API route is disabled in production');
    return;
  }

  const { filepath } = req.query;

  if (!filepath || typeof filepath !== 'string') {
    res.status(400).send('Filepath is required');
    return;
  }

  const unescapedFilepath = decodeURIComponent(filepath);
  const imagePath = path.join(process.cwd(), 'content/', unescapedFilepath);

  try {
    const imageBuffer = fs.readFileSync(imagePath);
    const contentType = `image/${path.extname(unescapedFilepath).slice(1)}`;

    res.setHeader('Content-Type', contentType);
    res.send(imageBuffer);
  } catch (error) {
    console.error('Error reading image:', error);
    res.status(404).send('Image not found');
  }
}
```
**Figure: Internal API to serve images from content folder**

You can find more details on [this repository](https://github.com/tinacms/demo-storing-images-and-content-together)

## 3. Everything inside public folder (✅ Recommended)

* Each document has a folder in `/public/uploads`
* Images and MDX file live together

![Figure: Option 3 - Folder structure - rules example](option-3-structure.png)

**✅ Pros**

* Fully self-contained  
* Tina Media Manager works  
* No custom middleware needed
  
**❌ Cons**

* MDX files live in `public`, which is unconventional—but works

This option is clean, simple, and works with Tina’s Media Manager out of the box — no special setup required.

### Example Collection config (Rules)

```js
import { Collection } from "tinacms";

const Rule: Collection = {
  label: "Rules",
  name: "rule",
  path: "public/uploads/rules",
  fields: [
    ...
  ],
  ...
};

export default Rule;
```
**Figure: Path pointing to public/uploads folder**

See more on [Tina.io - Storing Media With Content](https://tina.io/docs/guides/storing-media-with-content).
