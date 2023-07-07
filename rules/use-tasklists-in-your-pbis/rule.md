---
type: rule
title: Do you use tasklists in your PBIs
uri: use-tasklists-in-your-pbis
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
related: 
  - number-tasks-questions
redirects: []
created: 2023-07-06T23:11:00.000Z
archivedreason: null
guid: 2dbeeeb3-537f-4cbd-962d-df68ce153f93
---
  
There are many ways to write tasks in PBIs, but the best way is to use tasklists. This allows you to see the progress of the PBI at a glance as well as avoid any unintentional tasks being tracked. Below is the different ways you could write tasks in PBIs.

<!--endintro-->

### Numbering tasks

When sending tasks in email, you might [number your tasks](https://ssw.com.au/rules/number-tasks-questions/) to make it clear what you want. 

![Figure: Numbering tasks in PBIs works but isn't fully utilizing the platform](numbering-tasks.jpg)

Although this would work in PBIs, it's not the best way to do it in GitHub.

### Using checklists

You can use checkboxes in PBIs to create a checklist for tasks

![Figure: You can click the tasks toolbar button or simple type in a task which is recognized as "- \[ \]"](task-checklist.jpg)

This will show a visual que as to how many tasks you've completed for the PBI. You'll also be able to easily convert a task into it's own issue to detail it out further or have more in-depth conversations around the issue specifically.

![Figure: The tasks will light up at the top of the issue and you can easily create new issues from tasks](task-checklist-view.jpg)

One of the downsides to using checklists is that any checkbox in the issue description would show up as a task. This means that if you had a checkbox in the description that wasn't a task, it would show up as a task. This is why we recommend using tasklists.

![Figure: When you have more checkboxes, e.g. for bug reports. Your task indicator will not be accurate](task-checklist-incorrect-tasks.jpg)

### Using tasklists (recommended)

Lastly you should use the tasklist for your tasks, this gives the same advantages as standard checklists without interference from other checkboxes. 

![Figure: Using tasklist requires a little extra markdown around your checkboxes](tasklists-markdown.jpg)

Besides the benefits described above, there's also the advantage of having a UI component built specifically to markup a tasklist.

![Figure: Using tasklist requires a little extra markdown around your checkboxes](tasklists-markdown.jpg)

You can see from the UI component there is a convenient button to add a task as well as a menu list of options to convert, rename and remove tasks all through the UI. This is great for team members who don't feel comfortable with markdown.
