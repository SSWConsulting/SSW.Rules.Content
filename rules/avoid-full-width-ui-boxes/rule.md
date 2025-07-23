---
type: rule
tips: ""
title: Do you avoid full-width UI boxes on large screens?
seoDescription: Avoid full-width UI boxes on large screens. Use fit-content with
  min and max width to improve readability, maintain alignment, and ensure a
  clean responsive layout.
uri: avoid-full-width-ui-boxes
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
related:
  - rule
  - enforce-the-text-meaning-with-icons-and-emojis
guid: 545edc76-fd47-4bed-9083-19a752415c14
---
On large screens, full-width UI boxes can look awkward and reduce readability, especially when the content inside is just a short message. 

While full-width is fine on mobile (where horizontal space is limited), desktop and tablet layouts need smarter width handling.

<!--endintro-->

::: bad
![Figure: Bad example - Box doesn't look right](bad-full-width-box.png)
:::

::: good
![Figure: Good example - Box looks intentional](good-limited-width-box.png)
:::

## Defining responsive box widths

Apply the following CSS width properties to keep your UI boxes clean and responsive:

```css
width: fit-content;
min-width: 40%;
max-width: 700px;
```

## ✅ Design advantages

* **Better readability** for both short and long messages

  * Short messages don't look oddly small (thanks to min-width)
  * Longer messages don't sprawl across the full page (thanks to max-width)
  * Boxes grow naturally with their content but remain visually consistent
* **Visually balanced** – avoids floating tiny boxes or massive full-width ones
* **Aligned design** when using multiple boxes on the same screen
* Works seamlessly with **responsive layouts**

So remember... just because you have the width, doesn't mean you should use it. Your UI will feel polished and intentional.
