---
type: rule
tips: ""
title: Do you keep your images and content self-contained in your TinaCMS +
  Next.js project?
seoDescription: ""
uri: self-contained-images-and-content
authors:
  - title: ""
guid: fbe98e99-b57f-4605-a498-459bbbfc5ea7
---
When building a website using **TinaCMS and Next.js**, it’s important to keep your content (Markdown/MDX files) and related images together in the same folder. This makes your project easier to maintain, improves GitHub editing, and supports better portability.
            
<!--endintro-->

By default, Tina stores content in a `/content` folder and images in `/public`, which breaks self-containment and can cause confusion.

---

You have 3 options:

## 1. **Default structure**

- Content in `/content`
- Images in `/public`
- You must manually manage matching folder names and use frontmatter to point to images.

✅ Works out of the box  
❌ Not self-contained  
❌ Prone to errors when renaming/moving files

## 2. **Everything inside content folder**

- Each rule gets a folder in `/content`
- Images are stored alongside the MDX file

✅ Fully self-contained  
✅ Tina Media Manager works  
❌ Requires extra setup: update config, collections, and add a middleware

## 3. **Everything inside public folder** (✅ Recommended)

- Each rule has a folder in `/public/rules`
- Images and MDX file live together

✅ Fully self-contained  
✅ Tina Media Manager works  
✅ No custom middleware needed  
❌ MDX files live in `public`, which is unconventional—but works

This option is clean, simple, and works with Tina’s Media Manager out of the box—no special setup required. See more on [Tina.io - The 3 options for storing markdown in GitHub for TinaCMS
](https://www.youtube.com/watch?v=i3A6KqxcLYE).








