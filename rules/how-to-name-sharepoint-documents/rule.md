---
type: rule
archivedreason: 
title: Do you know how to name documents?
guid: fd6b589b-9f74-4d95-bc4f-b90b4c349c31
uri: how-to-name-sharepoint-documents
created: 2019-02-26T01:04:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Matt Wicks 
  url: https://ssw.com.au/people/matt-wicks
related: 
- do-you-know-how-to-use-sharepoint-search
- use-dashes-in-urls
- remove-spaces-from-your-folders-and-filename
redirects:
- do-you-know-how-to-name-documents

---

When naming documents, use **kebab-case** to separate words to make your files more easily discoverable.

<!--endintro-->

### Avoid spaces

::: greybox
Monthly Report.docx
:::
::: bad
Bad example: File name uses a space to separate words
:::

As far as search goes, using spaces is actually a usable option. What makes spaces less-preferable is the fact that the URL to this document will have those spaces escaped with the sequence %20. E.g. **sharepoint/site/library/Monthly%20Report.docx**. URLs with escaped spaces are longer and less human-readable. 

Know more on [Do you remove spaces from your folders and filename?](/remove-spaces-from-your-folders-and-filename)

### Avoid CamelCase

::: greybox
MonthlyReport.docx
:::
::: bad
Bad example: CamelCase - File name doesn't have spaces but also doesn't contain any separators between words
:::

This is a popular way to combine words as a convention in variable declarations in many coding languages, but shouldn't be used in document names as it is harder to read. Also, a file name without spaces means that the search engine doesn't know where one word ends and the other one begins. This means that searching for 'monthly' or 'report' might **not** find this document.

### Avoid Snake_Case

::: greybox
Monthly_Report.docx
:::
::: ok
Figure: OK example - underscored (Snake\_Case) URLs have good readability but are not recommended by Google
:::

Underscores are not valid word separators for search in SharePoint, and not recommended by others. Also, sometimes underscores are less visible to users, for example, when a hyperlink is underlined. When reading a hyperlink that is underlined, it is often possible for the user to be mistaken by thinking that the URL contains spaces instead of underscores. For these reasons it is best to avoid their use in file names and titles.

### Use kebab-case

::: greybox
monthly-report.docx
:::
::: good
Good Example: kebab-case - File name uses dashes to separate words
:::

A hyphen (or dash) is the best choice, because it is understood both by humans and all versions of SharePoint search.

:::info
You may use Uppercase in the first letter in Kebab-Case, however it's important to keep consistency
:::

### Extra

- **Add relevant metadata where possible**

If a document library is configured with metadata fields, add as much relevant information as you can. Metadata is more highly regarded by search than the contents within documents, so by adding relevant terms to a documents metadata, you will almost certainly have a positive effect on the relevance of search results.

- **Use descriptive file names and titles**

The file name and title is regarded more highly by search than the content within documents. Also, the title or file name is what is displayed in the search results, so by making it descriptive, you are making it easier for people who perform searches to identify the purpose of your document.
