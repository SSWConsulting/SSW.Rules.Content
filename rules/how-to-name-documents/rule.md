---
seoDescription: Mastering document naming conventions is crucial for effective SharePoint search and file discovery. Use descriptive words and kebab-case (hyphens) to make your files easily searchable.
type: rule
title: Do you know how to name documents/files?
uri: how-to-name-documents
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
  - zz-files
redirects:
  - do-you-know-how-to-name-documents
  - how-to-name-sharepoint-documents
created: 2019-02-26T01:04:10.000Z
archivedreason: null
guid: fd6b589b-9f74-4d95-bc4f-b90b4c349c31
---

When naming documents and images, use **descriptive words** and **kebab-case** (where you separate words with hyphens) to make your files more easily discoverable.

<!--endintro-->

## Naming files

Following good practices when naming files ensures clarity, consistency, and efficiency, whether working individually or in a team.

### ❌ Avoid special characters

Refrain from using special characters like / \ ? % * : | " < >. These can cause errors on certain systems.

### ✅ Use relevant words

The file name and its title is regarded more highly by search than the content within documents. Also, the file name is what is displayed in search results, so by making it descriptive you are making it easier for people to identify the purpose of your document.

## Formatting file names

Once you have chosen the best words, make it readable and consistent in formatting:

### ❌ Avoid spaces

As far as search goes, using spaces is actually a usable option. What makes spaces less-preferable is the fact that the URL to this document will have those spaces escaped with the sequence %20. E.g. **sharepoint/site/library/Monthly%20Report.docx**. URLs with escaped spaces are longer and less human-readable.

::: greybox
Monthly Report.docx
:::
::: bad
Figure: Bad example - File name using spaces to separate words
:::

Know more on [removing spaces from your folders and file names](/remove-spaces-from-your-folders-and-filename).

### ❌ Avoid unnecessary dots

Avoid using dots within filenames, as they can lead to potential issues with system processing, file recognition, and software compatibility. Dots are typically used to separate the name from the file extension (e.g., "document.pdf"), so additional dots can confuse systems, causing misinterpretation of the file type or errors when accessing the file

::: greybox
monthly.report.docx
:::
::: bad
Figure: Bad example - File name using dots to separate words
:::

::: info
**Note:** `.drawio.svg` and `.drawio.png` are valid svg/png images that contain an embedded **Draw.io** diagram. For these files, the extra dot is OK. More information on [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio).
:::

### ❌ Avoid CamelCase

::: greybox
MonthlyReport.docx
:::
::: bad
Figure: Bad example - File name using CamelCase doesn't have spaces but also doesn't contain any separators between words
:::

This is a popular way to combine words as a convention in variable declarations in many coding languages, but shouldn't be used in document names as it is harder to read. Also, a file name without spaces means that the search engine doesn't know where one word ends and the other one begins. This means that searching for 'monthly' or 'report' might **not** find this document.

### ❌ Avoid Snake_Case

::: greybox
Monthly_Report.docx
:::
::: ok
Figure: OK example - Underscored (Snake_Case) URLs have good readability but are not recommended by Google
:::

Underscores are not valid word separators for search in SharePoint, and not recommended by others. Also, sometimes underscores are less visible to users, for example, when a hyperlink is underlined. When reading a hyperlink that is underlined, it is often possible for the user to be mistaken by thinking that the URL contains spaces instead of underscores. For these reasons it is best to avoid their use in file names and titles.

### ✅ Use kebab-case

::: greybox
monthly-report.docx
:::
::: good
Figure: Good Example - File name uses kebab-case (dashes to separate words)
:::

A hyphen (or dash) is the best choice, because it is understood both by humans and all versions of SharePoint search.

:::info
You may use Uppercase in the first letter in Kebab-Case, however it's important to keep consistency.
:::

### ✅ Use leading zeros for numbered files

::: greybox
1-introduction.docx
10-summary.docx
2-design.docx
:::
::: bad
Figure: Bad example - Files without leading zeros sort incorrectly
:::

::: greybox
01-introduction.docx
02-design.docx
10-summary.docx
:::
::: good
Figure: Good example - Files with leading zeros sort correctly
:::

If a file name begins with a number and it's used for ordering or organisation, pad it with leading zeros (e.g. 01, 02 instead of 1, 2). This ensures files sort in the correct logical order when ordered by name.

## Extra

* **Never use capitalized letters in file extensions** - It can lead to compatibility issues and potential confusion across different operating systems and platforms. For example, saving an image as "image.JPG" instead of "image.jpg" might result in it not displaying correctly on certain platforms or being misinterpreted by software that is case-sensitive. Always use lowercase for consistency and reliability.

* **Ensure file names are unique** - Within a team, there may be a mix of operating systems being used by its members. For users on MacOS or other OS's that have case-sensitive filenames, it's crucial to ensure that filenames are unique. For example, don't use 'File.txt' if 'file.txt' already exists. This is especially important if these files are being tracked with Git, as it can cause issues for users on Windows, which has case-insensitive filenames.

* **Add relevant metadata where possible** - If a document library is configured with metadata fields, add as much relevant information as you can. Metadata is more highly regarded by search than the contents within documents, so by adding relevant terms to a documents metadata, you will almost certainly have a positive effect on the relevance of search results.
