---
type: rule
archivedreason: 
title: Do you ask for content changes using from X to Y?
guid: 1ac0fa3c-7726-4a0f-b5b1-a259801da926
uri: do-you-ask-for-content-changes-using-from-x-to-y
created: 2009-03-25T04:50:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
- title: Piers Sinclair
  url: https://ssw.com.au/people/piers-sinclair
related: []
redirects: []

---

When asking for changes to be made to any file like a web page, Word document, PowerPoint slide or code, always include the original version of the content ("X") together with the changes you require ("Y"). This means you have at hand a history of the page or file as it currently stands allowing for convenient future reference and also makes it very clear to the person doing the changes exactly what the new file is meant to look like. 

Make the changes even easier to see and understand by highlighting in <font style="background-color:#ff0000;">red</font> what you want to delete (only do this on the "From" section) and in <mark>yellow</mark> what you want to be added/updated (only do this on the "To" section).  All text we do not write ourselves should be indented, so this includes paragraphs we are copying and pasting (see [Do you use indentation for readability?](/do-you-use-indentation-for-readability))

<!--endintro-->

::: email-template  
|          |     |
| -------- | --- |
| To:      | Eric |
| Subject: | Update CodeAuditor features list |  
::: email-content  

### Hi Eric,

1. For the Code Auditor web page, please make the list read:

   - Scan all your projects for coding errors
   - Guarantee Industry best practices
   - Friendly licensing model, bloggers even pay $0 for the full version!

:::  
:::  
::: bad
Figure: Bad example - original version of content has not been included in the email
:::

::: email-template  
|          |     |
| -------- | --- |
| To:      | Eric |
| Subject: | Update CodeAuditor features list |  
::: email-content  

### Hi Eric,

http://www.ssw.com.au/ssw/codeauditor
1. On the Code Auditor web page, please change:

From:

  * Scan all your projects for coding bugs <font style="background-color:#ff0000;">and errors</font>
  * Enforce industry best practices              
  * Friendly licensing model pay nothing for the full version!

To:

  * Scan all your projects for coding errors
  * Guarantee industry best practices
  * Friendly licensing model<mark>, bloggers even pay $0</mark> for the full version!

:::  
:::  
::: good
Figure: Good Example - it has 'From' and 'To' with changes highlighted... so it is clear what needs to be changed
:::

### What if there are too many changes?

Sometimes you have a lot of content and too many changes, making the process "from X to Y" too arduous. In this case is recommended to use [Word 'Track Changes'](https://support.microsoft.com/en-gb/office/track-changes-in-word-197ba630-0f5f-4a8e-9a77-3712475e806a?ui=en-us&rs=en-gb&ad=gb) functionality.

![Figure: A Word document with 'Track Changes' ON is recommended if you have too many changes](word-track-changes.jpg)  

**Video:** [Top 10+ Rules to Better Email Communication with Ulysses Maclaren](https://www.youtube.com/watch?v=LAqRokqq4jI)

### Reviewing changes in GitHub via pull requests

A pull requests is a request to make changes to 1 or more files. GitHub provides out of the box functionality for reviewing changes in a pull request. This process is as follows

1. Open the pull request
2. Examine the changes using the tabs
    * Conversations: shows comments people have made about the change
    * Commits: shows comments associated with the changes the requester has made
    * Files changed: show the difference between the old and new files being changed. Red highlighting indicates deleted parts and green highlighting indicates added parts. 
    ![The pull request tabs](https://user-images.githubusercontent.com/79821522/112783096-3b593f00-909a-11eb-9862-c641822f133e.png)
    **Tip:** To see a visual preview of the changes to a markdown file select the "Display the rich diff" button
    ![The "Display the rich diff" button](https://user-images.githubusercontent.com/79821522/112783487-2a5cfd80-909b-11eb-9820-d04a437dd43a.png)
3. Add your review by navigating to "Files changed"

    1.&nbsp;Press "Review changes"</pre>

    2.&nbsp;Add a comment with your feedback.

    3.&nbsp;Choose "Approve" to mark it as ready to go live. If it is not ready, then choose "Comment" for general feedback or "Request changes" for mandatory changes.

    4.&nbsp;Press "Submit review" so that the requester can see it.
      ![Submitting a pull request review](https://user-images.githubusercontent.com/79821522/112782859-bbcb7000-9099-11eb-894d-2df0ee5fe290.png)


