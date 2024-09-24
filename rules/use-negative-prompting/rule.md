---
type: rule
archivedreason:
title: Do you use negative prompting?
guid: 5819b6ee-c0b5-4ada-bd04-71897ea7b668
uri: use-negative-prompting
created: 2023-06-30T00:00:00.000Z
authors: 
- title: Seth Daily
  url: https://www.ssw.com.au/people/seth-daily/
- title: Rick Su
  url: https://www.ssw.com.au/people/rick-su
related:
- when-to-use-ai-generated-images
- how-to-generate-an-ai-image
- the-best-ai-image-generators
- write-an-image-prompt
- use-parameters-in-your-image-prompts

---

Sometimes you might be trying to create a specific type of image, and the AI keeps including pieces that you don't want. A straightforward way to get around this problem is by including what you DON'T want in your prompt.

<!--endintro-->

## What is negative prompting?

Negative prompting is specifying what you don't want in your image. It guides the AI away from certain features that you're not interested in. Some AI image generators (e.g. Midjourney and Dreamstudio) have this option as a [parameter](/use-parameters-in-your-image-prompts/). In others (e.g. DALLE-2), you can include it in your prompt.

Imagine you are using Midjourney to generate a photo of an emplty highway in the mountains.

::: greybox
“A highway in the mountains”
:::

::: bad  
Figure: Bad example - When you use this prompt, Midjourney keeps putting cars on the highway!
:::

This is when it can be helpful to include a negative prompt. In Midjourney, this is done by using two dashes. (see [Midjourney parameter list](https://docs.midjourney.com/docs/parameter-list))

::: greybox
“A highway in the mountains --no cars”
:::

::: good  
Figure: Good example - The prompt with '--no cars' is more likely to eliminate cars in the picture.
:::
