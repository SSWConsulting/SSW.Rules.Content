---
seoDescription: Enhance your markdown by adding syntax highlighting to code blocks for improved readability and easier debugging.
type: rule
title: Do you set the language on code blocks?
uri: set-language-on-code-blocks
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: null
created: 2021-03-23T00:01:00.000Z
archivedreason: null
guid: 1f4e6b03-d6d3-45ca-9a8f-9595f3ff5fd5
---

You should have a syntax highlighter to show pieces of code on your pages for a better readability. By specifying the language within your code block, you can enable color coding similar to that in an IDE.

Tools like [Prism](https://prismjs.com), [highlight.js](https://highlightjs.org), or [Code Prettify](https://github.com/googlearchive/code-prettify) automatically apply syntax highlighting, making it easier for users to read code by color-coding different elements (e.g., keywords, strings, and variables).

<!--endintro-->

::: info
See this [json file](https://unpkg.com/gatsby-remark-vscode@1.0.3/lib/grammars/manifest.json) for all supported languages and their aliases that can be used in SSW Rules.
:::

To activate this feature, add the language name right after the opening 3 backticks (used to [write a code in Markdown](https://www.ssw.com.au/rules/rule/#11-code)).

For example, instead of starting a **JavaScript** code example with: **&#96;&#96;&#96;**, you should use **&#96;&#96;&#96;js** or **&#96;&#96;&#96;javascript** for syntax highlighting.

```none
let iceCream = 'chocolate';

if (iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```

::: bad
Figure: Bad example - No syntax highlighting
:::  

```javascript
let iceCream = 'chocolate';

if (iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```

::: good
Figure: Good example - This JavaScript code block shows its syntax highlighted
:::

::: codeauditor
[SSW CodeAuditor enforces this rule](https://codeauditor.com/rules).
:::
