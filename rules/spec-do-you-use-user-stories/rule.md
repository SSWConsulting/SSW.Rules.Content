---
type: rule
archivedreason: 
title: Spec - Do you use User Stories when appropriate?
guid: 0daa42ed-f103-4e4b-9d27-e9b77647b4b6
uri: spec-do-you-use-user-stories
created: 2009-11-03T10:33:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
related: []
redirects:
- spec-do-you-use-user-stories-when-appropriate

---

Product Backlog Items (PBIs) can be described in the form of a "User Stories" when appropriate. It ensures the developers will know the context for a PBI.


::: greybox
As a &lt;type of User&gt;
I want &lt;some goal&gt;
so that &lt;some reason&gt;

:::
Figure: User Story - template for description

<!--endintro-->


::: bad  
![Figure: User Story - Product Backlog Item form](TFS2012UserStory.gif)  
:::


::: greybox
I want to be able to search for customers.

:::
Figure: Bad Example - the user story is too vague and broad in scope

::: greybox
As a Marketing Manager...
    I want to be able to search for customers by country and last name.
    So that I can find their numbers and call customers close to me.  
:::
Figure: Good Example - Clear user story following the INVEST principle



**Note:** In the TFS Scrum template (since we now have a title, description, and acceptance criteria), we no longer generally need to use User Story formatting.
