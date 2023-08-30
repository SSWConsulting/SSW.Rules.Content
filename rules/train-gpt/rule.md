---
type: rule
title: When should you train GPT?
uri: train-gpt
authors:
  - title: Calum Simpson
    url: https://www.ssw.com.au/people/calum-simpson
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2023-02-08T04:53:29.524Z
guid: c655297f-eeea-41ca-beda-b1f9c27c7cdd
redirects:
  - train-gpt-3
---
GPT is an awesome product, that can do a lot out-of-the-box.

However, sometimes that out-of-the-box model doesn't do what you need it to do.

In that case, you need to apply extra training (aka fine tuning).

<!--endintro-->

Usually, for common scenarios GPT will already be adequate, but for more complex or highly specific use cases, it will not have the required training to output what you need.

For example, if you want to build an app that outputs SSW rules based on a title, the untrained model probably won't know what SSW Rules are so you need to train it.

::: bad
![Figure: Bad example - the untrained GPT model doesn't know what format to create a rule in](untrainedgpt3badexample.png.png)
:::

::: good
![Figure: Good example - the trained GPT model knows how to format the rule, and the style rules are written in](trainedgpt3goodexample.png)
:::
