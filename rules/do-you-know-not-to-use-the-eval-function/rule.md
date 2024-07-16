---
seoDescription: Avoid using inefficient "eval" functions in JavaScript, instead refer to global variables by concatenating variable names with strings.
type: rule
archivedreason:
title: Do you know not to use the "eval" function?
guid: 68d543a0-b55d-4d09-a3e0-107664a9e3cc
uri: do-you-know-not-to-use-the-eval-function
created: 2012-07-24T18:13:38.0000000Z
authors:
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
  - do-you-know-not-to-use-the-＂eval＂-function
---

The Javascript command "eval" evaluates the content of a text string and then runs it as Javascript code. It's common to see it around, however "eval" is one of the most inefficient constructs that JavaScript has. There are always more efficient ways to code and get a direct reference.

<!--endintro-->

Most of people that use "eval" want part of a variable name to be variable.

Once you realize that all global variables are held in the window array it becomes rather obvious that you can refer to that same field name without needing to use "eval" by referring to it.

eval('somevar' + num)

Figure: Bad example - The developer creates the variable name by concatenating the constant and variable parts together

window['somevar' + num]

Figure: Good example - Referencing the same field is as simple to code and more efficient than using "eval"
