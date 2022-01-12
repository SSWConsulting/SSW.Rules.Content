---
type: rule
archivedreason: 
title: Done - Do you go beyond 'Done' and follow a 'Definition of Done'?
guid: f8b61f21-7d1f-497f-a63f-4b9b98c2156c
uri: done-do-you-go-beyond-done-and-follow-a-definition-of-done
created: 2010-02-10T00:09:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Peter Gfader
  url: https://ssw.com.au/people/peter-gfader
- title: Paul Neumeyer
  url: https://ssw.com.au/people/paul-neumeyer
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: 
- dones-do-you-reply-done-and-delete-the-original-email
- dones-do-you-include-useful-details-in-your-done-email
- have-a-definition-of-ready
- do-your-user-stories-include-acceptance-criteria-aka-never-assume-automatic-gold-plating
- comments-do-you-enforce-comments-with-check-ins
- do-you-enforce-work-item-association-with-check-in
- before-starting-do-you-follow-a-test-driven-process
redirects: []

---

Having a clear Definition of Done for your team is critical to your success and quality management in Scrum.

Every team is different, but all need to agree on which items are in their "Definition of Done".  

<!--endintro-->

## There are 3 levels of 'Done' in communication

### Level 1

* Sending a ["Done" email](/dones-do-you-reply-done-and-delete-the-original-email)

### Level 2

* Sending a "Done" email
* Screenshots
* Code

### Level 3

* Sending a "Done" email
* Recording a quick and dirty "[Done Video](/record-a-quick-and-dirty-done-video)"
* Code (showing a full scenario e.g. a user story)

![Figure – Coded UI Test passes in Visual Studio](level-3-done.jpg)

## There are 8 levels of 'Done' in software quality

Start with these examples showing typical "Definitions of Done" from beginner teams to more mature teams:

### Team - Level 1

* The code compiles
* All tasks are updated and closed
* No high priority defects/bugs are on that user story

### Team - Level 2

* *All of the above, plus*
* All unit tests passed
* Greater than 1% code coverage (not earth shattering, but you need to start somewhere)

### Team - Level 3

* *All of the above, plus*
* Successful build on the Build Server
* [Git Branch Policies](/protect-your-master-branch)   
  OR   
  Azure DevOps Check in Policy - Change set Comments Policy (all check-ins must have a comment)
* Azure DevOps Check in Policy - Work Items (all check-ins must be associated with a work item)
* Code reviewed by one other team member (e.g. Checked by Bill)
* Sending a Done email with screenshots

::: good  
![Figure: Good example - Add check in policies to enforce your Definition of Done](CheckinPolicy.jpg)  
:::

### Team - Level 4

* *All of the above, plus*
* All acceptance criteria have been met
* All acceptance criteria have an associated test passing (aka. Automated functional testing with Web Tests (Selenium), Coded UI Tests, or Telerik Tests)
* Tip: Use Microsoft | [Azure Test Plans](https://docs.microsoft.com/en-us/azure/devops/organizations/billing/buy-access-tfs-test-hub?view=azure-devops-2020#buy-monthly-access-to-azure-test-plans)
* Sending a Done email (with video recording using SnagIt)

::: good  
![Figure: Organize tests in suites with built-in E2E traceability across requirements, test artifacts and defects](TestPlanning-1.png)  
:::

::: good  
![Figure: Use the client, Microsoft Test Manager, to run tests and not just capture the pass/fail of steps, comments/attachments and bugs, but also capture diagnostic data during execution, such as screen recording, system info, image action log etc](MTR-2.png)  
:::

::: good  
![Figure: Explore your web applications, find and submit bugs directly from your Chrome browser – no need for predefined test cases or test steps](XT-3.png)  
:::

`youtube: https://www.youtube.com/embed/JJCgP7XcpNA`
 
::: good
Figure: Good example - Done video showing the features worked on  
:::

### Team - Level 5

* *All of the above, plus*
* Deployed to UAT (ideally using Continuous Deployment)
* Complex code is documented (removing technical debt)
* Product Owner acceptance

### Team - Level 6

* *All of the above, plus*
* Multiple environments automatically tested using Lab Management

::: good  
![Figure: Good example - A tester Lab Management to create VMs for testing the application, then defines a test plan for that application with Test Case Management](LabManagement.jpg)  
:::

### Team - Level 7

* *All of the above, plus*
* Automated Load Testing
* Continuous Deployment

::: good  
![Figure: Good example - Load testing involves multiple test agents running Web Performance Tests and pounding the application (simulating the behavior of many simultaneous users)](LoadTesting.jpg)  
:::

### Team - Level 8 (Gold)

* *All of the above, plus*
* Deployed to Production

Congratulations! You are frequently deploying to production. This is called “Continuous Delivery” and allows you to gather quick feedback from your end users.

You might have everything deployed to production, but it might not yet be visible to the end user. This can be achieved by having “[Feature toggles](https://martinfowler.com/bliki/FeatureToggle.html)” in place. The actual release of the functionality is a decision that the Product Owner and business takes.
