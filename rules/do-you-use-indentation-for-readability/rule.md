---
type: rule
title: Do you use indentation for readability?
uri: do-you-use-indentation-for-readability
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Paul Neumeyer
    url: https://ssw.com.au/people/paul-neumeyer
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - when-you-reply-inline-do-you-use-a-different-color
redirects: []
created: 2010-09-01T02:53:29.000Z
archivedreason: null
guid: 1899c3db-ac1b-468e-a8e7-f2cdc5e0748a
---
Written communication can easily cause misunderstandings. Help the reader understand your message better by:

* Using “&gt;” and indentation when quoting the text from others, like the original email you are replying to, or a web page, etc.
* Your new text should be kept to the left
* Optionally, [use a different text color in your reply](/when-you-reply-inline-do-you-use-a-different-color)
* Add numbers if the sender didn't and it is appropriate

<!--endintro-->

This way you won't forget any questions in the original email.

::: email-template
|          |     |
| -------- | --- |
| To:      | Adam |
| Subject: | RE: Change on Northwind app |
::: email-content  

### Hi Adam,

Please change from X to Y\
The program flow logic worries me a bit\
Done. Sorry, this wasn't a final decision - I just put it there for testing purposes 

:::
:::
::: bad
Figure: Bad Example - there's too much information here
:::

::: email-template
|          |     |
| -------- | --- |
| To:      | Adam |
| Subject: | RE: Change on Northwind app |
::: email-content  

### Hi Adam,

     &gt; 1. Please change from X to Y\
Done - \[add a link to the page or a screenshot];

     &gt; 2. The program flow logic worries me a bit\
Sorry, this wasn't a final decision - I just put it there for testing purposes  

:::
:::
::: good
Figure: Good Example - You can clearly see the context of each part of the reply
:::

::: greybox
**Note:** 

* When using Outlook, the raw “>” character may be automatically formatted to a “>” bullet point. This change is a problem because it may change to a normal bullet point after being sent. To prevent this issue, press Control+Z to turn it back into the raw “>” character.
* For those using mobile devices the indentation function is not available, try instead using 3 spaces to indent manually. 
  :::

## GitHub

When using GitHub, you can use 4 spaces to indent a task and get clear separation between task and response. You can also use a "&gt;" symbol to achieve a similar result.

![Figure: How to write indentations with GitHub in Markdown](githubindentwrite.jpg "How to write indentations with GitHub in Markdown")

![Figure: Preview of different ways to add indentations in GitHub](githubindentpreview.jpg "Preview of different ways to add indentations in GitHub")

You can find more info about GitHub syntax at [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

- - -

`youtube: https://www.youtube.com/embed/LAqRokqq4jI`

<!--StartFragment-->

**Video: Top 10+ Rules to Better Email Communication with Ulysses Maclaren**

<!--EndFragment-->