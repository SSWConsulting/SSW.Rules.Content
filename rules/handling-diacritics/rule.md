---
seoDescription: Multilingual search features require handling diacritics to ensure accurate matches and a seamless user experience.
type: rule
archivedreason:
title: Do you know how to handle diacritics?
guid: 0d0c5084-5b42-45e0-afb5-c6f886d791ea
uri: handling-diacritics
created: 2024-03-13T14:38:37.0000000Z
authors:
  - title: Chloe Lin
    url: https://ssw.com.au/people/chloe-lin
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related: []
---

Imagine you're developing a search feature for a multilingual website. When a user searches for a term like "résumé", but the database contains variations like "resume" without accented characters, it leads to missed matches and incomplete search results. Furthermore, this lack of normalization can introduce inconsistencies in sorting and filtering, complicating data analysis and user navigation.

Implementing character normalization by converting accented and special characters to their closest unaccented equivalents allows terms like "résumé" to match "resume" enhancing search accuracy and overall user experience by addressing these multilingual nuances.

This is especially important for internationalization and for sites to serve users worldwide effectively, regardless of linguistic differences.

<!--endintro-->

### Handling diacritics in JS

JavaScript provides us with a handy method called [normalize()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize) that helps us tackle this problem effortlessly.

The method takes an optional parameter specifying the normalization form. The most common form is the Unicode Normalization Form Canonical Decomposition (NFD), which is suitable for most use cases.

See [Unicode equivalence](https://en.wikipedia.org/wiki/Unicode_equivalence)

Let's see how we can use it:

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

### Handling diacritics in .NET

You can also achieve the same result in .NET using a similar method [Normalize()](<https://learn.microsoft.com/en-us/dotnet/api/system.string.normalize?view=net-8.0#system-string-normalize(system-text-normalizationform)>):

```csharp
string accentedString = "résumé";
string normalizedString = RemoveDiacritics(accentedString);

static string RemoveDiacritics(string accentedString)
{
    Regex Diacritics = new Regex(@"\p{M}");    // A regex that matches any diacritic.
    string decomposedString = accentedString.Normalize(NormalizationForm.FormD);   // Equivalent to NFD
    return Diacritics.Replace(decomposedString, string.Empty);
}

Console.WriteLine(normalizedString);    // Output: resume
```

Voila! With just two line of code, we've transformed the accented "résumé" into its standard English form "resume". Now, the search functionality can accurately match user queries regardless of accents.

::: greybox
**Note:**
While this method often ensures uniformity and handles characters with multiple representations, it may not function as expected for non-diacritic characters such as 'æ' or 'ø'. In such cases, it may be necessary to use a library or manually handle these characters.
:::
