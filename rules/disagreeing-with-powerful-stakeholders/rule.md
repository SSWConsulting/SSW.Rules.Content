---
seoDescription: Disagreeing with powerful stakeholders can have a significant impact on project outcomes. Learn how to effectively express your opinions and interests while keeping the conversation focused on the issue.
type: rule
title: Stakeholder Management - Do you know how to disagree with powerful stakeholders?
uri: disagreeing-with-powerful-stakeholders
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair/
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud/
related:
  - fix-problems-quickly
  - for-the-record
created: 2024-03-21T04:59:07.597Z
guid: 2848c2b5-28cc-475f-ab24-0983f8d38b5a
archivedreason: null
---

Disagreeing with powerful stakeholders can have a huge impact. It's always good to speak up, but a poorly worded disagreement can result in misalignment or frustration. That's why it's crucial to frame your messages in a way that ensures ideas are expressed effectively.

`youtube: https://youtu.be/FbtHJm8vFpE?si=GNBJdUdM3QNCpRmx&t=186`
**Video: How to Disagree with Someone More Powerful (watch 3 min from 3:06-5:38)**

Imagine a scenario where you are a Developer on a team and you disagree with the Product Owner about the priority of your PBI - migrating from .NET 6 to .NET 8. The Product Owner is saying they don't want to do it, but you think it's important for this Sprint.

Let's see what tips and tricks can be applied to ensure a smooth discussion.

<!--endintro-->

## Align your interests and understanding

When you have a disagreement with a senior colleague, it's likely that you have different perspectives and understanding. Before you talk about the issue, it's pivotal to check you are on the same page about the issue and looking for a path forward. Here are some tips for doing so:

1. Repeat your understanding of the issue
2. Ask if they're open to feedback
3. Find a common target

#### 1. Repeat your understanding of the issue

By repeating back your understanding of the issue, you can check that their viewpoint aligns with yours, and if there are any discrepancies, they can be caught before the issue is discussed. (aka Steelmanning)

:::greybox
**Developer**: I think you don't want to migrate from .NET 6 to .NET 8 because you want to finish adding single-sign on first. And you consider any security issues to be priority 1. Is that correct?

**Product Owner**: Actually, the reason is because .NET 9 comes out in a few months and I want to wait for that version.
:::
:::good
Good example - The Developer identified that the Product Owner had a different reason than they thought
:::

#### 2. Ask if they're open to feedback

Getting permission to comment is a great tactic. It makes the stakeholder feel empowered to have the conversation and also gives you confidence that they are interested in what you have to say.

:::greybox
**Developer**: Would it be OK if I explain why I think we should upgrade now?

**Product Owner**: Sure!
:::
:::good
Good example - The Developer gives a warning to the Product Owner to check if they are in a moment where they are ready to listen to a dissenting opinion
:::

#### 3. Find a common target

Determine an outcome you both want to see from the solution. That way the conversation centers on delivering business value rather than being contrary for the sake of it.

:::greybox
**Developer**: Lately, our users have been having significant performance issues, and that has been a pain point. Would you agree?

**Product Owner**: Yes, absolutely!

**Developer**: Well, when I read the .NET 8 release notes I saw they have improved performance by 20%. That's why I want to upgrade now.
:::
:::good
Good example - The Developer identified a pain point the Product Owner cares about, strengthens their argument
:::

## Keep the dialog focused on the issue

When talking with a powerful stakeholder it's vital to keep the conversation on track and focused on the issue itself. Here are several strategies you can use:

1. Ground yourself in logic
2. Avoid judgemental language
3. Express that it's your opinion
4. Leave it up to them

#### 1. Ground yourself in logic

When communicating about a problem, emotions can quickly get in the way. You want to project confidence and neutrality - that's why it's critical to try and stick to the logic and facts.

#### 2. Express that it's your opinion

If you caveat that you are just expressing your opinion, others will feel like you are open to discussing the issue rationally and that you understand others may disagree.

:::greybox
**Product Owner**: I don't want to upgrade to .NET 8 this Sprint because I want to wait for .NET 9

**Developer**: No, we should upgrade to .NET 8 this Sprint because it will help fix users' performance issues.
:::
:::bad
Bad example - The Developer didn't express that it was their opinion.
:::

:::greybox
**Product Owner**: [See above]

**Developer**: In my opinion, it's better if we upgrade to .NET 8 this Sprint because it will help fix users' performance issues.
:::
:::good
Good example - The Developer mentions that it is their opinion leaving the topic open for discussion.
:::

#### 3. Avoid judgemental language

Language that sounds accusatory or judgmental can evoke bad reactions and derail a conversation. Words like "stupid", "hasty", "naive" etc. focus the discussion on people's judgment rather than the issue itself. When that happens, you are no longer discussing the logical cause of the disagreement.

:::greybox
**Developer**: It would be stupid if we didn't upgrade to .NET 8 this Sprint
:::
:::bad
Bad example - The Developer made their point and it sounds like a personal attack
:::

:::greybox
**Developer**: If we don't upgrade to .NET 8 this Sprint, our users are going to keep having the performance issues they have been complaining about.
:::
:::good
Good example - The Developer identifies a pain point for the users, rather than making it emotion based
:::

#### 4. Leave it up to them

Let them know it's their decision, but be clear that you disagree. Communicating this way allows them to feel in control but also makes it obvious what your opinion is.

:::greybox
We should upgrade to .NET 8 this Sprint so that we can solve the performance problems users are experiencing.
:::
:::bad
Bad example - Doesn't leave the power in the stakeholders hands.
:::

:::greybox
This call is yours, but my opinion is that we should upgrade to .NET 8 this Sprint so that we can solve the performance problems users are experiencing.
:::
:::good
Good example - Clearly expresses that the final decision is up to them
:::

Even if you follow all these tips, there is a chance the powerful stakeholder still won't agree with you. In this scenario, it's important to document your disagreement in a [for the record](/for-the-record) email.
