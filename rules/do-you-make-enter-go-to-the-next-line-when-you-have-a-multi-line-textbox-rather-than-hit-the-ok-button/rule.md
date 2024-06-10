---
seoDescription: When designing a multi-line text box in a form, make the "Enter" key go to the next line instead of pressing the OK button.
type: rule
title: Do you make "Enter" go to the next line when you have a multi-line
  textbox rather than hit the OK button?
uri: do-you-make-enter-go-to-the-next-line-when-you-have-a-multi-line-textbox-rather-than-hit-the-ok-button
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T06:52:00.000Z
guid: 441436ff-d142-48e8-b057-c225060259c9
---

If you have a multi-line textbox in a form, you should make the "Enter" key go to the next line in the text box, rather than cause it to hit the OK button.

<!--endintro-->

::: bad
![Figure: Bad example - "Enter" button causes OK button to be pressed instead of going to next line in the multi-line text box](developernotesscreen1.gif)
:::

::: good
![Figure: Good example - "Enter" button goes to the next line in the text box](developernotesscreen2.gif)
:::

It can be done by assigning "True" value to AcceptsReturn and Multiline options in properties bar.

![Figure: Developer Notes properties details](setupformtxt2.gif)
