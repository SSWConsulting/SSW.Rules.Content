---
seoDescription: I'd be happy to help you generate an SEO description. Please provide the Markdown or MDX content, "and" I'll do my best to create a concise, keyword-rich, and user-intent-matching description. 😊
type: rule
title: Do you know all the cool stuff you can do on SSW Rules?
uri: rule
authors:
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
  - title: Sebastien Boissiere
    url: https://ssw.com.au/people/sebastien-boissiere
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - do-you-understand-the-value-of-consistency
  - add-useful-and-concise-figure-captions
created: 2021-01-20T05:06:33.000Z
archivedreason: null
guid: 55db32aa-0718-4868-995c-673d8dd69f62
---

This is an example rule + Markdown cheatsheet to give you some guidance around how to write rules and show you the things you can use to format an SSW rule.

<!--endintro-->

## Concepts to write rules

There are a few concepts that are applied to structure most SSW Rules:

1. **Show the pain** - Usually in the intro, explain the problem and context around why that rule exists
2. **Give good and bad examples** - Include practical examples for people to better understand the concepts. [Using images is usually the best way to go](/use-images-to-replace-words)
3. **Explain the why, not the how** - A rule isn't a place to document how to use a 3rd party product. You should focus on the reasons **why** we do something, and then link to external documentation on **how** to do something

See a few examples of SSW Rules that follow the structure of good and bad examples, then link off to external documentation for more information:

* [GitHub Issues - Do you use Issue Templates?](/github-issue-templates)
* [Bicep - Do you use User-defined Data Types?](/bicep-user-defined-data-types)
* [Do you know how to backup data on SQL Azure?](/do-you-know-how-to-backup-data-on-sql-azure)

### 1. Headings, paragraphs, and blockquotes

```markdown
## This is a heading 2 

### This is a heading 3

#### This is a heading 4

##### This is a heading 5

###### This is a heading 6 and below is a blockquote

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.  
> \- Someone famous
```

**Figure: Markdown to generate headings and blockquotes**

