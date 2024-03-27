---
type: rule
title: Do you enhance readability with line breaks and spacing?
uri: format-new-lines
authors:
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan/
  - title: Josh Berman
    url: https://www.ssw.com.au/people/josh-berman/
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
  - title: Jayden Alchin
    url: https://ssw.com.au/people/jayden-alchin/
related:
  - add-useful-and-concise-figure-captions
  - use-the-right-html-figure-caption
created: 2021-07-06T01:13:05.707Z
archivedreason: ""
guid: e05522a7-1822-412c-80ee-5619039f7d96

---

Writing in large blocks of text is a common practice, but it can hinder readability. Incorporating line breaks and spacing significantly enhances content readability. This allows readers to navigate through the text more easily, absorb information more effectively, and stay engaged with the material.

<!--endintro-->

::: info
**Warning:** In web pages (HTML/Markdown), line breaks **should not be used to to create layout spacing** - it is a bad practice. You should use CSS margins and paddings to achieve that.
Learn more on [HTML br Tag: The Dos and Don'ts of Adding an HTML Line Break](https://blog.hubspot.com/website/html-line-break).

See the [Markdown Guide](https://www.markdownguide.org/basic-syntax/#line-breaks) for more information on line breaks in Markdown.

When referring to **emails** and/or **informal documents**, line breaks can be used for spacing. In these cases, correct syntax is not crucial and breaking a line is easier than dealing with margins/line spacing.
:::

### Long paragraphs

### Notes, Tips, PS

Content elements like **Note**, **Tip**, **PS** (and similar) should be on a new line to enable better readability. It is beneficial to bold those words.

::: greybox
Test the login functionality thoroughly. Note: Try both valid and invalid credentials.
:::
::: bad  
Figure: Bad example - No line break before the note
:::

::: greybox
Test the login functionality thoroughly.
**Note:** Try both valid and invalid credentials.
:::
::: good  
Figure: Good example - The "Note" being on a fresh line and in bold makes it much easier to read
:::

### Images and captions

It is recommended to include spaces after an image or a figure description.

::: info
In web, always rely on CSS margins to achieve this.
:::

### URLs

Breaking a line is also recommended before URLs.

::: greybox
Check out these employment opportunities at SSW: <https://www.ssw.com.au/employment#available>
:::
::: bad  
Figure: Bad example - No line break before the URL
:::

::: greybox
Check out these employment opportunities at SSW:
<https://www.ssw.com.au/employment#available>
:::
::: good  
Figure: Good example - The URL being on a fresh line makes it much easier to read
:::

### Headings

It's a good idea to have some space after headings.

::: greybox
Hey Bob,
Check out this awesome new video about the SSW Cultural Exchange Program!
:::
::: bad  
Figure: Bad example - No spacing after heading
:::

::: greybox
Hey Bob,

Check out this awesome new video about the SSW Cultural Exchange Program!
:::
::: good  
Figure: Good example - Spacing after heading
:::

### Multiple items should be a list

If you text has information divided in multiple items, it should be a list. For example, when sending PBIs.

::: greybox
Hey Adam,

I have 2 PBIs on my next to-do in the coming sprint: Product Backlog Item 88994: Performance | Create a new App Service plan and Product Backlog Item 88823: Azure | Create a new App Service Plan in West US for SL production resource group. I will do the IoC after.
:::
::: bad  
Figure: Bad example - Block of text
:::

::: greybox
Hey Adam,

I have 2 PBIs in this Sprint:

* PBI 88994: Performance | Create a new App Service plan
* PBI 88823: Azure | Create a new App Service Plan in West US for SL production resource group

I will do the IoC after.

:::
::: good  
Figure: Good example - List is used to make information easier to digest
:::

**Note:** On the example above, see how changing from "Product Backlog Item" to "PBI" also helps with readability.
