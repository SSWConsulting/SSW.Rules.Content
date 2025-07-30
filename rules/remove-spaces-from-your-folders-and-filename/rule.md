---
seoDescription: Do not add spaces on folders and files names to ensure seamless URL translation and avoid technical issues. Use kebab-case with dashes between words for a more readable and URL-friendly naming convention.
type: rule
archivedreason:
title: Do you avoid using spaces in folder and file names?
guid: 77003d23-7544-4bbe-92b9-48eae917d4a0
uri: remove-spaces-from-your-folders-and-filename
created: 2018-04-23T21:58:29.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related:
  - how-to-name-sharepoint-documents
redirects:
  - do-you-remove-spaces-from-your-folders-and-filename
---

It is **not** a good idea to have spaces in a folder or file name as they don't translate to URLs very well and can even cause technical problems.

Instead of using spaces, we **recommend**:

* **kebab-case** - using dashes between words

Other **not recommended** options include:

* **CamelCase** - using the first letter of each word in uppercase and the rest of the word in lowercase
* **snake_case** - using underscores between words

For further information, read [Do you know how to name documents?](/how-to-name-sharepoint-documents)

<!--endintro-->

This rule should apply to any file or folder that is on the web. This includes Azure DevOps Team Project names and SharePoint Pages.

::: greybox

* extremeemailsversion1.2.doc
* Extreme Emails version 1.2.doc

:::
::: bad
Figure: Bad examples - File names have spaces or dots
:::

::: greybox

* extreme-emails-v1-2.doc
* Extreme-Emails-v1-2.doc

:::
::: good
Figure: Good examples - File names have dashes instead of spaces
:::

::: greybox

* sharepoint&#46;ssw&#46;com&#46;au/Training/UTSNET/Pages/UTS%20NET%20Short%20Course&#46;aspx
* fileserver/Shared%20Documents/Ignite%20Brisbane%20Talk&#46;docx

:::
::: bad
Figure: Bad examples - File names have been published to the web with spaces so the URLs look ugly and are hard to read  
:::

::: greybox

* sharepoint&#46;ssw&#46;com&#46;au/Training/UTS-NET/Pages/UTS-NET-Short-Course&#46;aspx
* fileserver/Shared-Documents/Ignite-Brisbane-Talk&#46;docx"

:::
::: good
Figure: Good examples - File names have no spaces so are much easier to read
:::
