---
seoDescription: Improve readability with proper line breaks and spacing in your content to enhance user engagement and comprehension.
type: rule
title: Do you enhance readability with line breaks and spacing?
uri: format-new-lines
authors:
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Josh Berman
    url: https://www.ssw.com.au/people/josh-berman
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
  - title: Jayden Alchin
    url: https://ssw.com.au/people/jayden-alchin
related:
  - add-useful-and-concise-figure-captions
  - use-the-right-html-figure-caption
  - html-css-do-you-know-how-to-create-spaces-in-a-web-page
created: 2021-07-06T01:13:05.707Z
archivedreason: ""
guid: e05522a7-1822-412c-80ee-5619039f7d96

---

Writing in large blocks of text is a common practice, but it can hinder readability. Incorporating line breaks and spacing significantly enhances content readability. This allows readers to navigate through the text more easily, absorb information more effectively, and stay engaged with the material.

<!--endintro-->

::: info
**Warning:** For web (HTML/Markdown), line breaks **should not be used to to create layout spacing**!
You should [use CSS margin and/or padding](/html-css-do-you-know-how-to-create-spaces-in-a-web-page) instead.

Learn more on [HTML `<br>` Tag: The Dos and Don'ts of Adding an HTML Line Break](https://blog.hubspot.com/website/html-line-break).

See the [more information on line breaks in Markdown](https://www.markdownguide.org/basic-syntax/#line-breaks).

On the other hand, in regards to **emails** and/or **informal documents**, line breaks can be used for spacing. In these cases, correct syntax is not crucial, and breaking a line is more convinient than dealing with margins/line spacing.
:::

## Long paragraphs

Consider breaking lines/paragraphs when you have a long block of text. You should aim to separate the information by context.

::: greybox

SSW is made up of a great team of staff that is passionate about technology and how it meets business needs. Today SSW has offices in Sydney, Melbourne, Brisbane, Newcastle, Strasbourg (France) and Hangzhou (China), with over 100 employees. Want to meet them? Have a look at SSW People.

:::
::: bad  
Figure: Bad example - Long block of text
:::

::: greybox
SSW is made up of a great team of staff that is passionate about technology and how it meets business needs.

Today SSW has offices in Sydney, Melbourne, Brisbane, Newcastle, Strasbourg (France) and Hangzhou (China), with over 100 employees.

Want to meet them? Have a look at SSW People.
:::
::: good  
Figure: Good example - The text is separated by paragraphs
:::

## Callouts

Content elements like **Note**, **Tip**, **PS** (and similar) should be on a new line to enable better readability. It is beneficial to bold those words.

::: greybox
Test the login functionality thoroughly. Note: Try both valid and invalid credentials.
:::
::: bad  
Figure: Bad example - No line break before the note
:::

::: greybox

Test the login functionality thoroughly.\
**Note:** Try both valid and invalid credentials.
:::
::: good  
Figure: Good example - The "Note" being on a fresh line and in bold makes it much easier to read
:::

## URLs

Breaking a line is also recommended before URLs.

::: greybox
Check out these employment opportunities at SSW: <https://www.ssw.com.au/employment#available>
:::
::: bad  
Figure: Bad example - No line break before the URL
:::

::: greybox
Check out these employment opportunities at SSW:  \
<https://www.ssw.com.au/employment#available>

:::
::: good  
Figure: Good example - The URL being on a fresh line makes it much easier to read
:::

::: info
**Tips:** URLs can get cluttered quickly - [keeping them short and clean](/create-friendly-short-urls) makes them easier to read, share, and manage. Whenever possible, it's even better to [use descriptive links](/descriptive-links) instead of full URLs.
:::

## Headings

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

## Multiple items as lists

If you text has information that can be turned into multiple items, you should do so, by creating a list. For example, when sending PBIs for a Sprint.

::: greybox
I have 2 PBIs in the coming Sprint: Product Backlog Item 88994: Performance | Create a new App Service plan and Product Backlog Item 88823: Azure | Create a new App Service Plan in West US for SL production resource group. I will do the IoC after.
:::
::: bad  
Figure: Bad example - Block of text
:::

::: greybox
I have 2 PBIs in the coming Sprint:

* PBI 88994: Performance | Create a new App Service plan
* PBI 88823: Azure | Create a new App Service Plan in West US for SL production resource group

I will do the IoC after.

:::
::: good  

Figure: Good example - List is used to separate information and make it easier to digest
:::

**Note:** On the example above, see how changing from "Product Backlog Item" to "PBI" also helps with readability.
However, you should [only use acronyms when the recipient is familiar with the term](/avoid-acronyms).

## Images and captions

It is also recommended to include spaces after an image or a figure description. These elements need breathing space to help users focus on them.
