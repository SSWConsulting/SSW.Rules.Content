---
type: rule
title: Do you know not to use the "eval" function?
uri: do-you-know-not-to-use-the-eval-function
created: 2012-07-24T18:13:38.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>The Javascript command &quot;eval&quot; evaluates the content of a text string and then runs it as Javascript code. It's common to see it around, however &quot;eval&quot; is one of the most inefficient constructs that JavaScript has. There are always more efficient ways to code and get a direct reference.</p> </span>

<p>Most of people that use <span>&quot;eval&quot;<span style="display&#58;inline-block;"></span></span> want part of a variable name to be variable.</p>
<p>Once you realize that all global variables are held in the window array it becomes rather obvious that you can refer to that same field name without needing to use <span>&quot;eval&quot;<span style="display&#58;inline-block;"></span></span> by referring to it.</p>

<div class="ms-rteCustom-CodeArea">
<p>eval('somevar' + num)</p>
</div>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad example - The developer creates the variable name by concatenating the constant and variable parts together</span>

<div class="ms-rteCustom-CodeArea">
<p>window['somevar' + num] </p>
</div>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good example - Referencing the same field is as simple to code and more efficient than using <span></span>&quot;eval&quot;<span></span><span style="display&#58;inline-block;"></span></span>


