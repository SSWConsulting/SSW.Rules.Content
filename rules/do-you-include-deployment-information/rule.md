---
type: rule
archivedreason:
title: Do you include deployment information?
guid: 1f53c8c5-a294-4ac1-8f86-daf6a98fae64
uri: do-you-include-deployment-information
created: 2021-06-23T05:06:33.0000000Z
authors:
- title: Chris Briggs
  url: https://au.linkedin.com/in/chrisbriggsy
related: []

---
 
Every page on a website should have a version number. We have found this is the best way to keep track of changes to the site. 
Display the version number at the bottom of the page. 
The version information should display the application version number, the database version number and optionally the date last updated.
The version number increase and display should be automated to avoid developer error, and the best way to do this is to use the Version component from SSW.Framework.MVC.

 <!--endintro-->
 
::: good  
![Figure: Good example - Version information from SSW TimePRO](https://user-images.githubusercontent.com/86330472/123017625-4e1caf00-d410-11eb-931e-fc481a0c31d9.png)
:::

::: good
![Figure: Better example - SSW Website displays Continuous Deployment information including date and changeset](https://user-images.githubusercontent.com/86330472/123017681-6987ba00-d410-11eb-933e-47ee6dcf9f1a.png)
:::
