---
type: rule
archivedreason: 
title: Do you look for large strings in code?
guid: 87a0ae0c-61c1-4d99-9b96-86786795f7e0
uri: do-you-look-for-large-strings-in-code
created: 2012-04-01T09:17:55.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---


<p>Long hard-coded strings in a codebase can be a sign of poor architecture.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​To make hard-coded strings easier to find, <a href="/do-you-highlight-strings-in-your-code-editor">consider highlighting them in your IDE</a>.</p>
<img class="ms-rteCustom-ImageArea" src="LongStringBadExample.png" alt="longstringbadexample.png" /><br>
<span class="ssw-rteStyle-FigureBad">Figure: Bad Example - The connection string is hard-coded and isn't easy to see in the IDE.</span>
<img class="ms-rteCustom-ImageArea" src="longstringbadexample2.png" alt="longstringbadexample2.png" />
<span class="ssw-rteStyle-FigureBad">Figure: Better Example - The connection string is still hard-coded, but at least it's very visible to the developers.</span>
<img class="ms-rteCustom-ImageArea" src="ShortStrings.png" alt="longstringgood.png" />
<span class="ssw-rteStyle-FigureGood">Figure: Good Example - The connection string is now stored in configuration and we don't have a long hard-coded string in the code.</span>


