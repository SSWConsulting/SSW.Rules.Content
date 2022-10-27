---
type: rule
title: Do you keep a package audit log?
uri: package-audit-log
authors:
  - title: Piers
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-10-27T05:23:16.827Z
guid: 0a63d71e-66f0-4583-8a9c-6252df92ea34
---
Packages are the life blood of any software project. However, if the team is not careful, that life blood can turn into a heavy weight dragging the application down. It's too easy for 10 packages to turn into 1000.

That's why it's crucial to maintain a package audit log.
            
<!--endintro-->

A package audit log helps developers to keep track of why packages are added, who added them and who approved them.

Generally, keep track of packages in a different file for each project in the solution.

There are 6 attributes to keep track of:
- Name
- Link to npm/NuGet
- Action (aka added or removed)
- Actioned by
- Approved by
- Why the change was made

### Ensure it gets updated
It's imperative that the package audit log is updated every time a package is added or removed. So, add it to the Sprint Review as an item to action every week, that way the team is aware of all changes, and also any missed changes are caught.

TODO: Do you like it manual or having a pr that you put 

### TODO: Add template of md