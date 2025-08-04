---
seoDescription: Avoid unnecessary CSS classes and reuse existing ones to keep your code clean and maintainable.
type: rule
title: Do you avoid adding unnecessary CSS classes?
uri: avoid-unnecessary-css-classes
authors:
  - title: Geordie Robinson
    url: https://www.ssw.com.au/people/geordie-robinson
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
created: 2022-07-28T06:06:37.551Z
guid: ca1b7770-298b-4035-b45d-a570fa0ee77b
---

When creating or editing CSS or HTML, it's important to avoid adding unnecessary classes and IDs.

It can be tempting to add classes on elements, as it is often the most obvious solution to CSS problems... but doing so will lead to overly cluttered code and a host of overly specific solutions. When working on CSS it is almost always better to reuse rather than adding additional classes.

<!--endintro-->

You should use a front-end framework, like [Bootstrap](https://getbootstrap.com/) or [Tailwind](https://tailwindcss.com/). The best front-end frameworks will include most of the clases you will need on a project. Basically you will only need new classes for **very specific** layout elements.

::: greybox
**HTML:**

```html
<a class="view-all-link" href="https://www.youtube.com/playlist?list=PLIzW_0dAIKv3mjBeK8eyJbe1bOGWJX_UV">View All</a>
```

**CSS:**

```css
.view-all-link {
  margin-top: 0;
}
```
:::
::: bad
Figure: Bad example - The "view-all-link" class was added unnecessarily
:::

::: greybox
**HTML:**

```html
<a class="mt-0" href="https://www.youtube.com/playlist?list=PLIzW_0dAIKv3mjBeK8eyJbe1bOGWJX_UV">View All</a>
```
:::
::: good
Figure: Good example - Using a front-end framework class has the same effect without adding any extra CSS ruleset
:::
