---
type: rule
title: Markdown – Do you set the language on code blocks?
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

Examples:

* [Prism](https://prismjs.com)
* [highlight.js](https://highlightjs.org)

<!--endintro-->

::: info
See this [json file](https://unpkg.com/gatsby-remark-vscode@1.0.3/lib/grammars/manifest.json) for all supported languages and their aliases we can use in SSW Rules.
:::

To activate this feature, add the language name right after the opening [3 backticks used to write a code in Markdown](https://www.ssw.com.au/rules/rule/#11-code). For example, instead of starting a JavaScript code example with just <code>\`\`\`</code>, you should use <code>\`\`\`js</code> or <code>\`\`\`javascript</code> for highlighting.

::: bad

```none
let iceCream = 'chocolate';

if (iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```
  
Figure: Bad example - No syntax highlighting
:::  

::: good

```javascript
let iceCream = 'chocolate';

if (iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```

Figure: Good example - This JavaScript code block shows its syntax highlighted
:::

::: codeauditor
[SSW CodeAuditor enforces this rule](https://codeauditor.com/rules).
:::
