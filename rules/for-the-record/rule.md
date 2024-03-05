---
type: rule
title: Do you send a 'For the record' email when you disagree?
uri: for-the-record
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects:
  - do-you-send-a-for-the-record-email-when-you-disagree
  - send-a-for-the-record-email-when-you-disagree
created: 2010-07-16T06:49:34.000Z
archivedreason: null
guid: 47440022-76fd-4df5-a81c-363df2a0ccc0
---

Over the course of work on a project, there will likely be many little disagreements, and most can be captured in ["as per our conversation"](/do-you-send-as-per-our-conversation-emails) emails. Sometimes the differences of opinion relate to architectural issues or things that will be hard to change later. A lot of developers are on the quiet, introverted side, but vocal developers make their stance clear. Even that can be hard with some clients who have super strong voices and some clients are **not** great listeners.

<!--endintro-->

Regardless it is important to document disagreements so the client is crystal clear and a stronger version of ‘as per our conversation’ is to include the words ‘for the record’. Too often developers say they disagree but months later, the client may say:

::: greybox
“No I don’t recall you disagreed, I thought I gave counter arguments and then I assumed you had agreed with me.”
:::

![Figure: It's common for people to say "I don't remember you disagreeing with that decision", sending a "for the record" email makes it clear](past-decision-1500x500.jpg)

::: greybox
**One war story**

"One day we had an incident where one of our clients had found out that a developer had hard-coded the CSS (the default Angular way). When the client discovered it, they were wild and wanted 24 days written off as a consequence. To be clear, the reaction and the request were disproportionate. However, clients have memories that are fallible and they can be entitled to be upset when they come to a company (like SSW) that prides themselves on following best-practices.

I spoke to the developer about it, and he knew 100% that he had agreed with the Product Owner to leave it that way because it was super quick and they had bigger fish to fry at the time. The developer recalled explaining to the Product Owner that he wasn't comfortable taking that shortcut. The step that the developer failed to do was to cover his ass with an "As per our conversation" email... or when the disagreement is related to architectural issues (or issues that will require a lot of rework later) I suggest a more clear "For the record" email.

**Note:** Even better the developer could have included a URL in the email with a link to a PBI to remove this technical debt later."

Adam Cogan
SSW Chief Architect

:::

When you have a disagreement with someone who has decision making power, and you are unable to convince them that your recommendation is correct (and they were unable to convince you that their decision is correct), you should send an email to the people involved including your thoughts, because:

1. Later down the track it will provide a learning experience for someone (depending on who was right 😉)

**Tip:** Use [follow up then](/do-you-follow-up-emails-effectively) to remind you to revisit your email (e.g. 6 months in the future), then take the opportunity to follow up on it with a retrospective analysing the decision that was made and what the outcome was (no matter who was right, it shows you were invested enough in the issue to keep track of it)
  
2. After cooling down from the meeting, people might read it later and see it as useful input

**Note:** A "For the record" email should be reserved for a significant architectural decision, etc. That will be difficult or costly to change later. You should consider it a level above an ["As per our conversation" email](/do-you-send-as-per-our-conversation-emails), which is better suited for more minor decisions.

(...6 months later)

::: greybox
"I knew it, we should never have used React for the Northwind project."
:::
::: bad
Figure: Bad example - Being improductive and too late
:::

(...on the day)

::: greybox
"Thanks for the chat today. As per our conversation, you'd like us to build this feature using a quick workaround. Just for the record, the best practice would have been to XXX, but since you are the Product Owner, and I understand we're under time pressure, I of course will go with your decision."
:::
::: good
Figure: Good example - Documenting that client has asked you to do a shortcut
:::

(...on the day)

::: greybox
"Thanks for the chat today. For the record, you have requested that we proceed with developing the Northwind Project in React, whereas **we have recommended using Angular** for the following reasons:

* {{ LINK 1 }}
* {{ LINK 2 }}
* {{ LINK 3 }}

That said, you are the Product Owner and have final say in the matter, so we will proceed with React as per your decision."

:::
::: good
Figure: Good example - You have politely pointed out they are making a poor technology choice and given empirical evidence.
:::

**Note:** It's also a good email to have in your back pocket in case the client complains about slow progress in a few months time.

(...6 months later - the curious retrospective)

::: greybox
"I just got reminded about this email from 6 months ago, in the spirit of doing retrospectives to learn, thanks for taking my call about it.  
As per our conversation, we are both happy that the React solution has panned out and there has been some benefits that we didn't think of at the time such as hiring a couple of cool React developers. We agreed that we could have saved some money with Angular, but we don't regret the decision."
:::
::: good
Figure: Good example – 6 month retrospective to analyse the pros and cons of a past decision.  
:::

Tread carefully with a follow up email - use your discretion to avoid souring a relationship by unnecessarily rubbing their face in it. Mention the words "For the record," so that you can find it more easily in the future with a search, but avoid starting with it because it can sound a bit harsh.

Make sure you Cc your account manager and any other relevant parties so that they can keep informed of the situation.

Make it clear that your advice is purely technical in nature and not business or legal advice. Consider putting the words "The above is not legal advice." at the end of your email.

This is also a good thing to do if you have an [ethical problem](/do-you-only-do-what-you-think-is-right) with a task.

Take some time to complete this ["'For the record' emails" survey](https://forms.office.com/Pages/ResponsePage.aspx?id=NHwvrDW56Uir3BHl1PyysCa8TOGbvXxGkJLSg13sAKhURVdQRVBSUFZINzgxMzVLRlVOUVNDSUpBSiQlQCN0PWcu).
