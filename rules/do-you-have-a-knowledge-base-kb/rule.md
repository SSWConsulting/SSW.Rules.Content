---
type: rule
archivedreason: 
title: Do you have a Knowledge Base (KB)?
guid: 00879668-3bca-40bf-bdeb-7e4970062fc6
uri: do-you-have-a-knowledge-base-kb
created: 2009-03-02T02:45:54.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Titus Maclaren
  url: https://ssw.com.au/people/titus-maclaren
related: []
redirects:
- do-you-have-a-knowledge-base-(kb)

---

Do you know what the most useful thing on Microsoft website is? It is their knowledge base at [support.microsoft.com](https://support.microsoft.com/).

When a problem arises it should be your first port of call - it allows you to help yourself.

<!--endintro-->

So, if you answer questions on your products to customers, you are wasting time if you don't have a knowledge base. Just think, you might not be answering Harry's question if he could have looked it up himself.

Now of course there are many customers who don't look for a KB, but instead, you fire off the same old email that you already know is an MDAC related error, and your current solution is to tell them to run SSW Diagnostics and get all the green ticks.

::: greybox

**Dear Harry,**  

Thank you for taking the time to report the issue to SSW CodeAuditor. I'm happy to let you know that this is a known issue and has been addressed in our knowledge base: {{ LINK }}

Thanks,  
Bob
:::
::: good
Figure: Responding to a known issue with a KB article  
:::

The basic rule is: don't send back the answer in your email - instead send back the link. More specifically:

1. **If you can answer** a support email then reply to the support email
    * To: the client
    * Cc: the developer and your manager with the KB link
2. **If you can’t answer** the question then reply to the support email:
    * To: the client and the developer
    * Cc: your manager
    * Ask the customer if they can get diagnostics to all green ticks.
    * Ask the developer to “Please action?"

::: greybox

**Dear Harry,**

Thank you for taking the time to report the issue to SSW CodeAuditor.

I am sorry to let you know that I cannot reproduce this. Could you please provide me with more details or, even better, would I be able to connect to your PC? It is simple and you can see everything I do. To do so, you can send me an appointment for an appropriate time or add me to Skype

Kind Regards,   
Bob

:::
::: good
Figure: Responding when you cannot reproduce the issue  
:::


::: greybox

**Dear Harry,**

Done. The code changed from

{{ XXX }}

to

{{ YYY }}

Thank you for reporting this bug - our software only gets better with help from our customers. This fix will be available in the next version shortly.

Kind Regards,  
Bob

:::
::: good
Figure: Informing of a fix (Email 1 of 2) 
:::

**Note:** In this email, you can offer them an interim build.

::: greybox

**Dear Harry,**

Thank you for taking the time to report the issue to SSW CodeAuditor. I'm happy to let you know that this problem is fixed in this release.

Please download the new version at {{ LINK }}

Kind Regards, 
Bob

:::
::: good
Figure: Informing of a new version (Email 2 of 2)  
:::

Notice how by just giving them the URL, this email does the job of encouraging them to use your knowledge base in the future. You need to make sure the support staff knows that there are really only 4 types of emails customers should be receiving (see the 4 grey boxes).

Things are running well when you have support staff adding new KB for:

* Known issues
* Hot tips
* Performance tips KBs also play a very important role in getting a product released. You will never get every feature done or bug fixed - we all know it. 

Focus on getting a version out. It is usually more important to have a version available than having no version at all. When you are looking down the Project Plan, decide on what the **must-haves** are. The other features and known bugs will have to remain outstanding. All the longer-term bugs should go into the KB. We also put in the feature requests that we plan on doing. This way our customers know of our exciting features coming in future versions of our software.

However **don't** write a KB article if fixing the bug and making a new version solves the problem. You'll have to fix the problem anyway, so don't waste time writing a KB, just email the new version.

You don't need to be Microsoft to build a KB. A Knowledge Base does not need to be complicated. We use a simple knowledge base which is located at [pdi-ssw.zendesk.com/hc/en-us](https://pdi-ssw.zendesk.com/hc/).

Suggestions for features should be added to the backlog and voted on at uservoice.com.

::: greybox

**Dear Harry,**

Thanks for the suggestion for SSW CodeAuditor!

I have added it to the list of future developments (which we call our backlog). Future features can be voted on at uservoice.com

Thanks,
Bob

:::
::: good
Figure: Responding to a feature suggestion
:::

An important tip for creating a knowledge base document is to make sure it is easily searchable and accessible. 

You can easily create a page for a KB in GitHub's Wiki section. E.g. [SSW CodeAuditor KB](https://github.com/SSWConsulting/SSW.CodeAuditor/wiki/SSW-CodeAuditor-Knowledge-Base-(KB)).

::: good
![Figure: Good example - CodeAuditor's KB](https://user-images.githubusercontent.com/67776356/233515514-b81668ee-e0a7-49e5-a09e-595e895ef303.png)
:::

