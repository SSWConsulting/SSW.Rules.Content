---
type: rule
title: Do you use AI to generate your specification reviews?
uri: use-ai-to-generate-spec-reviews
authors:
  - title: Gert Marx
    url: https://www.ssw.com.au/people/gert-marx/
  - title: Calum Simpson
    url: https://www.ssw.com.au/people/calum-simpson/
  - title: Jeoffrey Fischer
created: 2023-10-13T00:45:19.179Z
guid: dcdcda96-80b7-4ed2-882f-f0062f723e76
---
Even the most seasoned analysts might occasionally overlook certain details in a specification review. Leveraging technology, especially AI, not only augments our capabilities but also acts as a safety net for those unintentional oversights.

<!--endintro-->

## The Role of AI in Enhancing Reviews

* **Tool, Not Replacement:** While AI can greatly aid in generating specification reviews, the human touch remains irreplaceable. AI provides a baseline, but the keen eyes of an expert bring depth and clarity to the document.
* **Interactive AI:** Instead of feeding AI with a static set of requirements, engage in a dialogue. Let the AI ask questions to better understand the depth and scope of the specification.
* **Customization Over Templates:** Relying on one-size-fits-all templates can be a pitfall. While they provide structure, they can also hinder innovation. Each project has its nuances, and the AI should be adaptable enough to cater to them.\
  ::: greybox
  Prompt:\
  You are an IT Consultancy specification write.\
  \
  Engage with me step-by-step to collect essential requirements.\
  \
  Ask me one question at a time, and then only ask the next after I have answered the last one.
  :::
  ::: good Figure: Good Example
  As you answer the questions, AI can generate new questions based on your previous answers and insights.
  :::

  ::: greybox
  Prompt:\
  Take the following requirements and write me a detailed specification review for the solution:\
  \
  1. Web application running on Azure\
  2. Solution captures feedback from users\
  3. Grab user information through sign up process\
  .......
  :::
  ::: bad Figure: Bad Example
  No information given about security, data migrations or existing infrastructure or services that can be re-used.
  :::

## Value Additions from AI

* **Generating PBIs:** AI can take over the task of creating Product Backlog Items (PBIs), offering consistency and speed.
* **Architecture Visualization:** Using tools like [Mermaid](https://mermaid.js.org/), AI can transform raw data into coherent and interactive architecture diagrams.

  ::: greybox
  graph TB\
  CUI\[Cloud User Interface]\
  CPM\[Cloud Product Management]\
  COM\[Cloud Order Management]\
  CAM\[Cloud Admin Module]\
  CPG\[Payment Gateway]\
  CI\[Cloud Infrastructure]\
  CUI -->|Place Order| COM\
  COM -->|Payment| CPG\
  CAM -->|Manage Products| CPM\
  CAM -->|System Configurations| CSC\[Cloud System Configurations]\
  CI\[Cloud Infrastructure] -->|Supports| CUI\
  CI -->|Supports| CPM\
  CI -->|Supports| COM\
  CI -->|Supports| CAM
  :::
  ::: good Figure: Good Example
  Simple Mermaid visualization of proposed system architecture
  :::
* **From Architecture to Specification:** Provide your AI with an architecture document. Watch it craft a draft specification review that can then be fine-tuned by professionals.

Remember, AI is a powerful tool in our arsenal, but the magic truly happens when we synergize its computational prowess with our domain expertise.