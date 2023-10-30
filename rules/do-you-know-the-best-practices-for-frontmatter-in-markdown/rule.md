---
type: rule
title: Do you know the best practices for Frontmatter in markdown?
uri: do-you-know-the-best-practices-for-frontmatter-in-markdown
authors:
  - title: Gert Marx
    url: https://www.ssw.com.au/people/gert-marx/
  - title: Ozair Ashfaque
    url: https://www.ssw.com.au/people/ozair-ashfaque/
created: 2023-10-30T23:25:28.835Z
guid: 7c0bb2bb-06b7-45a7-a3a5-5b1b27f7fef2
---
### Do you know the best practices for Frontmatter in markdown?

Frontmatter is a critical component in markdown files, especially when generating static sites or handling content management. It allows authors and developers to embed metadata directly at the beginning of a markdown document. This metadata can include information about the document's title, author, date, and other attributes. A well-structured Frontmatter ensures that the markdown processor can quickly extract the necessary metadata and use it for various purposes, like generating page titles or categorizing posts. 

However, when not structured properly, it can lead to parsing errors, inconsistencies, and even disrupt the rendering of the entire page. To avoid these pitfalls and ensure a seamless integration of your markdown files, it's essential to follow best practices when defining Frontmatter.

<!--endintro-->

#### Key-Value Pairs

Frontmatter in markdown primarily utilizes key-value pairs to represent metadata. Each key represents an attribute, like the title or the author, and the value associated with it provides specific information related to that attribute.

- **Keys** are always strings and should be descriptive enough to indicate the type of data they hold.
- **Values** can be strings, numbers, dates, or even arrays, depending on the data you're representing.

Using key-value pairs ensures a standardized format, which in turn makes it easier for both humans and machines to read and interpret the data. Moreover, this structured approach ensures that markdown processors can reliably extract and utilize the metadata, whether it's for rendering a webpage title, categorizing posts, or any other function.

::: greybox
```
---
title: My Article
author: John Doe
date: 2023-10-31
---
```
:::

::: good 
Figure: Good Example {Clear key-value pairs make it easy to understand and extract the metadata.} 
:::

However, avoid non-standard practices like mixing data types or adding unnecessary complexity:

::: greybox
```
---
title+author: My Article by John
2023-10-31
---
```
:::

::: bad 
Figure: Bad Example {Non-standard practices can lead to parsing errors and inconsistencies.} 
:::


#### Using Arrays for Complex Data

Arrays in Frontmatter are particularly useful when you have to represent multiple values for a single attribute. In markdown, an array is essentially a list of values that are associated with a common key.

- **Why Use Arrays?** Sometimes, a single key might have multiple associated values. Instead of creating multiple keys, or stringing values together, arrays provide a clean and organized method to capture this complex data.
  
- **Accessibility:** Arrays make it straightforward for markdown processors to loop through multiple values, making tasks like generating a list of tags or authors on a webpage much simpler.

- **Flexibility:** Arrays can hold strings, numbers, or even other objects, giving you a versatile tool to represent complex structures.

Here's how you can effectively use arrays:

::: greybox
```
---
authors: 
  - John Doe
  - Jane Smith
  - Bob Johnson
---
```
:::

::: good 
Figure: Good Example {Using arrays helps in listing multiple values under a single key efficiently.} 
:::

However, avoid the common mistake of listing values in a continuous string. This format is harder to parse, and you lose the distinct advantage of the array's structure:

::: greybox
```
---
authors: John Doe, Jane Smith, Bob Johnson
---
```
:::

::: bad 
Figure: Bad Example {Listing values in a string reduces clarity and makes data extraction challenging.} 
:::