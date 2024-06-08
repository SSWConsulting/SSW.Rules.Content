---
type: rule
archivedreason: 
title: Do you know The Levels to Git Mastery?
guid: c15e35de-6e6c-4034-bc7d-d81ba02469e7
uri: the-levels-to-git-mastery
created: 2016-02-15T19:15:15.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
- do-you-know-the-levels-to-git-mastery

---

Like most skills, it can take a little while to get your head around Git.
We rate our devs and the devs that we mentor on the following scale.

**Where are you?**

<!--endintro-->

### \*\* Level 1 - Understanding the basic principles

At this level, you need to have an understanding of the basic operations (including branching).

Your workflow looks like this:

* init local repository / clone
* pull
* &lt;code&gt;
* commit
* push


### \*\* Level 2 -  Working with Git on a team

Now that you know the basic Git commands you can start working on projects with more than one developer.

You should be using local feature branches for your work.

Your workflow involves:

* pull
* merge
* push


### \*\* Level 3 - Learning to use pull requests 

Pull requests can be used for code reviews within your team, or to accept suggested changes from people outside your team.

Pull requests should preferably be used with policies (TFS Git only  - harder with GitHub).

### \*\* Level 4 -  Working with a team advanced - Rebasing (harder, but worth it) 

When working in a team, Git does a pretty good job of merging code together from different branches... but it can be very messy. 
True Git masters master [rebasing](/rebase-not-merge). It lets you keep a much cleaner project history.

Git process for Git masters:

* pull master
* rebase feature branch on top of remote master
* push feature branch to remote or create pull request
