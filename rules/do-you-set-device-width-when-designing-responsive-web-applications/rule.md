---
type: rule
title: Do you set device width when designing responsive web applications?
uri: do-you-set-device-width-when-designing-responsive-web-applications
authors:
  - title: Ben Cull
    url: https://ssw.com.au/people/ben-cull
  - title: Jayden Alchin
    url: https://ssw.com.au/people/jayden-alchin
related:
  - responsive-design
redirects: []
created: 2014-06-21T03:26:58.000Z
archivedreason: null
guid: 28fc4b70-6cd7-4106-947e-82f2452630a5
---
Creating a responsive website? It's important to make sure the browser renders your content correctly on any screen size. Define the proper viewport meta tag to inform web browsers they need to behave responsively.

<!--endintro-->

```html
<meta name="viewport" content="width=device-width" />
```
Your website's viewport should be the same width as any given device's screen. Specify this with the content attribute `_device-width_`. 

::: bad  
![Figure: Bad example - No viewport meta tag](viewport-bad.png)
:::

::: good  
![Figure: Good example - Correct viewport meta tag](viewport-good.png)
:::

### Resize Text

The viewport meta tag should **not** set `_user-scaling=no_` or a `_maximum-scaling_` value less than 2. This allows us to meet accessibility standards for scalable content. [See WCAG 1.4.4](https://www.w3.org/WAI/WCAG21/Understanding/resize-text.html).
