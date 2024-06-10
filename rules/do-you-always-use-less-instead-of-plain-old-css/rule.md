---
seoDescription: Writing CSS efficiently and organizing large stylesheets becomes manageable with CSS pre-processors like LESS or SCSS.
type: rule
archivedreason:
title: Do you always use a CSS preprocessor language over plain CSS, such as LESS or SCSS?
guid: 1c97ba66-aaf3-4d40-a6f3-73adf21540f8
uri: do-you-always-use-less-instead-of-plain-old-css
created: 2014-06-18T05:34:37.0000000Z
authors:
  - title: Ben Cull
    url: https://ssw.com.au/people/ben-cull
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Rebecca Liu
    url: https://ssw.com.au/people/rebecca-liu
related: []
redirects:
  - do-you-always-use-a-css-preprocessor-language-over-plain-css-such-as-less-or-scss
---

Writing CSS is easy. Writing a lot of CSS can become unwieldy and unmanageable. Using CSS pre-processors like LESS or SCSS helps you segment and organize your CSS logically and compiles down to regular CSS so there are extra steps to get up and running.

<!--endintro-->

The key advantage of using CSS pre-processors is nested selectors. Instead line after line of specific CSS selectors you can nest them and they will compile down for you. Check out this example:

::: bad  
![Bad Example: Using regular CSS, you repeat yourself a lot](RulesLESS - css.png)  
:::

::: good  
![Good Example: Using LESS, we can structure our CSS better](RulesLESS - less.png)  
:::

The pre-processed CSS then compiles to the regular CSS shown above.

We recommend using SCSS for its slightly more robust language scripting, however, the [differences between LESS and SCSS are minor](https://css-tricks.com/sass-vs-less/).
