---
type: rule
archivedreason: archived as duplicate
title: Do you establish a baseline?
guid: 75df8950-b8f0-4c41-b438-1e863a4f7fab
uri: do-you-establish-a-baseline
created: 2016-04-28T17:56:10.0000000Z
authors:
- id: 3
  title: Eric Phan
related: []

---


<p>most important part of performance tuning is being able to quantify the process. This is why it’s super important that before you touch any code or SQL, that a measurement be taken of the current performance. Now the general rule is to make sure the tests are being run on the same or similar hardware to production and that the test always be run on the *<strong>same infrastructure</strong>* - otherwise you’d be comparing apples with oranges .</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​​Once you establish that baseline, you can then incrementally measure the performance impact for each change being made. This way you can measure effort vs reward as you could be working on a tweak for weeks that only improves performance by a few milliseconds whereas spending an hour to bundle and minify assets might yield a 50% improvement. </p>


