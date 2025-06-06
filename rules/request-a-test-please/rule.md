---
seoDescription: how-to-request-a-test-please-effectively-for-software-testing-and-quality-assurance
type: rule
title: Do you know how to request a "Test Please"?
uri: request-a-test-please
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
related:
  - do-you-send-as-per-our-conversation-emails
  - do-you-know-when-to-do-use-checked-by-xxx
  - conduct-a-test-please
  - when-you-use-mentions-in-a-pbi
redirects:
  - quality-do-you-know-how-to-request-a-test-please
created: 2015-08-26T19:03:34.000Z
archivedreason: null
guid: dda8e03b-f5a1-4dea-967e-cfda36fbda95

---

Testing is a fundamental aspect of software development, serving as the quality assurance checkpoint that ensures a product functions as intended, meets user expectations, and operates reliably in various environments. This crucial phase helps identify and rectify issues, enhances user satisfaction, and ultimately safeguards a software's reputation and success.

<!--endintro-->

## ✅ The ideal 'Test Please' workflow

When requesting a review or approval (commonly called a "Test Please") for a piece of work such as a video edit, blog post, or design preview, it's important to follow a consistent and transparent workflow:

1. **Post the preview link in the PBI** – Add the link to the version or preview at the top of the relevant PBI (Product Backlog Item)
2. **Use the PBI discussion to tag reviewers** – In the comments section, use `@` to mention the team members you want to review the work, and write a clear message (e.g., “Test please 🙏”)
3. **Keep all feedback and iterations in the same thread** – Reviewers should reply in the same PBI discussion with comments or with a confirmation like “Test passed ✅.” Any required changes or back-and-forth should also stay within that thread to keep the full history in one place
4. **Follow up professionally via Teams** – If there's no response after a reasonable time, you can follow up via Microsoft Teams with a short message (e.g., “Hi Adam, calling in 1 min about the preview link”), and reference the same PBI so the full context is easy to access

This process ensures feedback is traceable, transparent, and tied to the work item.  

## 'Test Please' via email

When there’s **no project backlog** in place, it’s acceptable to send a 'Test Please' request via email.

These are the steps you should take when requesting a "Test Please" via email:

1. Find 2 free testers to send the email below
2. Stop working on the project until you receive either a "pass" or "fail" email
3. Create your "Test Please" following this template:

::: email-template  

| | |
| -------- | --- |
| To:| John |
| Subject: | Product Name v1.11 |
::: email-content

1. <mark>'Test Please'</mark>

### Hi John

I am looking for bugs or approval to release this version.

1. Please test the following modifications:

* {{ FEATURE TO BE TESTED }}
* {{ FEATURE TO BE TESTED }}

I have done what I could for my code's health. E.g.

* Run SSW CodeAuditor - it has {{ X }} errors (if not 0, give reason)
* Kept my eye on Application Insights
* Ensured all packages are as up-to-date as possible
  * Updated:
    * Updated {{ PACKAGE }} from {{ VERSION }} to {{ VERSION }}
    * ...
  * Out-of-date:
    * {{ PACKAGE }} is on {{ VERSION }}. Latest is {{ VERSION }}.
    * ...

Specific issues to look out for are:

* {{ ISSUE }}
* {{ ISSUE }}

The latest version (Product Name v1.11) is at {{ URL }}

Keep in mind that a "Test Please" is an urgent task and that it should start within the hour.

**Notes:**

**\#1** - Know the [definition of a bug](/definition-of-a-bug)

**\#2** - Understand the importance of [conducting a "Test Please" internally and then with the client](/conduct-a-test-please-internally-and-then-with-the-client)

**\#3** - Send suggestions/bugs one email at a time (with unique and [good email subjects](/good-email-subject)) making it easier to fix and reply "Done"

**\#4** - CC the product owner and relevant stakeholders

**\#5** - Do not reply to this message until you can say:

* "**✅ Test Please succeeded** (as no Critical bugs). You are ready to deploy."\
or
* "**❌ Test Please failed** (as per Critical bugs reported)"

**\#6** - To keep things moving along, remember that after **5 business days**, the code will be automatically considered approved and pushed to Production.

Regards,

:::
:::

::: info
**Note to developers:**
If current version is better than the last version you can release (even with a test fail) as long:

* The bugs reported in the test fail existed in the old version
* 2 people have tested it
* The changes in this version are fairly important to get out
* You get to work on the failures ASAP
:::

## ❌ Don't send a 'Test Please' content via IM

You may use IM (e.g. Microsoft Teams) to point the tester to the 'Test Please' email.

::: greybox
"Ping!
I need you to check my 'Test Please' email\
See subject: **Product Name v1.11**"
:::

### Getting input from a extra people

If you require input from a few people that were not originally cc'd on the email or on the ['To Myself'](/send-to-myself-emails), like getting feedback on a design, it's nice to give everyone the entire task context.

You have 2 options:

1. **Keep the "test" in the same thread** (recommended)\
In this case, just add the people you need to the thread, asking them specifically for a 'Test Please' on what you need
2. **Create a new thread for the 'Test Please'**
This is for when you have a good reason not to (e.g. avoiding too long email threads; too many people cc'ed, etc).
In this case, make sure you include the original thread subject in your email, so people know the main task is happening there

This way everyone will have the entire history of the task and its progress.

::: info
**Note:** A @ mention is all you need if you are following the ideal workflow 😉
:::

---

## 'Test Please' specifics  

### Email draft 'Test Please'

In most cases, you can [get your email 'Checked by xxx'](/checked-by-xxx).

For really important stuff you may need to actually send a 'Test Please' email to test your email. In these cases:

* Add <mark>'Test Please'</mark> highlighted in yellow to the top of the email body
* Do **not** add 'Test Please' to the subject (it is too easy to forget removing it later!)

### Windows Forms 'Test Please'

For Windows Forms test you should include this info to the email:

* The latest version of {{ PRODUCT NAME }} has been uploaded to **\frog\SSW\Download[Application_verX-XX_beta.exe**
* Test on a fresh VPC image of Windows
* Install into a non-default directory
* Check the installation folder for misplaced items
* Test Unit Tests via "Help - Run Unit Tests"
* (If Applicable)Test the "Create" and "Reconcile" buttons. Read [Rules to Better .NET Projects](/rules-to-better-net-projects)
* Test open and closing forms and saving values
* Test most buttons and menus and links
* Disable your network connection and test again (check for unhandled errors)
* If your test fails, please rename the executable to **Application_verX-XX_failed.exe**

::: info
**Note:** For clients on fixed-price contracts, the 'Test Please' reply marks the start of the 30-day warranty period.
:::
