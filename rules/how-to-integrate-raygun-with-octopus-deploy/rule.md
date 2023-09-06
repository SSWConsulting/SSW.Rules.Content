---
type: rule
archivedreason: 
title: Do you know how to integrate RayGun with Octopus Deploy?
guid: 0a1156d2-6418-4c44-bf30-46f8d2bee405
uri: how-to-integrate-raygun-with-octopus-deploy
created: 2016-10-25T17:17:59.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-know-how-to-integrate-raygun-with-octopus-deploy

---

One of the best features of RayGun is the ability to track crash reports against deployments. This feature allows you to tell if a particular deployment has introduced a lot of new bugs or caused a regression of exceptions.

To set it up:

<!--endintro-->

1. Under Deployments
2. Select Octopus Deploy (Set up)

![](raygun-octopus-1.jpg)  
    Raygun will product you with a [PowerShell script](https://raygun.com/docs/deployments/octopus-deploy) to add into your octopus deployment steps that will call the RayGun API and log a new deployment
3. Trigger a new deployment
4. Then you’ll see the deployment in RayGun

![](raygun-octopus-2.png)  
Drilling into a deployment you’ll see:

* New errors
* Regressions
* Recurring errors

::: good  
![Figure: Good Example – Now you can measure the quality of your deployments](raygun-octopus-3.jpg)  
:::
