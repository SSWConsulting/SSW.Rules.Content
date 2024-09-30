---
type: rule
title: Cross-approvals - Do you know how to scale approvals?
seoDescription: Cross-approvals - Streamline your company's aspproval process
  with expert guidance.
uri: cross-approvals
authors:
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
  - title: Calum Simpson
    url: https://ssw.com.au/people/calum-simpson
  - title: Rick Su
    url: https://ssw.com.au/people/rick-su
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/uly
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Seth Daily
    url: https://ssw.com.au/people/seth-daily
related:
  - bench-master
  - management-structures
  - checked-by-xxx
redirects:
  - streamline-approvals
  - streamlining-approvals
created: 2023-08-08T13:00:00.000Z
archivedreason: null
guid: 4f425961-3b0e-4b1b-bea4-48bab98f5c05
---
In small companies, a single key stakeholder often approves everything, ensuring alignment with the organizational vision and strategy. However, as the company grows, this can lead to bottlenecks - or "approval hell". One approach that addresses this is to have multiple people responsible for a specific approval. This ensures a clearly communicated system for [cross-authorization](/purchase-please/#cross-authorization).

<!--endintro-->

`youtube: https://www.youtube.com/watch?v=-Xfi9CbIK1Q`

**Video: Cross-approvals - Do you know how to scale approvals? (4 min)**

## What is an approval?

Generally an approval is anytime you need someone else to check a piece of your work before it can be marked as done.

Approvals can either be:

* **Ad hoc** - these are best done following the 'checked by' rule: [Do you use 'Checked by xxx'?](https://www.ssw.com.au/rules/checked-by-xxx/)
* **Recurring** - these cause "approval hell" - you should use **approval scaling**

::: bad
![Figure: Bad example - Approval hell!](approval-hell.png)
:::

## ✅ Benefits of scaling approvals

* Time savings for the person causing the bottlenecks (aka the "original approver")
* Fewer bottlenecks for those seeking approval
* Consistent and high-quality approvals

::: good
![Figure: Good example - Scaled approvals - The group of people in charge of a cross approval are called a XXX Master](cross-approvals.png)
:::

### Developing the approval system

There are 5 steps to developing the new system of approvals:

1. **Identify** - Find tasks causing "approval hell" aka bottlenecks
2. **Assign** - Appoint trusted subject matter experts to be responsible
3. **Classify** - Determine the importance of the task
4. **Implement** - Document and induct the new approvers
5. **Monitor** - Keep track of each employee's responsibilities

#### 1. Process - Identify tasks causing "approval hell"

Look for tasks which frequently take a long time to be approved.

::: greybox
**Example:** Delays in approval for induction completion because the assigned approver is often busy.
:::

#### 2. Assign - Appoint trusted subject matter experts to be responsible

Build a list of people who are experts on that subject - they will be responsible for approvals.

Once the list is compiled, assign each person a priority. That determines the order to contact people.

::: greybox
**Tip:** Set the "original approver" as the lowest priority to minimize their involvement.
:::

::: bad
![Figure: Bad example - Adam approves the completion of everyone's induction](induction-bad.png)
:::

::: good
![Figure: Good example - There are 10 Induction Masters responsible for approving everyone's induction - in this case I would start with Brady](induction-good.jpg)
:::

#### 3. Classify - Determine the importance of the task

Some tasks are more valuable than others. For example, a task to fix spelling mistakes doesn't matter as much as deleting invoices. Therefore, you would assign more approvers to the task of deleting invoices.

Figuring out the correct number of approvals can be difficult. Generally, the idea is to reduce the amount of approvals as much as possible without sacrificing quality or risk.

Here are some guidelines:

##### Number of Approvals: 0

The gold standard is to look for a way to remove approvals entirely. This gold standard can usually be achieved for common sense fixes using tools like Grammarly and ChatGPT. For example, you may decide that any spelling mistake fix can be applied to the company induction system as long as Grammarly has verified it.

In these cases, it becomes a [rubber stamp](/rubber-stamp-prs) and a 3rd party tool acts as the approver.

::: greybox
**Example:** Fixing a typo.
:::

##### Number of Approvals: 1

Tasks that require 1 approval are usually well-documented, routine processes. In that case, the standard acts as the second approver since it is assumed that it has been followed.

::: greybox
**Example:** A routine leave request.
:::

##### Number of Approvals: 2

2 approvals are for tasks that fall into one of the following categories:

* They do not follow a well-documented process
* They frequently have variations from the process
* They are of high importance

In these cases, a 2nd approval is valuable because:

✅ It establishes confidence in the process

✅ It results in fewer mistakes slipping through

✅ A single approver may make a rushed or wrong decision

✅ The approvers hold each other accountable

::: greybox
**Example:** A purchase for $500-$5,000 (relatively expensive).
:::

##### Number of Approvals: 3+ or stick with the "original approver"

When approval is critical to the business, it is worth considering if it should be approved by a "council" of people or by the "original approver". These are tasks where a mistake could be catastrophic for the business. It's important that one of the approvers of these tasks is a senior in the relevant field. Any key stakeholders affected by the change should also be alerted.

::: greybox
**Example:** Opening a new office (costly and risky).
:::

#### 4. Implement - Document and induct the new approvers

The final step is to record all the established decisions and induct the new approvers.

1. Induct each person by having them shadow the "original approver" for at least 3 approval processes
2. Document the new approvers in a central location (e.g. Teams Approvals), naming it "{{ APPROVAL NAME }} Masters"
3. Create a template in the Teams Approvals app to ensure a standard process is followed
4. Update the relevant standard so that instead of contacting the "original approver", individuals contact the new approvers

::: good
![Figure: Good example - Read the employee instructions to see how to get it approved](v2-bench-masters-good.jpg)
:::

#### 5. Monitor - Keep track of each employee's responsibilities

One problem with this system is responsibility creep! When someone is a trusted individual within the company, they can end up with too many responsibilities, causing new bottlenecks.

To prevent this issue, create reports tracking the number of approvals people do. That way, if someone has too many, you can reallocate some of them.

![Figure: A report tracking how many approvals people do from the Teams Approvals app (structured data). Inside the form there are the right people to approve](teams-approvals-report.jpg)

![Figure: Instead of using an approvals app, this is a report tracking how many approvals people do from company emails (unstructured data). Each person needs to first manually look up who is the employee responsible for approving the email](eagle-eye-report.jpg)

The tool is called [SSW EagleEye](https://www.ssweagleeye.com/).

## Handling conflicts

Sometimes, approvers may run into a controversial approval or be unsure about an approval. Approvers may also have differing views about how to handle an approval.

Disputes between 2 approvers can be solved as follows:

1. The 2 approvers should have a call to get aligned about how to solve the problem
2. If they still cannot agree, they should call in a 3rd approver to mediate
3. If they still cannot agree, then the original approver should act as arbiter

## Communicating the streamlined approvals process

This process should ideally be implemented across all business bottlenecks. However, identifying the most problematic approvals can be challenging.

To solve this, communicate the new approval process company-wide, encouraging employees to suggest areas for implementation. This crowdsourcing approach should yield valuable feedback on where to apply the streamlined approval process.
