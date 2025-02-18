---
seoDescription: Learn how to send tasks one email at a time and improve communication by breaking up unrelated tasks, grouping related tasks, and replying "Dones".
type: rule
archivedreason:
title: Do you split emails by topic?
guid: 9f321108-9a2e-4a89-b287-aff227d5d5a2
uri: split-emails-by-topic
created: 2009-03-30T03:26:32.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - send-email-tasks-to-individuals
  - communication-are-you-specific-in-your-requirements
  - separate-messages
redirects:
  - do-you-send-tasks-one-email-at-a-time
  - email-unrelated-individually

---

People often overlook or miss items in long, carefully drafted emails. To improve clarity and task completion, it's more effective to send separate emails for unrelated (or independent) tasks.

Each email should focus on one task or multiple tasks that are directly related or interdependent. This helps recipients complete the tasks, reply with "Done," delete the email, and move on to the next without confusion. Additionally, ensure your requests are clear and concise to minimize misunderstandings.

<!--endintro-->

## Group related tasks

If you are requesting many smaller tasks under the same topic, you should group them in the same email. In this case, [number each task that you wish to be completed](/number-tasks-questions).

## Break up unrelated tasks

If you have a list of things to be done, and find that your requests are **not** directly related (don't depend on each other OR are not to be done in the same environment), it is better to break it up and send separate emails.

::: email-template  

| | |
| -------- | --- |
| To: | Steven |
| Subject: | Northwind website domain change and CSS fixes |  
::: email-content

### Hi Steven

1. Please buy the domain **Northwind.com**
2. Migrate all the content from **Northwind.com.au** to **Northwind.com**
3. Set up a 301 redirect from **Northwind.com.au** to **Northwind.com**
4. Make sure all the fonts are consistent
5. Make the headings bold

:::  
:::  
::: bad  
Figure: Bad example - One email for multiple unrelated tasks (domains vs styling)
:::

::: email-template  

| | |
| -------- | --- |
| To: | Steven |
| Subject: | Northwind website domain change |  
::: email-content

### Hi Steven

1. Please buy the domain **Northwind.com**
2. Migrate all the content from **Northwind.com.au** to **Northwind.com**
3. Set up a 301 redirect from **Northwind.com.au** to **Northwind.com**

:::  
:::
::: email-template  

| | |
| -------- | --- |
| To: | Steven |
| Subject: | Northwind website CSS fixes |  
::: email-content

### Hi Steven

1. Make sure all the fonts are consistent
2. Make the headings bold

:::  
:::
::: good
Figure: Good example - Separate emails for unrelated tasks. A few related tasks in the same email
:::

## Break up monster tasks

If you have a very large task that requires days of work, it is also better to break it up and send separate related emails. A big task like "Boil the Ocean" would become several emails with consistent subjects:

* "Boil the Ocean #1",
* "Boil the Ocean #2",
* "Boil the Ocean #3", etc

The advantages are that you get an email history for specific parts, making it easier to include someone else and follow up.

::: greybox
**Tip:** Understand tasks sizes by reading [how to size user stories effectively](/estimating-do-you-know-how-to-size-user-stories-effectively).
:::

## Replying 'Dones'

When replying to emails, always reply to each email individually. Never consolidate separate emails into one as it leaves unfinished email threads.

Learn more about [the best ways to reply "Dones"](/dones-do-you-reply-done-and-delete-the-original-email).
