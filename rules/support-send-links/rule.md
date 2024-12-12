---
seoDescription: Ensure customer support responses are effective by including relevant documentation links. 
type: rule
archivedreason:
title: Do you send links when offering support?
guid: 00879668-3bca-40bf-bdeb-7e4970062fc6
uri: support-send-links
created: 2024-09-02T02:45:54.0000000Z
authors:
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: 
  - knowledge-base-kb
redirects: []
---

When offering support to customers using your product, think about whether this problem has occurred before or could happen again. If it has, there should be documentation available. This not only helps customers resolve their issues faster but also reduces the repetitive workload for the support team.

You should never have to answer the same question twice.
When you get a new question e.g. "Can I do validation in TinaCMS?" these are the steps you should follow

1. Check for existing documentation.
2. If it doesn't exist, create the documentation.
3. Reply with a link to the documentation.

Every support message should include a link to the relevant documentation or, if applicable, to a Product Backlog Item (PBI).

<!--endintro-->

::: greybox
Yes - you can do validation in TinaCMS.
You can do it by adding the ui.validation function to your field definition.

Let me know if you have any issues with this!
:::
::: bad
Figure: Bad Example - explaining how to solve the problem when there are already docs
:::

::: greybox
Yes - you can do validation in TinaCMS. Here is the link to the docs [https://tina.io/docs/extending-tina/validation](https://tina.io/docs/extending-tina/validation).
:::
::: good
Figure: Good Example - Replying with a link to the docs
:::

Sometimes, you might get questions about bugs, upcoming features, or other things that are not documented. In this case,

::: greybox
Not yet - We are still working on mermaid diagram support in TinaCMS. Check out this issue to see the status
<https://github.com/tinacms/tinacms/issues/4733>
:::
::: good
Figure: Good Example - Sending a link to a PBI is also acceptable
:::

After a while, you will build a great library of documentation that customers will use to self-serve their questions. This practice will also get you to read your documentation and improve it more often.

**Exceptions to this rule:**

* **Do not** write a documentation page if fixing the bug and releasing a new version solves the problem. In this case, create a PBI (or find an existing one) and reply with the link to it.
* **Do not** write a documentation page or PBI if the question/answer is irrelevant to your product, e.g., "Next.js - how do I deploy my app?" (This is not relevant to TinaCMS.)

**🤖 AI Tip:** Consider training a chatbot on your documentation to help answer common questions automatically. [Learn more about implementing a chatbot](https://www.ssw.com.au/rules/website-chatbot/)
