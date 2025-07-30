---
seoDescription: Use quotation marks to clarify controls and enhance user understanding in technical documentation, improving searchability and readability.
type: rule
archivedreason:
title: Do you know how to format UI elements in technical documentation?
guid: a7a66734-2449-487c-ba14-def26cff8da9
uri: formatting-ui-elements
created: 2016-04-21T02:57:12.0000000Z
authors: 
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - distinguish-keywords-from-content
  - do-you-know-how-to-make-quotations-easier-to-identify
redirects:
  - reference-do-you-use-quotation-mark-for-controls
  - use-quotation-mark-for-controls
---

When writing technical instructions, it's important to distinguish UI controls, buttons, and labels from regular text to improve readability and maintain consistency.

<!--endintro-->

::: greybox
Click Save to store your changes.
:::
::: bad
Figure: Bad Example - It's not clear that "Save" is a control  
:::

## Option 1: Bold

Best for UI elements like buttons, labels, or menu options.

**Tip:** See [how to add bold in Markdown](/rule/#2-text-decorations).

::: greybox
Click **Save** to store your changes.
:::
::: good
Figure: Good example - Using bold for buttons and menu options
:::

## Option 2: Quotation marks (quotes)

Best for exact texts users must enter/type; but can also used for UI elements like buttons, labels, or menu options.

::: greybox
Type "Admin" in the **Username** field.
:::
::: good
Figure: Good example - Using quotes for exact text users should type
:::

## Option 3: Code formatting

Ideal for commands, or file names.

**Tip:** See [how to use code formatting in Markdown](/rule/#10-code).

::: greybox
Enter the command `git clone https://github.com/user/repo.git`
:::
::: good
Figure: Good example - Using quotation marks for exact text users may type
:::
