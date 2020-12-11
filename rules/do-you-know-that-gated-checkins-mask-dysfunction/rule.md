---
type: rule
archivedreason: 
title: Do You Know That Gated Checkins Mask Dysfunction?
guid: 72d53450-adcc-4e4f-a993-729a7bc73a29
uri: do-you-know-that-gated-checkins-mask-dysfunction
created: 2012-11-01T15:15:53.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---

Gated checkins are used to stop developers from checking in bad code and breaking the build.

This does not contribute to high functioning teams, and instead masks, or even creates dysfunction.

<!--endintro-->


::: greybox

In the retro the team decides to turn gated checkins on because Jonny and Sue keep breaking the build.

The build doesn’t get broken any more, because Jonny and Sue now have to fix their code before they check it in.

This doesn’t mean that Jonny and Sue are writing better code, it just means that they are not checking in code that breaks the build.

Gated checkins will not improve their skill level, change their attitude or improve the quality of their code.

The development ninjas on the team are proud of their code, and check in several times per day. Because the gated checkin takes 10 minutes their workflow is impacted.

They resent Jonny and Sue for having to work this way.

Gated Checkins mask the dysfunction on the team, and introduce impediments to the high performers.

:::

Bad Example – Gated Checkins mask dysfunction

::: greybox

In the retro the team discusses the fact that the build is often broken.
 After a round table discussion about becoming better programmers and building better quality software, the team decides to the following guidelines:

1. The team will all run build notifications so that everyone knows when, and by whom the build is broken.
2. If someone needs help with solving a problem, they are going to feel good about asking for help early, and learning something new in the answer.
3. If someone is asked for help, they will gladly share their knowledge to ensure that the quality of the project is maintained ,and the team help each other to become better developers.
4. Before checking in, the devs will compile and run all tests. \*\*
5. If someone checks in and does break the build, they will call out to all members of the team that the build is broken so that no-one gets latest.<br>They will fix the build IMMEDIATELY, and then call out again when it is fixed.<br>(Some teams have a rule that if you break the build three times you have to shout coffee / lunch).
6. The team agrees that you don’t go home if the build isn’t green. <br>If it comes to the end of the day and you are not sure your code will not break the build – do not checkin. Create a shelveset and resolve the issue properly the next day.
<br>If you have checked in, the build is broken, and you cannot fix it before going home, you must email all devs on the team, and the product owner with an explanation.
7. The status of the build is reviewed in every daily scrum.


:::

Good Example – The whole team should be constantly aware and invested in the status of the build, the quality of the software and in encouraging each other to better developers.
\*\* I actually don’t follow this rule when working on small teams of awesome devs, who write code against tests and checkin frequently.

Instead I encourage the process to be:

* checkin 4-5 times a day
* write lots of tests
* if the tests that you are working against pass- checkin and let the build server do a full compile and run all the tests
* if you have broken the build, call it out, fix it immediately and then call it out again.


This is the most productive way for small teams of awesome developers to produce great code… and it's fun !
