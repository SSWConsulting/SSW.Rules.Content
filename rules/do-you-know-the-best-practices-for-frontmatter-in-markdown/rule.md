---
type: rule
title: Do you know the best practices for Frontmatter in markdown?
uri: do-you-know-the-best-practices-for-frontmatter-in-markdown
authors:
  - title: Gert Marx
    url: https://www.ssw.com.au/people/gert-marx/
  - title: Ozair Ashfaque
    url: https://www.ssw.com.au/people/ozair-ashfaque/
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks/
created: 2023-10-30T23:25:28.835Z
guid: 7c0bb2bb-06b7-45a7-a3a5-5b1b27f7fef2
---

Frontmatter is a critical component in markdown files, especially when generating static sites or handling content management. It allows authors and developers to embed metadata directly at the beginning of a markdown document. This metadata can include information about the document's title, author, date, and other attributes. A well-structured Frontmatter ensures that the markdown processor can quickly extract the necessary metadata and use it for various purposes, like generating page titles or categorizing posts.

However, when not structured properly, it can lead to parsing errors, inconsistencies, and even disrupt the rendering of the entire page. To avoid these pitfalls and ensure a seamless integration of your markdown files, it's essential to follow best practices when defining Frontmatter.

<!--endintro-->

### Use Key-Value Pair Organization

Frontmatter is metadata serialized into a plain text format primarily yaml but can also be toml, or json. In Frontmatter, each key represents an attribute, like the title or the author, and the value associated with it provides specific information related to that attribute.

- **Keys** are always strings and should be descriptive enough to indicate the type of data they hold
- **Values** can be strings, numbers, dates, or even arrays, depending on the data you're representing

Using key-value pairs ensures a standardized format, which in turn makes it easier for both humans and machines to read and interpret the data. Moreover, this structured approach ensures that markdown processors can reliably extract and utilize the metadata, whether it's for rendering a webpage title, categorizing posts, or any other function.
However, avoid non-standard practices like mixing data types or adding unnecessary complexity:

```md
–––
title+author: My Article by John
2023-10-31
–––
```

::: bad
Figure: Bad example - Non-standard practices can lead to parsing errors and inconsistencies
:::

```md
–––
title: My Article
author: Bob Northwind
date: 2023-10-31
–––
```

::: good
Figure: Good example - Clear key-value pairs make it easy to understand and extract the metadata
:::

### Use Arrays for Complex Data

Arrays in Frontmatter are particularly useful when you have to represent multiple values for a single attribute. In markdown, an array is essentially a list of values that are associated with a common key.

- **Why Use Arrays?** Sometimes, a single key might have multiple associated values. Instead of creating multiple keys, or stringing values together, arrays provide a clean and organized method to capture this complex data
- **Accessibility:** Arrays make it straightforward for markdown processors to loop through multiple values, making tasks like generating a list of tags or authors on a webpage much simpler
- **Flexibility:** Arrays can hold strings, numbers, or even other objects, giving you a versatile tool to represent complex structures

However, avoid the common mistake of listing values in a continuous string. This format is harder to parse, and you lose the distinct advantage of the array's structure:

```md
–––
authors: John Doe, Jane Smith, Bob Johnson
–––
```

::: bad
Figure: Bad example - Listing values in a string reduces clarity and makes data extraction challenging
:::

Here's how you can effectively use arrays:

```md
–––
authors: 
  - Bob Northwind
  - Jane Smith
  - Bob Johnson
–––
```

::: good
Figure: Good example - Using arrays helps in listing multiple values under a single key efficiently
:::

### Use Meaningful Keys

The keys you choose for your Frontmatter should be meaningful and descriptive. They act as identifiers for the associated values, so it's essential that they clearly convey the data they represent.

- **Descriptive Names:** Instead of using `desc`, use `description`. Instead of `auth`, use `author`
- **Consistency:** Stick to a consistent naming convention, whether it's camelCase, snake_case, or kebab-case

Avoid non-descriptive keys:

``` md
–––
t: My Article
auth: Bob Northwind
–––
```

::: bad
Figure: Bad example - Shortened or unclear keys can lead to confusion
:::

Use clear, meaningful keys:

``` md
–––
title: My Article
author: Bob Northwind
–––
```

::: good
Figure: Good example - Descriptive keys make Frontmatter easy to understand and work with
:::

### Use Explicit Datatypes

It's crucial to be explicit about datatypes in Frontmatter. This clarity helps markdown processors understand how to handle the provided metadata correctly.

- **Strings vs. Numbers:** If you're representing a year, use a number, e.g., `2023`. If you're mentioning a title or name, use a string, e.g., `"My Article"`
- **Booleans:** For binary choices, like true or false, use booleans. For example, `published: true`

Avoid ambiguous datatypes:

``` md
–––
year: '2023'
published: "yes"
–––
```

::: bad
Figure: Bad example - Ambiguous datatypes can lead to parsing errors
:::

Be explicit with your datatypes:

``` md
–––
year: 2023
published: true
–––
```

::: good
Figure: Good example - Explicit datatypes ensure accurate data representation and extraction
:::

### Avoid Inline HTML

While markdown allows the integration of inline HTML, it's recommended to avoid using it within Frontmatter. Using HTML can lead to rendering issues, especially when the markdown is processed by static site generators or other tools.

- **Simplicity:** Sticking to markdown syntax within Frontmatter keeps the metadata clean and straightforward
- **Portability:** By avoiding HTML, you ensure that the Frontmatter remains compatible with various markdown processors and platforms

However, some might try to use HTML for additional formatting or structure:

``` md
–––
title: <em>My</em> Article
author: <strong>Bob Northwind</strong>
–––
```

::: bad
Figure: Bad example - Using inline HTML can cause unexpected rendering or parsing issues
:::

Stick to plain markdown:

``` md
–––
title: "My Article"
author: 
  - name: "Bob Northwind"
    role: "Writer"
published: true
year: 2023
tags: 
  - Technology
  - Writing
  - Markdown
metadata: 
  created_at: "2023-10-30"
  modified_at: "2023-11-06"
–––
```

::: good
Figure: Good example - Keeping Frontmatter free of HTML ensures consistent rendering
:::
