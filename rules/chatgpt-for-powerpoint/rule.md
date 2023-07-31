---
type: rule
title: Do you know how to make a PowerPoint presentation using ChatGPT?
uri: chatgpt-for-powerpoint
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
created: 2023-07-31T16:29:02.708Z
guid: 87b105e9-98f7-467e-ad88-7861795bb1d5
---
By now, you’ve probably realised that you can ask ChatGPT to create a content for a PPT, which you can then copy and paste into PowerPoint, but this is still time consuming. The next level is to get it to then create the VBA script that can be run to generate the whole PPT 😀

Here’s a great prompt template for doing both! Feel free to play around with things like the preferred format or title colours.

<!--endintro-->

::: greybox
You are an expert presentation writer and PowerPoint expert.
Write a PowerPoint presentation on {TOPIC}. 
Each slide should have a title and bullet point content. 
Don't give me advice on what to talk about on each slide, instead give me the actual content I can use. 
Then create a VBA script to create the PPT including slide titles and all content on each slide. 
Make the title text on each slide this colour: RGB(204, 65, 65)
Do not save the PPT.
1st, ask for the {TOPIC}
:::

::: good
Figure: Prompt Template for creating a PowerPoint presentation
:::

Then, follow these steps:
1.	Open Microsoft PowerPoint
2.	Make sure you have enabled the developer tab
3.	Click the Developer Tab | Visual Basic (or “Alt L V”)
4.	Click Insert | Module
5.	Paste your code into the text box and press F5 to run it
