---
type: rule
archivedreason: 
title: Do you import namespaces and shorten the references?
guid: 0bf92b2c-b378-4e05-bd4c-d91f783138ac
uri: do-you-import-namespaces-and-shorten-the-references
created: 2018-04-25T22:28:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- import-namespaces-and-shorten-the-references

---

You should import namespaces and shorten the references.

<!--endintro-->



```
System.Text.StringBuilder myStringBuilder = new System.Text.StringBuilder();
```



::: bad
Figure: Bad code - Long reference to object name

:::



```
using System.Text;
...
...
StringBuilder myStringBuilder = new StringBuilder();
```



::: good
Figure: Good code - Import the namespace and remove the repeated System.Text reference

:::



If you have ReSharper installed, you can let ReSharper take care of this for you:


::: ok  
![Figure: Right click and select "Reformat Code..."](ReSharperReformatCode.gif)  
:::


::: ok  
![Figure: Make sure "Shorten references" is checked and click "Reformat"](ReSharperShortenReferences.gif)  
:::
