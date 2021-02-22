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
related: []
redirects:
- do-you-know-how-to-name-documents

---

When naming documents, use kebab-case to separate words to make your files more easily discoverable.

<!--endintro-->

A file name without spaces means that the search engine doesn't know where one word ends and the other one begins. This means that searching for 'monthly' or 'report' might  **not**  find this document.



```
MonthlyReport.docx
```




::: bad
Bad Example: File name doesn't contain any separators between words


:::
As far as search goes, using spaces is actually a usable option. What makes spaces less-preferable is the fact that the URL to this document will have those spaces escaped with the sequence %20. E.g. https://sharepoint/site/library/Monthly%20Report.docx. URLs with escaped spaces are longer and less human-readable.



```
Monthly Report.docx
```




::: bad
Bad Example: File name uses a space to separate words

:::

Underscores are not valid word separators for search in SharePoint, and not recommended by others. Also, sometimes underscores are less visible to users, for example, when a hyperlink is underlined. When reading a hyperlink that is underlined, it is often possible for the user to be mistaken by thinking that the URL contains spaces instead of underscores. For these reasons it is best to avoid their use in file names and titles.



```
Monthly_Report.docx
```




::: bad
Bad Example: File name uses an underscore (snake\_case) to separate words


:::

A hyphen is the best choice, because it is understood both by humans and all versions of SharePoint search.



```
Monthly-Report.docx
```




::: good
Good Example: File name uses a kebab-case to separate words


:::

### Add relevant metadata where possible

If a document library is configured with metadata fields, add as much relevant information as you can. Metadata is more highly regarded by search than the contents within documents, so by adding relevant terms to a documents metadata, you will almost certainly have a positive effect on the relevance of search results.

### Use descriptive file names and titles

The file name and title is regarded more highly by search than the content within documents. Also, the title or file name is what is displayed in the search results, so by making it descriptive, you are making it easier for people who perform searches to identify the purpose of your document.

### Related Rule


* [Do you know how to use SharePoint search?](/do-you-know-how-to-use-sharepoint-search)
* [Do you use dashes in your URLs?](/use-dashes-in-urls)
