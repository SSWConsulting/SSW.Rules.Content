---
type: rule
title: Do you use chain of density prompts for summarization?
uri: chain-of-density
authors:
  - title: Seth Daily
    url: https://www.ssw.com.au/people/seth-daily
related:
  - summarize-long-conversations
  - fundamentals-of-prompt-engineering
  - critical-agent
created: 2023-09-19T00:00:00Z
archivedreason: null
guid: b962b722-e7a8-42ed-b045-f8f2e4c7bd1b
---

If you have a lot of text to sum up, it can be time consuming to extract the most important parts. If you want a simple way to keep the important stuff, you should use chain of density (CoD).

<!--endintro-->

## What is Chain of Density?

CoD prompting is a useful way to reduce the chances that ChatGPT makes mistakes when summarizing text. It works automatically with one prompt. [Studies have shown](https://arxiv.org/pdf/2309.04269.pdf) that CoD summaries are preferable to normal GPT-4 summaries.

When you give it the prompt, it will:

* Add important stuff step by step
* Critique itself to check quality
* Improve its own summary

Here's an example prompt you can use to do CoD - the only thing you need to to is paste the text you want summarized into the {{ ARTICLE }} placeholder:

::: greybox
"Article: {{ ARTICLE }}  
You will generate increasingly concise, entity-dense summaries of the above article.  

Repeat the following 2 steps 5 times.  

Step 1. Identify 1-3 informative entities (";" delimited) from the article which are missing from the previously generated summary.  
Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the missing entities.

A missing entity is:

* relevant to the main story,
* specific yet concise (5 words or fewer),
* novel (not in the previous summary),
* faithful (present in the article),
* anywhere (can be located anywhere in the article).

Guidelines:

* The first summary should be long (4-5 sentences, ~80 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach ~80 words.
* Make every word count: rewrite the previous summary to improve flow and make space for additional entities.
* Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
* The summaries should become highly dense and concise yet self-contained, i.e., easily understood without the article.
* Missing entities can appear anywhere in the new summary.
* Never drop entities from the previous summary. If space cannot be made, add fewer new entities.

Remember, use the exact same number of words for each summary."
:::

Depending on how dense of a summary you want, you may want to take the outputs from step 2, 3, or 4, instead of 5.
