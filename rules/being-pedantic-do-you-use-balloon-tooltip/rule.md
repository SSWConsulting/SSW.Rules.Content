---
type: rule
archivedreason: "RE: Tiago's feedback on unnecessary rules "
title: Being Pedantic - Do you use balloon tooltip?
guid: cd45a275-e7fe-4a7c-bc1e-1b9f17b00bea
uri: being-pedantic-do-you-use-balloon-tooltip
created: 2012-11-27T09:23:38.0000000Z
authors: []
related: []
redirects: []

---

The standard tooltip is a rectangle, so the tool tip for the control can be misleading. While, the balloon tooltip has an arrow pointing to the destination control, which is clearer for users.

<!--endintro-->


::: bad  
![Figure: Standard tooltip.](../../assets/BadTooltip.gif)  
:::


::: good  
![Figure: Balloon tooltip.](../../assets/GoodTooltip.gif)  
:::

To implement you can:

1. Set the standard Tooltip's property IsBalloon true or
2. Use EdwardForgacs' balloon tooltip control.
