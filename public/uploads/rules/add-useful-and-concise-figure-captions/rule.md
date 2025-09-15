---
seoDescription: Enhance your web content by adding useful figure captions to images and videos for better SEO and user engagement.
type: rule
title: Figures - Do you add useful text captions to images and videos?
uri: add-useful-and-concise-figure-captions
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - screenshots-avoid-walls-of-text
  - figures-do-you-use-bad-example-and-good-example-with-ticks-and-crosses-in-captions
  - figures-do-you-use-the-right-html-css-code-to-add-the-useful-figure-caption
  - right-format-to-write-videos-time-length
  - placeholder-for-replaceable-text
redirects:
  - figures-do-you-add-useful-and-concise-figure-text-(aka-a-caption)-to-avoid-a-lot-of-text-over-images
  - add-a-useful-figure-caption-below-all-images
  - show-a-bad-example-and-then-a-good-example
  - figures-do-you-add-useful-and-concise-figure-text
created: 2014-12-04T20:24:03.000Z
archivedreason: null
guid: cb664ecb-4910-4d82-bcbc-47e35cbe89ee
---
When you add images/videos to websites/applications, it is helpful to add a caption underneath them, describing and including extra information to users.

It's a convenient way of catching users' attention to your content. When people are scanning a newspaper, they often check out the pictures first, then read the accompanying description, and if it sounds interesting, they'll go back and read the article. Users read websites in a similar fashion.

<!--endintro-->

To catch readers' attention, include a useful description - don't just describe what the image is... say what it's used for in the context of the document.

It is especially important that images and captions serve a purpose, as opposed to graphics which are there solely for design.

### Tip #1: Use prefixes

Prefix your caption with "Figure: ", "Video: ", "Code: ", or "GIF: "

If it is a good/ok/bad example (see the next tip), then the prefix should be something like: "Figure: Good/Bad/OK example - ", "Video: Good/Bad/OK example - ", or "Code: Good/Bad/OK example - ".

::: info
**Note:** The first word after the dash should be capitalized, and the [caption should not include a full stop](/avoid-full-stops-in-bullet-point-lists/) at the end.

E.g. **Figure: Good example - This is a caption**
:::

### Tip #2: Give bad and good examples

When possible, use "bad" and "good" examples to clearly explain **Dos and don'ts**.

::: info
At SSW we always show the bad example first, then the good example. You will see samples of this in the next tips below.
:::

### Tip #3: Bold your captions

::: greybox
{{ IMAGE }}\
{{ CAPTION }}
:::
::: bad
Figure: Bad example - Caption not bolded can be mixed up with regular content
:::

::: greybox
{{ IMAGE }}\
**{{ CAPTION }}**
:::
::: good
Figure: Good example - Caption stands out when bolded
:::

### Tip #4: Describe the actions in your captions

Especially for screenshots, it is a good idea to have your figure describe the action the user would take:

::: greybox
{{ IMAGE }}\
**Figure: This is the screen**
:::
::: bad
Figure: Bad example - Vague caption description
:::

::: greybox
{{ IMAGE }}\
**Figure: On the screen, choose the execution method**
:::
::: good
Figure: Good example - Clear caption description
:::

### Tip #5: Video captions should be the title + length

When embedding videos, include a caption with **the video title** + **video length** in brackets.

**Note:** As per Tip #1, you should also prefix with "Video: " instead of "Figure: ".

::: greybox
{{ VIDEO }}\
**Figure: Scrum video**
:::
::: bad
Figure: Bad example - Using "Figure:" for a video caption + a vague text
:::

::: greybox
{{ VIDEO }}\
**Video: Intro to Scrum in Under 10 Minutes (9 min)**
:::
::: good
Figure: Good example - Video caption following the standard "Video: {{ VIDEO TITLE }} ({{ VIDEO LENGTH}})"
:::

This helps:

* Giving a brief text summary of the video
* Getting some extra Google Juice
* Letting users know what to expect in terms of time required to watch
* Serving as a reminder in case that video ever gets removed by its owner

::: info
**Note:** The exception is for promotional videos where the caption may undesirably impact the look and feel of your page. If you don't include the video title in the caption, consider adding it above the video as regular content, so it's searchable.
:::

### Tip #6: AI images - include your prompt

If you're sharing an AI generated image, show others how you made it.

::: greybox
{{ IMAGE }}\
**Figure: An AI image of baseball player sliding**
:::
::: bad
Figure: Bad example - Doesn't educate others about AI images
:::

::: greybox
{{ IMAGE }}\
**Figure: An AI image of baseball player sliding. Prompt: A realistic image of a baseball player sliding. The uniform is white and the crowd is cheering.**
:::
::: good
Figure: Good example - Readers understand how you made the image, and they improve their own AI image skills by learning from your caption
:::

### Tip #7: Link people's names to their profiles

When you have someone's name in your caption, link the name to their profiles (e.g. [SSW People profile](https://ssw.com.au/people)).

::: greybox
{{ VIDEO }}\
**Video: In this video, Bob talks about Outlook**
:::
::: bad
Figure: Bad example - A vague text with no link to Bob's profile. Also missing the video length
:::

::: greybox
{{ VIDEO }}\
**Video: How to search on Outlook by [Bob](https://ssw.com.au/people/sample) (2 min)**
:::
::: good
Figure: Good example - A descriptive caption using the video title + profile link + video length at the end
:::

### Tip #8: GIFs - Label accordingly

Using a GIF instead of a static image can be beneficial for illustrating multiple steps, as it saves page space. Be sure to specify that it is a GIF in the caption to distinguish it from a static image

::: greybox
{{ GIF }}\
**Figure: Users | Summary | User Information | LinkedIn URL**
:::
::: bad
Figure: Bad example - Does not specificy that it is a GIF
:::

::: greybox
{{ GIF }}\
**Figure: Animated GIF - Users | Summary | User Information | LinkedIn URL**
:::
::: good
Figure: Good example - Specificies that it is a GIF
:::
