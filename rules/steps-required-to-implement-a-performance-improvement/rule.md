---
type: rule
archivedreason: 
title: Do you know the steps required to implement a performance improvement?
guid: 7d74c3e9-58ce-4ec1-b1c3-22a02e7cfc83
uri: steps-required-to-implement-a-performance-improvement
created: 2020-06-10T20:48:27.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
related:
- do-you-avoid-reviewing-performance-without-metrics
- have-tests-for-performance
redirects:
- do-you-know-the-steps-required-to-implement-a-performance-improvement

---

The following steps will help to guide efforts to implement a performance improvement. The key is to only make a small change with each iteration and run a performance test to ensure that change resulted in an improvement.

<!--endintro-->

1. Establish a performance target (goal posts)
2. Build an automated performance test
3. Run the performance test to establish a baseline (the current performance data)
4. Make a *small*change to the process
5. Run the performance test again to measure the impact of the single improvement against the baseline
6. If the change results in a measurable performance improvement, then keep it
7. Repeat steps 4 to 6 until the performance target has been met

For  **bonus points** when you're ready to deploy to production:

1. Run the performance test against production to establish a production baseline
2. Deploy the changes to production
3. Run the performance test to measure the impact of the improvements
4. Provide the performance improvement results to your Product Owner and bask in the shower of compliments coming your way for a job well done!

Working against a baseline and having a defined target will ensure that you are not prematurely or over optimizing your process.

