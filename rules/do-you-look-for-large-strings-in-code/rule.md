---
type: rule
title: Do you look for large strings in code?
uri: do-you-look-for-large-strings-in-code
created: 2012-04-01T09:17:55.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>Long hard-coded strings in a codebase can be a sign of poor architecture.</p> </span>

<p>​To make hard-coded strings easier to find, <a href="/do-you-highlight-strings-in-your-code-editor">consider highlighting them in your IDE</a>.</p>
<img class="ms-rteCustom-ImageArea" src="/PublishingImages/LongStringBadExample.png" alt="longstringbadexample.png" /><br>
<span class="ssw-rteStyle-FigureBad">Figure&#58; Bad Example - The connection string is hard-coded and isn't easy to see in the IDE.</span>
<img class="ms-rteCustom-ImageArea" src="/PublishingImages/longstringbadexample2.png" alt="longstringbadexample2.png" />
<span class="ssw-rteStyle-FigureBad">Figure&#58; Better Example - The connection string is still hard-coded, but at least it's very visible to the developers.</span>
<img class="ms-rteCustom-ImageArea" src="/PublishingImages/ShortStrings.png" alt="longstringgood.png" />
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - The connection string is now stored in configuration and we don't have a long hard-coded string in the code.</span>


