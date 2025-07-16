---
seoDescription: Do you leverage your AI conversations to turn discussions into documentation?
type: rule
archivedreason:
title: Do you use AI to turn discussions into documentation?
guid: c73f2949-72ed-4562-8e3c-3cf03e0403ba
uri: ai-assisted-artifacts
created: 2025-07-16T10:43:28.0000000Z
authors:
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
related: []
redirects:

---

All projects come with their share of documentation overhead. While your usual [awesome documentation](/awesome-documentation) artifacts like READMEs, architecture maps, and the F5 Experience, don't change too often, you will often find yourself writing [Architectural Decision Records (ADRs)](/architectural-decision-records), sequence diagrams, and Wiki pages that track important decisions and directions throughout the SDLC.

But the last thing any developer wants to do is write and maintain this documentation. In enterprise organisations, many of these artifacts have strict formatting requirements and data points that must be met, which takes an already tedious task and throws it firmly into the "maybe some other time" bucket.

But with a minor shift in process, you can use AI to transform your brainstorming and problem-solving sessions into quality documentation that would bring a tear of joy to your BA's eye.

<!--endintro-->

## Giving AI the context
The key to quality artifacts is quality information. If you're brainstorming a given problem with AI from the get-go, chances are you've already provided it a huge amount of context around the current problem statement, possible solutions and trade-offs that need to be considered, while finally settling on a recommended approach to put forward to the team.

If you're working collaboratively with other developers in a workshop environment, then you need a way to let AI "listen in" on the discussion. It's recommended to record these conversations through Microsoft Teams or a similar tool, and then leverage AI assistants like [SSW YakShaver](https://yakshaver.ai), [Sembly](https://sembly.ai), or [Tactiq](https://tactiq.io/) to pull out the relevant pieces of information into a summary. If none of those are an option, you can pull the entire transcript down and use it un-summarized, but beware of token bloat (and not-safe-for-documentation comments!).

Regardless of which method you use, you end up with the all-important context you need in order to document the outcomes. The only difference now is getting AI to do the hard work!

## Generating the artifacts
Whether it's an ADR, sequence diagram, or a Wiki page, there should be a consistent template that dictates what each artifact should look like. This is what you can feed into your AI of choice, along with the context, and have it generate the relevant artifacts for you.

## ADRs are important to get right... Can I trust it?
While nothing AI does is a guaranteed victory, this method has produced fantastic results in the real-world. Many of SSW's architects use this productivity hack to take the gruntwork out of document generation, and some of the crazier ones are even trying to automate the entire process! If you'd like to see an example of how this whole process looks like, check out Gordon Beeming's [From Conversation to Documentation](https://gordonbeeming.com/blog/2025-06-26/from-conversation-to-documentation-a-modern-dev-workflow-with-ai) blog post.