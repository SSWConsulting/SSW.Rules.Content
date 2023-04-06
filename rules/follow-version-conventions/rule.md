---
type: rule
archivedreason: 
title: Comments - Do you follow the general commenting rules?
guid: 84813d6d-f297-4d0b-83a8-e598411ece71
uri: follow-version-conventions
created: 2018-04-23T23:28:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- comments-do-you-follow-the-general-commenting-rules

---

There is almost always a better alternative to adding comments to your code.

What are the downsides of comments? What are the alternatives? What are bad and good types of comments? 

<!--endintro-->

There is almost always a better alternative to adding comments to your code. [Chapter 4: Comments, Clean Code](https://www.amazon.ca/Clean-Code-Handbook-Software-Craftsmanship-ebook/dp/B001GSTOAM) is a treatise par excellence on the topic.

### What are the downsides of comments?

1. Comments don't participate in refactoring and therefore get out of date surprisingly quickly.
2. Comments are dismissed by the compiler (except in weird languages like java) and therefore don't participate in the design.
3. Unless strategically added, they place a burden on the reader of the code (they now have to understand 2 things: the code and your comments).

### What are the alternatives to comments?

1. Change name of the element (class, function, parameter, variable, test etc.) to a longer more apt name to further document it.
2. For ‘cryptic’ code (perhaps to optimize it), rewrite it in simpler terms (leave optimization to the runtimes).
3. Add targeted unit tests to document a piece of code.
4. Innovative techniques that are well known solutions to common code smells e.g.:
    - For large methods/classes, break them and have longer names for them.
    - For a method with large number of parameters, wrap them all up in a Parameter Object.
    - &lt;pair up with someone else, think… be creative.&gt;

### What are some **bad** types of comments?

1. That explain the "what"/"how" of the code. Basically the code rewritten in your mother tongue.
2. Documentation comments in non-public surface area.
3. Commenting out the code itself (perhaps to work on it later? That’s what source control is for).
4. TODO comments (Little ones are OK, don't leave them there for too long. The big effort TODOs - say that are over an hour or two - should have a work item URL to it).
5. And many more...

### What are some **good** types of comments?

Very few of these really. Although even these are subject to all the downsides of comments.
Note that a lot of punch can be delivered in 140 characters! Twitter previously?

1. Comments that explain the why (e.g. strategic insights).
2. ...that hyperlink to an external source where you got the idea/piece of code.
3. ...that hyperlink to a Bug/PBI for adding some context.
4. ...that are documentation comments for your next-biggest-thing-on-Nuget library.
5. ...that are real apologies (perhaps you had to add some gut-wrenching nasty code just to meeting time constraints, must be accompanied by a link to Bug/PBI).

Last but not the least, [some parting words](http://butunclebob.com/ArticleS.TimOttinger.ApologizeIncode) from [@UncleBob](https://twitter.com/unclebobmartin) himself:

> "A comment is an apology for not choosing a more clear name, or a more reasonable set of parameters, or for the failure to use explanatory variables and explanatory functions. Apologies for making the code unmaintainable, apologies for not using well-known algorithms, apologies for writing 'clever' code, apologies for not having a good version control system, apologies for not having finished the job of writing the code, or for leaving vulnerabilities or flaws in the code, apologies for hand-optimizing C code in ugly ways."   
>                                   - Uncle Bob (Robert Martin of 'Clean Code' fame)
