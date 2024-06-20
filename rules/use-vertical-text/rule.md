---
type: rule
archivedreason:
title: Data Layout - Do you take advantage of vertical text to avoid lots of thin columns?
guid: 84531bc9-6ec3-41c8-aab1-20e60958957f
uri: use-vertical-text
created: 2024-06-05T19:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - when-to-use-reporting-services
redirects: []

---

When a report has many columns and each column contains small amount of data, it is a good idea to use vertical text for the column headers.
<!--endintro-->

By changing the WriteMode of a text box from:

```sql
 lr-tb (left to right, top to bottom)
```

To

```sql
 tb-lr (top to bottom, left to right)
```

...your text will become vertical, and you save lots of space.

::: bad  
![Figure: Bad example - Not using vertical text for headings, when you have lots of thin columns](RS_VerticalText_1.gif)  
:::

::: ok  
![Figure: OK example - Not using ticks and crosses](RS_VerticalText_2.gif)  
:::

Take it to the next level by using emojis in your report.

::: good  
![Figure: Good example - Use emojis to improve the quality of your report](RS_VerticalText_3.gif)
:::

Emojis can add visual interest and make your report more engaging and easier to interpret at a glance.

**Note:** Microsoft have not given us the option of having the vertical text bottom to top. It would be easier to read. This suggestion has been added to Suggestions for Microsoft RS.
