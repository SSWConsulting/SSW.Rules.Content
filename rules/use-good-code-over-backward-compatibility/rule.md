---
type: rule
archivedreason: 
title: Do you use good code over backward compatibility?
guid: 07b07831-f85d-4803-9309-effef003754d
uri: use-good-code-over-backward-compatibility
created: 2018-04-25T21:15:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-good-code-over-backward-compatibility

---

Supporting old operating systems and old versions means you have more (and often messy) code, with lots of if or switch statements. This might be OK for you because you wrote the code, but down the track when someone else is maintaining it, then there is more time/expense needed.

When you realize there is a better way to do something, then you will change it, clean code should be the goal, however, because this affects old users, and changing interfaces at every whim also means an expense for all the apps that break, the decision isn't so easy to make.

<!--endintro-->

Our views on backward compatibility start with asking these questions:

* Question 1: How many apps are we going to break externally?
* Question 2: How many apps are we going to break internally?
* Question 3: What is the cost of providing backward compatibility and repairing (and test) all the broken apps?


Let's look at an example:

We have a public web service [/ssw/webservices/postcode/](https&#58;//www.ssw.com.au/ssw/webservices/postcode/)
If we change the URL of this public Web Service, we'd have to answer the questions as follows:

* Answer 1: Externally - Don't know, we have some leads:
We can look at web stats and get an idea. 
If an IP address enters our website at this point, it tells us that possibly an application is using it and the user isn't just following the links.
* Answer 2: Website samples + Adams code demo
* Answer 3: Can add a redirect or change the page to output a warning Old URL. Please see www.ssw.com.au/ PostCodeWebService for new URL


Because we know that not many external clients use this example, we decide to remove the old web service after some time.

Just to be friendly, we would send an email for the first month, and then another email in the second month.  After that, just emit "This is deprecated (old)."  We'll also need to update the UDDI so people don't keep coming to our old address.

We probably all prefer working on new features, rather than supporting old code, but it’s still a core part of the job. If your answer to question 3 scares you, it might be time to consider a backward compatibility warning.


::: greybox
 **From: ** John Liu www.ssw.com.au
 **To:**  SSWALL
 **Subject: ** Changing LookOut settings

The stored procedure procLookOutClientSelect (currently used only by LookOut any version prior to 10) is being renamed to procSSWLookOutClientIDSelect. The old stored procedure will be removed within 1 month.
You can change your settings either by: 

:::

* Going to LookOut Options -&gt; Database tab and select the new stored procedure
* Upgrading to SSW LookOut version 10.0 which will be released later today
