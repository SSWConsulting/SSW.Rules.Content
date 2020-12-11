---
type: rule
archivedreason: 
title: Do you always use a CSS preprocessor language over plain CSS, such as LESS or SCSS?
guid: 1c97ba66-aaf3-4d40-a6f3-73adf21540f8
uri: do-you-always-use-a-css-preprocessor-language-over-plain-css-such-as-less-or-scss
created: 2014-06-18T05:34:37.0000000Z
authors:
- id: 37
  title: Ben Cull
- id: 1
  title: Adam Cogan
- id: 20
  title: Rebecca Liu
related: []

---

Writing CSS is easy. Writing a lot of CSS can become unwieldy and unmanageable. Using CSS pre-processors like LESS or SCSS helps you segment and organize your CSS logically and compiles down to regular CSS so there are extra steps to get up and running.

<!--endintro-->

The key advantage of using CSS pre-processors is nested selectors. Instead line after line of specific CSS selectors you can nest them and they will compile down for you. Check out this example:
<dl class="badImage">&lt;dt&gt;<img src="RulesLESS - css.png" alt="RulesLESS - css.png">&lt;/dt&gt;<dd>Bad Example: Using regular CSS, you repeat yourself a lot</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="RulesLESS - less.png" alt="RulesLESS - less.png">&lt;/dt&gt;<dd>Good Example: Using LESS, we can structure our CSS better<br></dd></dl>
The pre-processed CSS then compiles to the regular CSS shown above.

We recommend using SCSS for its slightly more robust language scripting, however, the [differences between LESS and SCSS are minor](https://css-tricks.com/sass-vs-less/).
