---
type: rule
archivedreason: 
title: Do you look for large strings in code?
guid: 87a0ae0c-61c1-4d99-9b96-86786795f7e0
uri: do-you-look-for-large-strings-in-code
created: 2012-04-01T09:17:55.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady
related: []

---

Long hard-coded strings in a codebase can be a sign of poor architecture.

<!--endintro-->

To make hard-coded strings easier to find, [consider highlighting them in your IDE](/do-you-highlight-strings-in-your-code-editor).

[[badExample]]
| ![The connection string is hard-coded and isn't easy to see in the IDE.](LongStringBadExample.png)
![Better Example - The connection string is still hard-coded, but at least it's very visible to the developers.](longstringbadexample2.png)
[[goodExample]]
| ![The connection string is now stored in configuration and we don't have a long hard-coded string in the code.](ShortStrings.png)
