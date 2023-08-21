---
type: rule
archivedreason: 
title: Data - Do you avoid spaces and empty lines at the start of character columns?
guid: 848bd3dc-36eb-408f-a216-ce06bb730c54
uri: avoid-spaces-and-empty-lines-at-the-start-of-character-columns
created: 2019-11-25T19:01:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- data-do-you-avoid-spaces-and-empty-lines-at-the-start-of-character-columns

---

Text in character columns (char, varchar, text, nchar, varchar, text) can start with spaces or empty lines which is usually data entry error.

The best way to avoid this issue is to handle whitespace in the middle-tier before it reaches the database.

<!--endintro-->

Here’s an example of removing whitespace and carriage returns in the middle-tier using Regex:

```csharp
static string Trim(string inputText)
{
  Match m = Regex.Match(inputText, @"[^\s]");
  return m.Success ? inputText.Substring(m.Index) : inputText;
}
```

**Figure: C# Removing whitespace and carriage returns in middle-tier** 

The code above:
* Uses Regular Expressions (Regex) to match the first non-whitespace character (includes tabs, spaces, line feeds and carriage returns).
* Retrieves the index of the character
* Returns the text from the character onwards, thus removing the whitespace at the start

This code could be triggered in the middle-tier before inserting into the database.
