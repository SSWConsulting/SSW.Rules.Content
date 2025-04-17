---
seoDescription: Add quotation marks to make them easily identifiable and improve readability by starting a new line with indentation.
type: rule
archivedreason:
title: Do you format quotations to stand out from the main text?
guid: 0212ab54-f936-4d72-a690-c9276ded3cc6
uri: style-quotations
created: 2016-04-21T04:15:15.0000000Z
authors:
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
related:
  - format-new-lines
  - commas-and-full-stops-always-should-have-1-space-after-them
  - use-quotation-mark-for-controls
  - indent
redirects:
  - do-you-know-how-to-make-quotations-easier-to-identify
  - how-to-add-quotations
---

Quotations should never blend into the rest of your message. Whether you're responding to an email or writing content for the web, formatting quotations clearly helps readers understand what’s being quoted and what's your original content.

<!--endintro-->

Generally, the best practice is to always **start a quote on a new line and indent it**, making it visually distinct and easy to follow.

::: greybox
Software development can be painful and costly. Hang on, that should say "Software development **is** painful and costly"  
:::
::: bad
Figure: Bad example - The quotation is mixed up with main text  
:::

::: greybox
Software development can be painful and costly. Hang on, that should say:

&nbsp;&nbsp;&nbsp;"Software development **is** painful and costly"  
:::
::: good
Figure: Good example - The quotation has quote marks, on a new line and indented  
:::

::: greybox
Software development can be painful and costly. Hang on, that should say:

&nbsp;&nbsp;&nbsp;> Software development **is** painful and costly  
:::
::: good
Figure: Good example - The quotation has greater-than sign, on a new line and indented  
:::

## 🖥️ For Web UI

In web design, it’s important to make quotations stand out from surrounding text. You should:

* Place the quote on a new line
* Use quotation marks for clarity
* Style it visually with a different font style, spacing, italics, or borders

Use the semantic `<blockquote>` HTML tag to indicate a quotation, and apply CSS to enhance visibility.

**HTML example:**

```html
<blockquote>
  “Design is not just what it looks like and feels like. Design is how it works.” – Steve Jobs
</blockquote>
```

**CSS example:**

```css
blockquote {
    border-left: 4px solid #f5f5f5;
    margin-top: 1rem;
    padding: 1rem;
}
```

**Markdown example:**

If you're using Markdown, simply prefix the quoted text with a `>` symbol, and it will automatically render as a blockquote:

```md
> "Design is not just what it looks like and feels like. Design is how it works."
```

This is how it renders:

> "Design is not just what it looks like and feels like. Design is how it works."

## 📧 For emails / IM 

In email or IM replies, quoting previous messages is essential for context. The standard convention is to prefix quoted lines with a greater-than symbol `>`, which makes the quoted text clearly identifiable — even in plain-text emails.

**Email reply example:**

::: email-template  

| | |
| -------- | --- |
| To: | Bob |
| Subject: | Northwind - April report |  
::: email-content

### Hi Bob

&nbsp;&nbsp;&nbsp; > Can you send the report by Friday?
Sure! I’ll send it over by end of day.

:::  
:::  

This simple formatting makes conversations easier to follow, especially in long email threads.
