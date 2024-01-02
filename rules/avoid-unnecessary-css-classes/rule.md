---
type: rule
title: Do you avoid adding unnecessary CSS classes?
uri: avoid-unnecessary-css-classes
authors:
  - title: Geordie Robinson
    url: https://www.ssw.com.au/people/geordie-robinson/
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
created: 2022-07-28T06:06:37.551Z
guid: ca1b7770-298b-4035-b45d-a570fa0ee77b

---

When making or editing CSS or HTML content it is important to avoid adding classes and ID's unnecessarily.

It can be tempting to add classes on elements, as it is often the most obvious solution to CSS problems... but doing so will lead to overly cluttered code and a host of overly specific solutions. When working on CSS it is almost always better to reuse rather than adding additional classes.

<!--endintro-->

You should use a front-end framework, like Bootstrap or Tailwind. The best front-end frameworks will include most of the clases you will need on a project. Basically you will only need new classes for very specific layout elements.

HTML:

```html
<a class="view-all-link" href="https://www.youtube.com/playlist?list=PLIzW_0dAIKv3mjBeK8eyJbe1bOGWJX_UV">View All</a>
```

CSS:

```css
.view-all-link{
  margin-top: 0;
}
```

::: bad
Figure: Bad example - The "view-all-link" class was added unnecessarily
:::

HTML:

```html
<a class="mt-0" href="https://www.youtube.com/playlist?list=PLIzW_0dAIKv3mjBeK8eyJbe1bOGWJX_UV">View All</a>
```

::: good
Figure: Good example - Using [Bootstrap's class "mt-0"](https://getbootstrap.com/docs/4.0/utilities/spacing/) has the same affect without adding any class
:::
