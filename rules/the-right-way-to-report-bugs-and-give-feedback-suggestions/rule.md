---
type: rule
title: Do you know the right way to report bugs and give feedback/suggestions?
uri: the-right-way-to-report-bugs-and-give-feedback-suggestions
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
related:
  - do-you-provide-details-when-reporting-net-applications-errors
redirects:
  - do-you-know-the-right-way-to-report-bugs
  - do-you-know-the-right-way-to-report-bugs-and-give-feedback-suggestions
created: 2009-03-25T04:53:21.000Z
archivedreason: null
guid: 22b7ce50-2586-4fa0-999f-a76a3d60a44a
---

When reporting bugs and giving product feedback, it is essential that you are as descriptive as possible. 

In the case of bugs, the goal is enough detail so the developer can reproduce the error to find out what the problem is.

In the case of suggested features it is best to:  

1.	Draft your suggestion
2.	Call the Product Owner sharing screens, then add the text “checked by XXX”
3.	If a backlog exists, save the Issue/PBI and @mention relevant people (they should get an email) as per https://www.ssw.com.au/rules/when-you-use-mentions-in-a-pbi 
4.	If the client will not get an automatic nicely formatted email with all the text, then send the email with the URL of the Issue/PBI

Try to have one issue/PBI/email per bug/suggestion, but if the bugs/suggestions are related or very small (e.g. they are all on the same page) then you should group them together in a single email.

<!--endintro-->

::: email-template  
|          |     |
| -------- | --- |
| To:      | info@ssw.com.au |
| Subject: | Your software|  
::: email-content  

### Hi 
            
I'm having a problem with your PerformancePro software. When I run it, it says something about registration and then exists. 

Can you tell how to fix this? 

Thanks,  
Susan

:::  
:::
::: bad  
Figure: Bad Example - This email isn't going to help the developer much - it is vague and has no screen capture, and gives no alternate way for the developer to contact the user regarding the issue
:::

::: email-template  
|          |     |
| -------- | --- |
| To:      | info@ssw.com.au |
| Subject: | Your software|  
::: email-content  

### Hi 
            
I'm having a problem with your PerformancePro software. When I run it, this is what happens: 

1. Run the application from Start | Programs 
2. Access opens 
3. I get this error:
  ![](error-software-bur-report.jpg)

I have the latest version of all my software. I am running Windows 10 and Office365. 

Can you please investigate and let me know how to proceed?

Thanks,  
Susan

:::  
:::
::: good  
Figure: Good Example - This email includes the product name and version, the category of the issue (BUG), a screen capture and contact number, and shows that the user's system is up to date
:::

A great template to follow is the [Functional Bug template](https://github.com/aspnet/Home/wiki/Functional-bug-template) from the ASP.NET open-source project. Spending time to provide as much detail as possible, by ensuring you have the three critical components of: Steps to reproduce, Expected outcome, and Actual outcome, will save the both you and the developer time and frustration in the long run. 

Also, make sure your descriptions are detailed and useful as that can make finding the solution quicker and easier.

Make sure you always explain and give as many details as you can of how you got an error or a bad experience.

::: email-template  
|          |     |
| -------- | --- |
| To:      | Rebecca |
| Subject: | SSW TV |  
::: email-content  

### Hi Rebecca, 
            
Where is SSW TV on the navigation?

Adam     

:::  
:::
::: bad
Figure: Bad example - Lack of details
:::

::: email-template  
|          |     |
| -------- | --- |
| To:      | Rebecca |
| Subject: | Can't find SSW TV link on SSW website |  
::: email-content  

### Hi Rebecca, 
            
Navigated to ssw.com.au

Scrolling down looking for a big graphic like "CHECK OUT SSW TV! CLICK HERE!"
(Nothing)
Me, thinking… "Hmm... let's try the menu at the top..."
  
About Us? Nope.
Services? Nope.
Products and Support? Nope.
Training? Nope.
User Group? Nope.
Rules? Nope.

Me, thinking... "OK. Now where? Most likely, the SSW company description will list it..."
Navigates to About Us... scrolling down... nothing.

Me, thinking... "OK. Weird. Let's go back." Me, goes back to homepage.
Me, thinking... "Is there a site map?" Scrolls to bottom of page. Clicks sitemap link.
Me, thinking... "Ctrl+F for TV? Nope." Me, gives up... types tv.ssw.com.au to try and get lucky. Huzzah!

1. Can you help users to get to SSW TV from ssw.com.au

Adam 

:::  
:::
::: good
Figure: Good example - We can easily identify more the one way to improve the UX
:::

Better than a good description of the bug is a screen recording. This should be followed for a more detailed report. Use [Snagit](http://www.techsmith.com/snagit.html) or [Camtasia](/production-do-you-know-how-to-start-recording-with-camtasia) to record your screen.

`youtube: https://www.youtube.com/embed/y9vsGY1hYN0`

::: good
Figure: Good example - Recording bug reports in a video can make the issue clearer to see
:::

`youtube: https://www.youtube.com/embed/VDZSfHJ7GNU`

::: good
Figure: Good example - Giving feature requests via video
:::

::: greybox
**Who should you email, the Product Owner or the Tech Lead?** 

It depends on the team, but often the Product Owner is busy. If you know the Tech Lead and your suggestion is obviously a good one and not too much work, then you should email the Tech Leader and Cc the Product Owner.

The Product Owner can always respond if he doesn’t like the suggestion:  
- For a bug email: 
<br/>
<br/>
  **To: TechLead  
  Cc: ProductOwner  
  Subject: Bug -  xxx (or use PBI @mention)**

- For a new feature email: 
<br/>
<br/>
  **To: TechLead  
  Cc: ProductOwner  
  Subject: Suggestion - xxx  (or use PBI @mention)**

**Note:** You may have a group email such as all@northwind.com.au, You would only Cc this email for greater visibility. 

:::

### Do you use emojis for PBI titles?

When you create a bug/suggestion to a backlog, it's a good idea to add emoji in the title. Not only does it look nicer, but people can look at the item and take in the necessary information quickly.

This means that anyone looking at the backlog can glean its nature at a glance, rather than having to read each item to know what category it is (5 bugs, 2 features, etc.):
- 🐛 Bug - Calendar is not showing on iOS devices
- ✨Feature - Add 'Back to menu' item to top navigation
