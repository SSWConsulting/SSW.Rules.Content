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


<p class="ssw15-rteElement-P">Writing CSS is easy. Writing a lot of CSS can become unwieldy and unmanageable. Using&#160;CSS pre-processors like LESS or SCSS&#160;helps you segment and organize your CSS logically and compiles down to regular CSS so there are extra steps to get up and running.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>The&#160;key advantage of using&#160;CSS pre-processors&#160;is nested selectors. Instead line after line of specific CSS selectors you can nest them and they will compile down for you. Check out this example&#58;​</p><dl class="badImage"><dt><img src="/PublishingImages/RulesLESS%20-%20css.png" alt="RulesLESS - css.png" /></dt><dd>Bad Example&#58; Using regular CSS, you repeat yourself a lot</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/RulesLESS%20-%20less.png" alt="RulesLESS - less.png" /></dt><dd>Good Example&#58; Using LESS, we can structure our CSS better<br></dd></dl><p>The pre-processed​ CSS then&#160;compiles&#160;to the regular CSS shown above.<br></p><p>We recommend using SCSS for its slightly more robust language scripting, however, the <a href="https&#58;//css-tricks.com/sass-vs-less/">differences between LESS and SCSS are minor</a>.<br><br></p>


