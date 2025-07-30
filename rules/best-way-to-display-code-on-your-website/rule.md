---
seoDescription: Best way to display code on your website using simple and effective formatting.
type: rule
archivedreason:
title: Do you know how to display code in HTML?
guid: edf8e58b-33bb-42a9-aa9a-85c1ca6b74d1
uri: best-way-to-display-code-on-your-website
created: 2016-08-05T18:57:08.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
  - do-you-know-the-best-way-to-display-code-on-your-website
---

Displaying code on a website is an important aspect of creating developer-friendly content, ensuring the code is clear, readable, and accessible. When done correctly, it enhances user experience and helps avoid confusion.

<!--endintro-->

## The best way to display a piece of code

Use HTML `<code>` and `<pre>` tags:

* The `<code>` tag is used for inline or block-level code snippets that are embedded within other text. It applies minimal styling, indicating that the enclosed content is code. However, it does not preserve formatting like indentation or line breaks
* The `<code>` tag is used to display preformatted text and code blocks where whitespace, line breaks, and indentation are preserved. It’s especially useful for larger code blocks where maintaining the original formatting is essential. This tag ensures that the code appears exactly as written in the source

### Using monospace fonts and syntax highlighting

Code should be displayed using monospace fonts (e.g., Courier, Consolas) to ensure that each character takes up the same space, improving readability.

Tools like Prism.js, Highlight.js, or Google Prettify automatically apply syntax highlighting, making it easier for users to read code by color-coding different elements (e.g., keywords, strings, and variables). Learn more on [Do you set the language on code blocks?](set-language-on-code-blocks)

::: info
**Tip:** Consider scrollbars for long code blocks - When dealing with long code snippets, it's helpful to display them within scrollable containers to maintain page layout without overwhelming the reader.
:::

```html
<font face="Courier, Times, Arial, Verdana" size="3">
  public class Configuration { public static string MySetting { get; } }
</font>
```

::: bad
Figure: Bad example - Using `<font>` with a bad inline styling to display some code
:::

```html
<p>The function <code>console.log()</code> prints messages to the console.</p>
```

::: good
Figure: Good example - Using `<code>` for inline code snippets
:::

```html
<pre>
function greet() {
    console.log("Hello, world!");
}
</pre>
```

::: good
Figure: Good example - Using `<pre>` for code blocks
:::

::: info
**Warning:** Do not use auto-format (Ctrl-K, Ctrl-F) in Visual Studio when updating page with `<pre>` tags, or it will destroy all the code formatting. We have made a suggestion to Microsoft to fix this.
:::