::: info
Do **not** use Heading 1 (`<h1>`) in the content, even with the good intention of improving SEO. The page title already uses `<h1>`, and adding more can harm accessibility and semantic structure. As per [MDN guidelines - avoid multiple `<h1>` elements on the same page](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements#avoid_using_multiple_h1_elements_on_one_page).
:::

## This is a heading 2

Lorem ipsum dolor sit amet. Ut enim ad minim veniam, quis nostrud exercitation. qui officia deserunt mollit anim id est laboru.

## This is a heading 2 with some **emphasized text** by making it bold

**Tip:** See [text decoration section](#2-text-decorations) for more details on making the text bold.

### This is a heading 3

Lorem ipsum dolor sit amet. Ut enim ad minim veniam, quis nostrud exercitation. qui officia deserunt mollit anim id est laboru.

#### This is a heading 4

Lorem ipsum dolor sit amet. Ut enim ad minim veniam, quis nostrud exercitation. qui officia deserunt mollit anim id est laboru.

##### This is a heading 5

Lorem ipsum dolor sit amet. Ut enim ad minim veniam, quis nostrud exercitation. qui officia deserunt mollit anim id est laboru.

###### This is a heading 6

Lorem ipsum dolor sit amet. Ut enim ad minim veniam, quis nostrud exercitation. qui officia deserunt mollit anim id est laboru.

...and this is a blockquote:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.
>
> \- Someone famous

---

### 2. Text decorations

```markdown
_This text will be italic._  

**And this text will be bold.**

~~strikethrough.~~

_You **can** combine them_.

<mark>These words</mark> are surrounded by a &lt;mark&gt; (HTML needed).
```

**Figure: Markdown to generate different text styles**

_This text will be italic._  

**And this text will be bold.**

~~strikethrough.~~

_You **can** combine them_.

<mark>These words</mark> are surrounded by a &lt;mark&gt; (HTML needed).

---

### 3. Lists

```markdown
#### Unordered lists

- This is the first item of an unordered list
- This is the second item of an unordered list
  1.  This is the first item of an ordered list inside an unordered list
  2.  This is the second item of an ordered list inside an unordered list
- This is the third item of an unordered list
  - This is the first item of an unordered list inside another
  - This is the second item of an unordered list inside another
    1. This is the first item of an ordered list inside a nested unordered list
    2. This is the second item of an ordered list inside a nested unordered list

#### Ordered lists

1. This is the first item of an ordered list
2. This is the second item of an ordered list
3. This is the third item of an ordered list
   - This is the first item of an unordered list inside an ordered list
   - This is the second item of an unordered list inside an ordered list
     1. This is the first item of an ordered list inside another
     2. This is the second item of an ordered list inside another
```

**Figure: Markdown to generate lists**

#### Unordered lists

* This is the first item of an unordered list
* This is the second item of an unordered list
  1. This is the first item of an ordered list inside an unordered list
  2. This is the second item of an ordered list inside an unordered list
* This is the third item of an unordered list
  * This is the first item of an unordered list inside another
  * This is the second item of an unordered list inside another
    1. This is the first item of an ordered list inside a nested unordered list
    2. This is the second item of an ordered list inside a nested unordered list

#### Ordered lists

1. This is the first item of an ordered list
2. This is the second item of an ordered list
3. This is the third item of an ordered list
   * This is the first item of an unordered list inside an ordered list
   * This is the second item of an unordered list inside an ordered list
     1. This is the first item of an ordered list inside another
     2. This is the second item of an ordered list inside another

---

### 4. Links

```md
[link text](https://www.url.com "link title")
```

**Figure: Markdown to generate links**

This is [an internal link](https://www.ssw.com.au).

This is [an internal link with title](https://www.ssw.com.au "This is a link title") (hover me).

This is [an external link](https://www.google.com).

::: greybox
**Cool link features:**

* We use [icons on files' links](/use-icons-to-not-surprise-users) to not to surprise users
* Our main headings auto-generated [anchor links](/anchor-links) so users can easily access a section of a long page like this one.
   E.g. To go straight to this section of the page, you can access [https://ssw.com.au/rules/rule/#4-links](#4-links)

:::

---

### 5. Boxes

```md
::: greybox  
This is a box using the class "greybox".  
:::
```

**Figure: Markdown to generate boxes**

::: greybox  
This is a box using the class "greybox".  
:::

::: highlight  
This is a box using the class "highlight".
:::

::: info  
This is a &lt;div&gt; using the class "info". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.  
:::

::: china  
This is a &lt;div&gt; using the class "china". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  
:::

::: codeauditor
This is a &lt;div&gt; using the class "codeauditor". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  
:::

::: todo  
This is a &lt;div&gt; using the class "todo". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.  
:::

#### Hiding content

Use the class "hidden" to hide content.

```md
::: hidden  
bfb265e3-644e-4cbe-b17c-4d378b014809-7947936  
:::
```

**Figure: Nothing will show up from this Markdown**

---

### 6. Images

```md
::: class
![Figure: Caption text](image-file.jpg)
:::
```

#### Classes for images

::: img-small  
![Figure: Image using class "img-small"](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

::: img-medium  
![Figure: Image using class "img-medium"](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

::: img-large  
![Figure: Image using class "img-large"](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

::: no-border
![Figure: Image using class "no-border"](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

#### Extra examples

![Figure: How a smaller image (400px) works with long caption. Full screen on mobile, real width on larger screens...](https://images.unsplash.com/photo-1528820454441-189cd70a6c3c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80)

![Figure: ...and with a short caption](https://images.unsplash.com/photo-1528820454441-189cd70a6c3c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80)

::: todo  
TODO: Make these images hosted internally as per [Do you make sure your images are hosted internally?](/images-should-be-hosted-internally)
:::

---

### 7. Captions

```md
::: bad  
Figure: Caption for bad examples
:::

::: ok  
Figure: Caption for OK examples
:::

::: good  
Figure: Caption for good examples
:::
```

#### Captions on images

::: bad  
![Figure: Caption for bad images](https://images.unsplash.com/photo-1542014740373-51ad6425eb7c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

![Figure: Caption for regular images](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)

::: ok  
![Figure: Caption for OK images](https://images.unsplash.com/photo-1478998674531-cb7d22e769df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

::: good  
![Figure: Caption for good images](https://images.unsplash.com/photo-1491472253230-a044054ca35f?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)
:::

#### Captions on boxes

::: greybox  
This is an example of a bad grey box.  
:::  
::: bad  
Figure: Caption for bad examples
:::

::: greybox  
This is an example of a normal grey box.
:::  
**Figure: Caption for normal examples**

::: greybox  
This is an example of a OK grey box.
:::  
::: ok  
Figure: Caption for ok examples  
:::

::: greybox  
This is an example of a good grey box.
:::  
::: good  
Figure: Caption for good examples  
:::

---

### 8. Videos

#### Code for videos

```md
`youtube: https://www.youtube.com/embed/0ugMkda9IBw`
**Video: Top 5 Reasons Why ASP.NET MVC is Great (3 min)**
```

**Figure: Markdown to add videos and video captions**

#### Example

Check out this video - it's responsive!

`youtube: https://www.youtube.com/embed/0ugMkda9IBw`
**Video: Top 5 Reasons Why ASP.NET MVC is Great (3 min)**

---

### 9. Twitter Cards Embed

Embedding a Tweet is similar to a video. Copy the link of the tweet then add it to the rule with backticks on each side like this:

```md
`oembed: https://twitter.com/MrHinsh/status/24123713864`
```

`oembed: https://twitter.com/MrHinsh/status/24123713864`

---

### 10. Code

To include code block in Markdown, start with 3 backticks <code>```</code> on a new line, write or paste your code, and then end with 3 backticks on a new line.

For syntax highlighting in code blocks, add the language name right after the opening backticks. Learn more on [Markdown – Do you set the language on code blocks?](/set-language-on-code-blocks)

To add inline code in Markdown, wrap the code snippet with single backticks. See `this text` as inline code for example.

```md
This is a piece of code in a code block
```

::: bad  
Figure: Bad example - Because this code doesn't include the language used
:::

See this [json file](https://unpkg.com/gatsby-remark-vscode@1.0.3/lib/grammars/manifest.json) for all supported languages and their aliases we can use in SSW Rules. See some examples:

```javascript
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  alert("Yay, I love chocolate ice cream!");
} else {
  alert("Awwww, but chocolate is my favorite...");
}
```

**Figure: Javascript code block**

```sql
IF EXISTS (SELECT 1 FROM
               INFORMATION_SCHEMA.TABLES
           WHERE
               TABLE_TYPE='BASE TABLE' AND
               TABLE_NAME='Employees'
           )
    ALTER TABLE [dbo].[Employees]( …… ) ON [PRIMARY]
ELSE
    CREATE TABLE [dbo].[Employees]( …… ) ON [PRIMARY]
```

**Figure: SQL code block**

```cs
public class MyClass
{
    public string  myField = string.Empty;

    public MyClass()
    {
    }

    public void MyMethod(int parameter1, string parameter2)
    {
        Console.WriteLine("First Parameter {0}, second parameter {1}",
                                                    parameter1, parameter2);
    }

    public int MyAutoImplementedProperty { get; set; }

    private int myPropertyVar;

    public int MyProperty
    {
        get { return myPropertyVar; }
        set { myPropertyVar = value; }
    }
}
```

**Figure: C Sharp code block**

```json
{
  "glossary": {
    "title": "example glossary",
    "GlossDiv": {
      "title": "S",
      "GlossList": {
        "GlossEntry": {
          "ID": "SGML",
          "SortAs": "SGML",
          "GlossTerm": "Standard Generalized Markup Language",
          "Acronym": "SGML",
          "Abbrev": "ISO 8879:1986",
          "GlossDef": {
            "para": "A meta-markup language, used to create markup languages such as DocBook.",
            "GlossSeeAlso": ["GML", "XML"]
          },
          "GlossSee": "markup"
        }
      }
    }
  }
}
```

**Figure: JSON code block**

---

### 11. Email Templates

#### Code for email template

```md
::: email-template  
| | |
| -------- | --- |
| To: | XXX |
| Cc: | YYY |
| Bcc: | ZZZ |
| Subject: | {{ EMAIL SUBJECT }} |  
::: email-content

### Hi XXX,

{{ EMAIL CONTENT }}

:::  
:::  
::: good  
Figure: Good example - Nice email template  
:::
```

**Figure: Markdown for email templates**

::: email-template

|          |                     |
| -------- | ------------------- |
| To:      | XXX                 |
| Cc:      | YYY                 |
| Bcc:     | ZZZ                 |
| Subject: | {{ EMAIL SUBJECT }} |

::: email-content

### Hi XXX

{{ EMAIL CONTENT }}

:::  
:::  
::: good  
Figure: Good example - Nice email template  
:::

---

### 12. Tables

#### Code for tables

```md
| Tables        |      Are      |   Cool |
| ------------- | :-----------: | -----: |
| col 3 is      | right-aligned | \$1600 |
| col 2 is      |   centered    |   \$12 |
| zebra stripes |   are neat    |    \$1 |
```

**Figure: Markdown to generate tables**

#### Examples

| Tables        |      Are      |   Cool |
| ------------- | :-----------: | -----: |
| col 3 is      | right-aligned | \$1600 |
| col 2 is      |   centered    |   \$12 |
| zebra stripes |   are neat    |    \$1 |

| Markdown | Less      | Pretty     |
| -------- | --------- | ---------- |
| _Still_  | `renders` | **nicely** |
| 1        | 2         | 3          |

---

### 13. Thematic breaks (horizontal rules)

#### Code for hr

```md
---
```

#### Examples

---
