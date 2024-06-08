---
type: rule
title: Do you avoid creating multiple Team Projects for the same project?
uri: avoid-creating-multiple-team-projects-for-the-same-project
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
created: 2021-09-20T21:06:37.714Z
archivedreason: "Piers: We don’t use TFS anymore and even if we did, this rule
  looks very outdated. "
guid: 3fbe41ba-5650-410a-a84b-f6fd7b507539
---
TFS uses Team Project to manage sources code, Work Items and other project related document; the source control allows you to create multiple solution folders under the same Team Project to meet your need. You shouldn't create multiple Team Projects for the same project as this make it very difficult to query the Work Items, create reference between projects and make builds.

TFS Team Project should be considered from a project management point of view instead of technical point of view, you should use a Team Project to manage all resources in your project, including source code, documentations and reports etc. If you are separating the related source code into different Team Project, you will find it's difficult for you to decide the location of your other resources should be going to, like your release plan, project update etc.\
<!--endintro-->

![Figure: Bad Example - Multiple Team Projects for the same product](bad-multiple-projects.gif)



![Figure: Good Example - Multiple solution folders in the same Team Project](good-multiple-folders.gif)