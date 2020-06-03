---
type: rule
title: Do you use good code over backward compatibility?
uri: do-you-use-good-code-over-backward-compatibility
created: 2018-04-25T21:15:21.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Supporting old operating systems and old versions means you have more (and often messy) code, with lots of if or switch statements. This might be OK for you because you wrote the code, but down the track when someone else is maintaining it, then there is more time/expense needed.</p><p>When you realize there is a better way to do something, then you will change it, clean code should be the goal, however, because this affects old users, and changing interfaces at every whim also means an expense for all the apps that break, the decision isn't so easy to make.<br></p> </span>

<p>Our views on backward compatibility start with asking these questions&#58;</p><ul><li>Question 1&#58; How many apps are we going to break externally?</li><li>Question 2&#58; How many apps are we going to break internally?</li><li>Question 3&#58; What is the cost of providing backward compatibility and repairing (and test) all the broken apps?</li></ul><p>Let's look at an example&#58;</p><p>We have a public web service&#160;<a href="https&#58;//www.ssw.com.au/ssw/webservices/postcode/">/ssw/webservices/postcode/</a><br>If we change the URL of this public Web Service, we'd have to answer the questions as follows&#58;</p><ul><li>Answer 1&#58; Externally - Don't know, we have some leads&#58;<br>We can look at web stats and get an idea.&#160;<br>If an IP address enters our website at this point, it tells us that possibly an application is using it and the user isn't just following the links.</li><li>Answer 2&#58; Website samples + Adams code demo</li><li>Answer 3&#58; Can add a redirect or change the page to output a warning Old URL. Please see www.ssw.com.au/ PostCodeWebService for new URL <br></li></ul><p>Because we know that not many external clients use this example, we decide to remove the old web service after some time.</p><p>Just to be friendly, we would send an email for the first month, and then another email in the second month.&#160; After that, just emit &quot;This is deprecated (old).&quot;&#160; We'll also need to update the UDDI so people don't keep coming to our old address.</p><p>We all wish we never need to support old code, but sometimes the world doesn't go that way, if your answer to question 3 scares you, then you might need to provide some form of backward compatibility or warning.</p><p class="ssw15-rteElement-GreyBox"><b>From&#58;&#160;</b>John Liu www.ssw.com.au<br><b>To&#58;</b>&#160;SSWALL<br><b>Subject&#58;&#160;</b>Changing LookOut settings<br><br>The stored procedure procSSWLookOutClientIDSelect (currently used only by LookOut any version prior to 10) is being renamed to procSSWLookOutClientIDSelect. The old stored procedure will be removed within 1 month.<br>You can change your settings either by&#58; <br><ul><li>Going to LookOut Options -&gt; Database tab and select the new stored procedure<br></li><li>Upgrading to SSW LookOut version 10.0 which will be released later today<br></li></ul></p><p><br></p>


