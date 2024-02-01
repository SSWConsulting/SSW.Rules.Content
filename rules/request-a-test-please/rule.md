---
type: rule
title: Quality - Do you know how to request a "Test Please"?
uri: request-a-test-please
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - do-you-send-as-per-our-conversation-emails
  - do-you-know-when-to-do-use-checked-by-xxx
  - conduct-a-test-please
redirects:
  - quality-do-you-know-how-to-request-a-test-please
created: 2015-08-26T19:03:34.000Z
archivedreason: null
guid: dda8e03b-f5a1-4dea-967e-cfda36fbda95
---

Testing is a fundamental aspect of software development, serving as the quality assurance checkpoint that ensures a product functions as intended, meets user expectations, and operates reliably in various environments. This crucial phase helps identify and rectify issues, enhances user satisfaction, and ultimately safeguards a software's reputation and success.

These are the steps you should take when requesting a "Test Please":

<!--endintro-->

1. Find 2 free testers to send the email below
2. Stop working on the project until you receive either a "pass" or "fail" email
3. Create your "Test Please" following this template:

::: email-template  
|          |     |
| -------- | --- |
| To:      | John |
| Subject: | Product Name v1.11 |  
::: email-content  

1. <mark>'Test Please'</mark>

### Hi John,  
I am looking for bugs or approval to release this version.

1. Please test the following modifications:

* {{ FEATURE TO BE TESTED }}
* {{ FEATURE TO BE TESTED }}

I have done what I could for my code's health. E.g.

* Run SSW CodeAuditor - it has {{ X }} errors (if not 0, give reason)
* Run SSW LinkAuditor - it has {{ X }} errors (if not 0, give reason)
* Kept my eye on Application Insights

Specific issues to look out for are:

* {{ ISSUE }}
* {{ ISSUE }}

The latest version (Product Name v1.11) is at {{ URL }}

Keep in mind that a "Test Please" is an urgent task and that it should start within the hour.

**Notes:**
* Know the [definition of a bug](/definition-of-a-bug)
* Understand the importance of [conducting a "Test Please" internally and then with the client](/conduct-a-test-please-internally-and-then-with-the-client)
* Send suggestions/bugs one email at a time (with unique and [good email subjects](/good-email-subject)) making it easier to fix and reply "Done"
  * Please CC the project manager and the client
* Do not reply to this message until you can say:
  * "**✅ Test Please succeeded** (as no Critical bugs). You are ready to deploy."  
    or 
  * "**❌ Test Please failed** (as per Critical bugs reported)"

Regards,

:::
:::

::: info
**Note to developers:**
If current version is better than the last version you can release (even with a test fail) as long:
- The bugs reported in the test fail existed in the old version
- 2 people have tested it
- The changes in this version are fairly important to get out
- You get to work on the failures ASAP
:::

### Don't send a 'Test Please' content via IM

You may use IM (e.g. Microsoft Teams) to point the tester to the 'Test Please' email.

::: greybox
"Ping!   
I need you to check my 'Test Please' email   
See subject: **Product Name v1.11**"
:::

### What if you are doing an email test?

In most cases, you can [get your email 'Checked by xxx'](/checked-by-xxx).

For really important stuff you may need to actually send a 'Test Please' email to test your email. In these cases:

* Add <mark>'Test Please'</mark> highlighted in yellow to the top of the email body
* Do **not** add 'Test Please' to the subject (it is too easy to forget removing it later!)

### What if you need to get input from a few people?

If you have received a task that requires input from a few people that were not originally cc'd on the email or on the ['To Myself'](/send-to-myself-emails), like getting feedback on a design, it's nice to give everyone the entire task context.

You have 2 options:

1. **Keep the "test" in the same thread** (recommended)  
   In this case, just add the people you need to the thread, asking them specifically for a 'Test Please' on what you need

2. **Create a new thread for the 'Test Please'**
   This is for when you have a good reason not to (e.g. avoiding too long email threads; too many people cc'ed, etc).   
   In this case, make sure you include the original thread subject in your email, so people know the main task is happening there

This way everyone will have the entire history of the task and its progress.

### What if you're doing a Windows Forms test?

For Windows Forms test you should include this info to the email:
- The latest version of {{Product Name}} has been uploaded to **\\frog\SSW\Download\[Application\_verX-XX\_beta.exe**
- Test on a fresh VPC image of Windows
- Install into a non-default directory
- Check the installation folder for misplaced items
- Test Unit Tests via "Help - Run Unit Tests"
- (If Applicable)Test the "Create" and "Reconcile" buttons. Read [Rules to Better .NET Projects](/rules-to-better-net-projects)
- Test open and closing forms and saving values
- Test most buttons and menus and links
- Disable your network connection and test again (check for unhandled errors)
- If your test fails, please rename the executable to **Application\_verX-XX\_failed.exe**

::: info
**Note:** For clients on fixed-price contracts, the 'Test Please' reply marks the start of the 30-day warranty period.
:::
