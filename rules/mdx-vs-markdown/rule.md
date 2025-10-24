---
type: rule
title: Do you know when to use MDX over Markdown?
seoDescription: " Learn when to use MDX for custom components and advanced functionality, regardless of the framework, versus sticking with Markdown for simplicity."
uri: mdx-vs-markdown
authors:
  - title: Jack Pettit
    url: https://ssw.com.au/people/jack-pettit
guid: 9231556d-6d72-43b8-ba7d-ce704e64221c
related:
  - rule
redirects: []
---
Markdown and MDX are closely related — think of MDX as Markdown’s more powerful sibling. Markdown keeps things simple and readable, while MDX extends it to handle interactive and dynamic content using React (or other component frameworks).

[TinaCMS](https://tina.io) is a great tool to build your site in MDX.

<!--endintro-->

[View MD & MDX examples](/rule).

## When to use Markdown (.md)

Markdown is perfect for straightforward content. Think of it like writing a clear, no-frills document. You'll want to use Markdown when:

* You're creating something simple like a blog post, documentation, or guide
* Your team includes people who aren't tech experts
* You want your page to load quickly
* You just need basic formatting like headings, lists, and images

::: greybox
**Example:** A recipe blog post with some text, headings, and a few pictures. Markdown handles this beautifully without any extra complexity.
:::

## When to use MDX (.mdx)

MDX builds on Markdown by letting you embed components and logic directly inside your content. It’s still Markdown at heart — but with superpowers. Use MDX when:

* You need interactive features that go beyond static text
* You want to include custom components from different web frameworks
* Your content requires some programming logic
* You're creating tutorial content with live examples

::: greybox
**Example:** A coding tutorial with an interactive chart showing performance metrics, or a documentation page with a live code editor where readers can try out code in real-time.
:::

## Things to consider

MDX isn't perfect for every situation. Before you jump in, consider:

* **Complexity** - Since it's more advanced than plain Markdown, non-technical teams might find it tricky
* **Performance** - Too many fancy components can slow down your page
* **Extra setup** - You'll need to manage more technical dependencies

## The golden rule ⭐️

Choose Markdown for simple, fast content. Choose MDX when you need more interactive and dynamic features.

The key is to start simple. Use Markdown for most of your content, and only switch to MDX when you truly need those extra capabilities.

## More on migrating to MDX

Want to migrate your website to a modern CMS like **[🦙 TinaCMS](https://tina.io/)**, and move from Markdown to MDX? Check out [Markdown to MDX migration guide](https://tina.io/docs/guides/converting-md-to-mdx).

`youtube: https://www.youtube.com/watch?v=CyWH5wPJUC8`
**Video: Case Study - SSW migrating from MD to MDX for SSW Rules (5 min)**
