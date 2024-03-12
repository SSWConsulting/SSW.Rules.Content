---
type: rule
archivedreason:
title: Do you know how to handle diacritics?
guid: 0d0c5084-5b42-45e0-afb5-c6f886d791ea
uri: do-you-know-how-to-handle-diacritics
created: 2023-09-14T14:38:37.0000000Z
authors:
  - title: Chloe Lin
    url: https://ssw.com.au/people/chloe-lin
related: []
---

Imagine you're building a search feature for a multilingual website. A user searches for "résumé" , but the database contains entries without accented characters like "resume." Without normalization, these variations might not match, leading to inaccurate search results.

Thankfully, JavaScript provides us with a handy method called "normalize()" that helps us tackle this problem effortlessly.

<!--endintro-->

The method takes an optional parameter specifying the normalization form. The most common form is the Unicode Normalization Form Canonical Deomposition (NFD), which is suitable for most use cases. Let's see how we can use it:

```js
const accentedString = "résumé";
const normalizedString = accentedString
  .normalize("NFD")
  .replace(/\p{Diacritic}/gu, "");

console.log(normalizedString); // Output: resume
```

There are 2 things happening in the code above:

1. **normalize()** converts strings into the NFD. This form decomposes composite characters into the base character and combining characters. E.g. 'é' would be decomposed into 'e' + '´'
2. **replace(/\p{Diacritic}/gu, "")** matches any character with a diacritic mark (accent) and replaces it with an empty string

Voila! With just two line of code, we've transformed the accented "résumé" into its standard English equivalent "resume". Now, the search functionality can accurately match user queries regardless of accents.

**Note:**

While this method often ensures uniformity and handles characters with multiple representations, it may not function as expected for non-diacritic characters such as 'æ' and 'ø'. In such cases, it may be necessary to use a library or handle these characters manually.
