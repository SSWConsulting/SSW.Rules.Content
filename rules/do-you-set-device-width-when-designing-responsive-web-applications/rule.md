---
type: rule
title: Do you set device width when designing responsive web applications?
uri: do-you-set-device-width-when-designing-responsive-web-applications
created: 2014-06-21T03:26:58.0000000Z
authors:
- id: 37
  title: Ben Cull

---



<span class='intro'> When designing a responsive website, you need to make sure that the browser understands how to correctly render your website. Device-Width informs the browser what the size of the viewport should be. </span>

<p>Since we want our website to render corectly for all screen sizes, we specify that it should set the viewport to the size of the device's screen.<br></p>
<pre class="language-html" style="margin-bottom&#58;24px;padding&#58;1em;border-width&#58;0px 0px 0px 6px;border-left-style&#58;solid;font-family&#58;consolas, monaco, 'andale mono', monospace;font-size&#58;14px;line-height&#58;19px;overflow&#58;auto;color&#58;#4d4e53;text-shadow&#58;none;direction&#58;ltr;word-break&#58;normal;">&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width&quot; /&gt;​</pre><p>​This ensures the browser always renders at the correct resolution for the device.</p>


