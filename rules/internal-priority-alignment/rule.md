---
seoDescription: 
type: rule
archivedreason:
title: Do you have a Priority Alignment meeting?
guid: ea9036b3-649f-4555-8a4b-8ba7de56de50
uri: internal-priority-alignment
created: 2024-10-11T00:00:00.0000000Z
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
related:
  - know-where-your-staff-are
  - bench-master
redirects: []
---

[Bench Masters](/bench-mastes) are responsible for ensuring that developers get put on projects that align with the companies goals and the developers' career goals. This means they need to stay aligned with the company' stakeholders and keep them informed of the developers' focus.
Bench Masters also help employees blocked by a company stakeholder to get unblocked.

This alignment can be achieved through a weekly meeting with the Bench Masters and stakeholders called the Priority Alignment meeting.

The following meeting structure should be followed

::: email-template  

|          |                                                      |
| -------- | ---------------------------------------------------- |
| To:      | {{ COMPANY STAKEHOLDERS }}                           |
| Subject: | ⚖️ Bench Master Priority Alignment - {{ DATE }} |
::: email-content  

Hey {{ COMPANY STAKEHOLDERS }},

1. Watch the recording
    {{ RECORDING URL }}

The goal is to use our internal devs on the best project.

### Attendees

{{ ATTENDEES }}

### Summary - Have there been any staffing changes for any of our internal projects in the past week?

* {{ PROJECT 1 }} - {{ STATUS 1 }}
* {{ PROJECT 2 }} - {{ STATUS 2 }}
* {{ PROJECT 3 }} - {{ STATUS 3 }}
* ❓{{ PERSON 1 }} - from {{ PREVIOUS PROJECT }} to {{ NEW PROJECT }} - {{ NOTE }}
* {{ PERSON 2 }} - Back on {{ PROJECT NAME }} next {{ DATE }}

### 🛑 Blocked people (times we proxied for {{ COMPANY STAKEHOLDER }})

* {{ BLOCKED PERSON 1 }} - {{ ISSUE DESCRIPTION }}
* {{ BLOCKED PERSON 2 }} - {{ ISSUE DESCRIPTION }}

### ✅ The highlights

* {{ PERSON }} - {{ DETAILS }}

### ❌ The lowlights – any issues or concerns?

* {{ PERSON }} - {{ DETAILS }}

### Ad hoc topics

* {{ TOPIC }}

### Priorities - any new tasks that need to get done and who should do it?

Copy from last week and make changes as needed  
Legend:  
✅ Done since last meeting, remove in next week's summary  
⭐️ New/Status Change since last meeting  
⚠️ Warning - Something might not be correct here  
❌ Remove next meeting - Consider removing these as the team is not working on it

| **Product**         | **Projects**         | **Team**           |
| ------------------- | -------------------- | ------------------ |
| **{{ PRODUCT 1 }}** | {{ PROJECT DETAIL }} | {{ TEAM MEMBERS }} |
| **{{ PRODUCT 2 }}** | {{ PROJECT DETAIL }} | {{ TEAM MEMBERS }} |

<This email was sent as per the rule: [ssw.com.au/rules/internal-priority-alignment](/internal-priority-alignment)>

:::  
:::

After the meeting, the Bench Masters should record a [quick summary](/summary-recording-sprint-reviews) and send it out to the stakeholders. This is especially important for stakeholders who couldn't attend.

## Where do I store the meeting artifacts?

Microsoft loop is a good option, but its important to copy them into an email and send them out to the stakeholders.
